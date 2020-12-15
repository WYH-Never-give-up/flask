from app import  app
@app.route("/")
def index() :
    return "欢迎来到我的网站"
