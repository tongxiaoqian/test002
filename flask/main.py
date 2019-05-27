from flask import Flask
# 创建flask框架
# 静态文件访问的时候url匹配时，路由规则里的路径名字 默认值是、static
app = Flask(__name__, static_url_path='/static')
print(app.url_map)
# @app.route('/')
# def index():
# 	"""处理index页面逻辑"""
# 	return 'nihao'
@app.route('/login.html')
def login():
    """登录的逻辑"""
    # 读取login.html 并且返回
    with open('login.html') as f:
        content = f.read()
    return content


if __name__ == '__main__':
    # 运行服务器、
    app.run()
