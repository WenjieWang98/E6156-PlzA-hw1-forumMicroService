from flask import *
from config import db
import random
import time
import config


app = Flask(__name__)

# config
app.config.from_object(config)


# # keep login
# @app.context_processor
# def login_status():
#     # 从session中获取id
#     uid = session.get('id')
#     if uid:
#         try:
#             cur = db.cursor()
#             sql = "select nickname,email from UserInformation where id = '%s'" % uid
#             db.ping(reconnect=True)
#             cur.execute(sql)
#             result = cur.fetchone()
#             if result:
#                 return {'id': uid, 'email': result[1], 'nickname': result[0]}
#         except Exception as e:
#             raise e
#     # 如果id信息不存在，则未登录，返回预设值
#     return {'id': 1, 'email': "sw@gmail.com", 'nickname': "Sixuan"}


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# random id
def gengenerateID():
    re = ""
    for i in range(128):
        re += chr(random.randint(65, 90))
    return re


# Post
@app.route('/post_issue', methods=['GET', 'POST'])
def post_issue():
    if request.method == 'GET':
        return render_template('post_issue.html')
    if request.method == 'POST':
        title = request.form.get('title')
        comment = request.form.get('text')
        if session.get('id'):
            uid = session.get('id')
        else:
            uid = 1
        issue_time = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            cur = db.cursor()
            Ino = gengenerateID()
            sql = "select * from Issue where Ino = '%s'" % Ino
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()

            while result is not None:
                Ino = gengenerateID()
                sql = "select * from Issue where Ino = '%s'" % Ino
                db.ping(reconnect=True)
                cur.execute(sql)
                result = cur.fetchone()
            sql = "insert into Issue(Ino, id, title, issue_time) VALUES ('%s','%s','%s','%s')" % (
                Ino, uid, title, issue_time)
            db.ping(reconnect=True)
            cur.execute(sql)
            db.commit()
            sql = "insert into Comment(Cno, Ino, comment, comment_time, id) VALUES ('%s','%s','%s','%s','%s')" % (
                '1', Ino, comment, issue_time, uid)
            db.ping(reconnect=True)
            cur.execute(sql)
            db.commit()
            cur.close()
            return redirect(url_for('formula'))
        except Exception as e:
            raise e


# main page
@app.route('/formula')
def formula():
    if request.method == 'GET':
        try:
            cur = db.cursor()
            sql = "select Issue.Ino, Issue.id,UserInformation.nickname,issue_time,Issue.title,Comment.comment from Issue,UserInformation,Comment where Issue.id = UserInformation.id and Issue.Ino = Comment.Ino and Cno = '1' order by issue_time DESC "
            db.ping(reconnect=True)
            cur.execute(sql)
            issue_information = cur.fetchall()
            cur.close()
            return render_template('formula.html', issue_information=issue_information)
        except Exception as e:
            raise e


# detail
@app.route('/issue/<Ino>', methods=['GET', 'POST'])
def issue_detail(Ino):
    if request.method == 'GET':
        try:
            if request.method == 'GET':
                cur = db.cursor()
                sql = "select Issue.title from Issue where Ino = '%s'" % Ino
                db.ping(reconnect=True)
                cur.execute(sql)

                issue_title = cur.fetchone()[0]
                sql = "select UserInformation.nickname,Comment.comment,Comment.comment_time,Comment.Cno from Comment,UserInformation where Comment.id = UserInformation.id and Ino = '%s'" % Ino
                db.ping(reconnect=True)
                cur.execute(sql)
                comment = cur.fetchall()
                cur.close()
                return render_template('issue_detail.html', Ino=Ino, issue_title=issue_title, comment=comment)
        except Exception as e:
            raise e

    if request.method == 'POST':
        Ino = request.values.get('Ino')
        if session.get('id'):
            uid = session.get('id')
        else:
            uid = 1
        comment = request.values.get('text')
        comment_time = time.strftime("%Y-%m-%d %H:%M:%S")
        try:
            cur = db.cursor()
            sql = "select max(Cno) from Comment where Ino = '%s' " % Ino
            db.ping(reconnect=True)
            cur.execute(sql)
            result = cur.fetchone()
            Cno = int(result[0]) + 1
            Cno = str(Cno)
            sql = "insert into Comment(Cno, Ino, comment, comment_time, id) VALUES ('%s','%s','%s','%s','%s')" % (
            Cno, Ino, comment, comment_time, uid)
            cur.execute(sql)
            db.commit()
            cur.close()
            return redirect(url_for('issue_detail',Ino = Ino))
        except Exception as e:
            raise e


if __name__ == '__main__':
    app.run()
