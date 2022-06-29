from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

import testdb
from pybo import db
from pybo.forms import QuestionForm, AnswerForm
from pybo.models import Question
from datetime import datetime
bp = Blueprint('question', __name__, url_prefix='/question')


@bp.route('/list')
def list_question():
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page, per_page=10)
    return render_template('questions/question_list.html', question_list=question_list)



@bp.route('/detail/<int:question_id>/')
def detail(question_id):
    question = Question.query.get_or_404(question_id)
    form = AnswerForm()
    return render_template('questions/question_detail.html', question=question,form=form)

@bp.route('/create/',methods=('GET', 'POST'))
def create():
    print(request.method,1)
    form = QuestionForm() # 새로운 객체? __init__에서 기억을 해두나? 초기화는 어디에서?
    print(request.method,form.content.data,2)
    if request.method == 'POST' and form.validate_on_submit():
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('questions/question_form.html', form=form)

# @bp.route('/test')
# def dbtest():
#     testdb.getall_question()
#     return '성공'


