from wsgiref.simple_server import make_server

from hello_server import application

httpd = make_server('', 8000, application)
print('开始监听8000端口。。。')
httpd.serve_forever()