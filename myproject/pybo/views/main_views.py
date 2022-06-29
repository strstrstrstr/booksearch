from datetime import datetime

from flask import Blueprint, render_template, url_for
from werkzeug.utils import redirect
import testdb
from pybo import db
from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')


# @bp.route('/')
# def index():
#     question_list = Question.query.order_by(Question.create_date.desc())
#     return render_template('questions/question_list.html', question_list=question_list)



@bp.route('/')
def index():
    return redirect(url_for('question.list_question'))

@bp.route('/test')
def dbtest():
    for i in range(300):
        q= Question(subject='자동 생성'+str(i),content='가보자',create_date=datetime.now())
        db.session.add(q)

    db.session.commit()
    return '성공'


