

from flask import Blueprint, request

from pybo.naverapi import naver_blog

bp = Blueprint('naver', __name__, url_prefix='/naver')


@bp.route('/blog')
def blog():

    key = request.args.get('keyword')
    print(key)
    content = naver_blog(key)
    return {'result' : content}


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'