from analyzer import app

@app.route("/hello")
def hello():
    return "Hello, World!"
