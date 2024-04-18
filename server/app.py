from flask import Flask 

app = Flask(__name__)

@app.route('/')
def hello():
    return f"<h1>Let's Gooooooo!</h1>"


if __name__ == '__main__':
    app.run(port=5555, debug=True)