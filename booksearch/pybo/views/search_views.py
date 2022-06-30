from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

import folium
import testdb
from pybo import db
from pybo.forms import QuestionForm, AnswerForm, BookSearchForm
from pybo.models import Question
from datetime import datetime
bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/search')
def search():
    bestSeller = '신은 죽었다.'
    return render_template('search/search.html', bestSeller=bestSeller)

@bp.route('/location',methods=('GET', 'POST'))
def location():
    bookNm = request.form.get('bookNm')

    return render_template('search/location.html')
