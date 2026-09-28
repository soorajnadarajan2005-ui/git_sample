from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return "Hello, GitHub! My first Python app."
@app.route("/about")
def about():
    return "This is my sample Flask application."
if __name__ == "__main__":
    app.run(debug=True)