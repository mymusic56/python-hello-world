from flask import Flask, request, render_template


app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return '<h1>Home</h1>'

@app.route('/user/list', methods=['GET','POST'])
def userList():
    dList = [{"id":"1","name":"zhangsan"}, {"id":"2","name":"lisi"}]
    return render_template('list.html', dataList=dList)


if __name__ == '__main__':
    app.run('', 8000)

