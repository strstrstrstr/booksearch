from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect

import folium
import testdb
from pybo import db
from pybo.forms import QuestionForm, AnswerForm, BookSearchForm
from pybo.models import Question
from datetime import datetime
import pybo.libraryApi as lbApi
import random
bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/search')
def search():
    ranNum = random.randrange(1, 10)
    url = lbApi.url()
    bestSeller = lbApi.bestSeller(url)
    bookname= bestSeller['response']['docs'][ranNum]['doc']['bookname']
    return render_template('search/search.html', bestSeller=bookname)

@bp.route('/location',methods=('GET', 'POST'))
def location():
    bookNm = request.form.get('bookNm')

    return render_template('search/location.html')

@bp.route('/list',methods=('GET', 'POST'))
def search_list():
    bookNm = request.form.get('bookNm')
    print(bookNm)
    url = lbApi.url()
    bestSeller = lbApi.bookSearch(url, bookNm)
    print(bestSeller)
    return render_template('search/search_list.html')