from flask import Blueprint, render_template, request, url_for
from flask_wtf import form
from werkzeug.utils import redirect

import folium
import testdb
from pybo import db
from pybo.forms import QuestionForm, AnswerForm, BookRentForm
# from pybo.models import Question
from datetime import datetime
import pybo.libraryApi as lbApi
import random

from pybo.models import History

bp = Blueprint('search', __name__, url_prefix='/search')


@bp.route('/search')
def search():
    ranNum = random.randrange(1, 10)
    url = lbApi.url()
    bestSeller = lbApi.bestSeller(url)
    bookname= bestSeller['response']['docs'][ranNum]['doc']['bookname']
    return render_template('search/search.html', bestSeller=bookname)

@bp.route('/location/<int:isbn>/')
def location(isbn):
    print(isbn)
    lbInfo = lbApi.bookInLibrary(isbn)['response']['libs']
    bkDt = lbApi.bookSearch(isbn)['response']['detail'][0]['book']
    print(bkDt)
    return render_template('search/location.html', bookData=bkDt, lbInfo=lbInfo)

@bp.route('/list',methods=('GET', 'POST'))
def search_list():
    bookNm = request.form.get('bookNm')
    url = lbApi.url({'pageSize=20'})
    bestSeller = lbApi.bookSearchList(url, bookNm)
    return render_template('search/search_list.html', bookList=bestSeller['response']['docs'])

# @bp.route('/hide/<int:isbn>&<booknm>', methods=('GET',))
# def book_his(isbn,booknm):
#     history = History(bookname=booknm, isbn13=isbn) # 나중에 날짜도
#     db.session.add(history)
#     db.session.commit()
#     print('성공')
#     return redirect(url_for('search.search'))
