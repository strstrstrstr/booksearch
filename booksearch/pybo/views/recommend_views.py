from flask import Blueprint, render_template, request, url_for,g
from werkzeug.utils import redirect

import folium
import testdb
from pybo import db
from pybo.forms import QuestionForm, AnswerForm, BookRentForm
# from pybo.models import Question
from datetime import datetime
import pybo.libraryApi as lbApi
import random

from pybo.machine import find_sim_book
from pybo.models import History
from pybo.naverbookapi import booksearch_info, yes24_steady_sell

bp = Blueprint('recommend', __name__, url_prefix='/recommend')


@bp.route('/list',methods=('GET','POST'))
def recommend_list():
    try:
        if g.user == None:
            return redirect(url_for('search.search'))
        # for temp in g.user.user_set:
        #     print(temp.bookname)
        print('-'*40)
        print(g.user.username)
        print(g.user.user_set[-1].bookname)
        print('-'*40)
        recommend_list=find_sim_book(g.user.user_set[-1].bookname)
        print(recommend_list)

        result = []
        for temp in recommend_list:
            result.append(booksearch_info(temp))
    except:
        recommend_list = yes24_steady_sell()
        result = []
        for temp in recommend_list:
            result.append(booksearch_info(temp))
    print('-'*40)
    print(result)
    return render_template('search/search_list.html', bookList=None,recommend=result)

# @bp.route('/booking/<int:key,char>', methods=('GET', ))
# def booking(key,char1):
#
#     print(char1)
#     print(key)
#     return redirect(url_for('recommend.recommend_list'))

@bp.route('/booking', methods=('GET', ))
def booking_recommend():
    if g.user:
        bookname = request.args.get('bookname')
        print(bookname)
        isbn13= request.args.get('isbn13')
        print(isbn13)
        g.user.user_set.append(History(bookname=bookname, isbn13=isbn13))
        db.session.commit()
        return redirect(url_for('search.search'))
    else:
        return redirect(url_for('search.search'))