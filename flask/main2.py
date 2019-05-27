from flask import Flask

# 创建flask框架
app = Flask(__name__, static_url_path="/static")


@app.route('/login.html')
def login():
    with open('login.html') as f:
        content = f.read()
    return content
print('haha')
print('嘿嘿')

if __name__ == '__main__':
    app.run()
