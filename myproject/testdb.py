from pybo.models import Question,Answer
from datetime import datetime
from pybo import db


def test(m):
    q= Question(subject= '질문 %d입니다...'%(m),content='질문 %d 에대한 내용 입니다 ㅎㅎ'%(m),create_date=datetime.now())
    db.session.add(q)
    # db.session.commit()

def test10():
    for temp in range(1,11):
        test(temp)
    db.session.commit()

def getall_question():
    a= Question.query.get(1)
    db.session.delete(a)
    db.session.commit()

    # result = Question.query.all()

    # for temp in result:
    #     print(temp.subject)
    #     print(temp.content)