from datetime import datetime

from flask import Blueprint, render_template, url_for,g
from werkzeug.utils import redirect
import testdb
from pybo import db
# from pybo.models import Question
from pybo.machine import find_sim_book
from pybo.models import User, History
from pybo.naverbookapi import booksearch_info

bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/')
# def index():
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('questions/question_list.html', question_list=question_list)



@bp.route('/')
def index():
    return redirect(url_for('search.search'))

@bp.route('/test')
def dbtest():
    # q= History(bookname='오은영의 화해',isbn13='9788997396870')
    # s= History(bookname='오이대왕',isbn13='9788958283508')
    # db.session.add(s)
    # s= History(bookname='오직 두 사람',isbn13='9788954645614')
    # db.session.add(s)
    # s= History(bookname='10배의 법칙',isbn13='9788960519145')
    # db.session.add(s)
    # s= History(bookname='휴대폰 전쟁',isbn13='9788971849866')
    # db.session.add(s)
    #
    #
    #
    #
    # db.session.commit()

    if g.user == None:
        return url_for('search.search')
    # for temp in g.user.user_set:
    #     print(temp.bookname)
    print(find_sim_book(g.user.user_set[-1].bookname))
    recommend_list=find_sim_book(g.user.user_set[-1].bookname)
    for temp in recommend_list:
        print(booksearch_info(temp))
    return '성공'


