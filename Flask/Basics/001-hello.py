from flask import Flask

app = Flask("FirstApp")

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/bye")
def bye():
    return "Goodbye, World!"

if __name__ == "__main__":
    app.run()