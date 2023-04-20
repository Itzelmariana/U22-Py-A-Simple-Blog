
from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get(
    "https://api.npoint.io/d4f64a9cdeb2acb86491").json()


@app.route('/')
def home():
    return render_template("index.html",  blog_post=response)


@app.route('/contact')
def contact():
    return render_template("contact.html")


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/blog/<int:num>')
def get_blog(num):
    response = requests.get(
        "https://api.npoint.io/d4f64a9cdeb2acb86491").json()
    return render_template("post.html", blog_post=response, n=num)


if __name__ == "__main__":
    app.run(debug=True)
