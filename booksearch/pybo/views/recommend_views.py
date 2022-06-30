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
from pybo.naverbookapi import booksearch_info, yes24_steady_sell

bp = Blueprint('recommend', __name__, url_prefix='/recommend')


@bp.route('/list',methods=('GET',))
def recommend_list():
    try:
        if g.user == None:
            return redirect(url_for('search.search'))
        # for temp in g.user.user_set:
        #     print(temp.bookname)
        print(find_sim_book(g.user.user_set[-1].bookname))
        recommend_list=find_sim_book(g.user.user_set[-1].bookname)
        result = []
        for temp in recommend_list:
            result.append(booksearch_info(temp))
    except:
        recommend_list = yes24_steady_sell()
        result = []
        for temp in recommend_list:
            result.append(booksearch_info(temp))

    return render_template('search/search_list.html', bookList=None,recommend=result)