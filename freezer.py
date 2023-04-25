from flask_frozen import Freezer
from main import app
import requests

freezer = Freezer(app)


@freezer.register_generator
def contact():
    yield '/contact'


@freezer.register_generator
def about():
    yield '/about'


@freezer.register_generator
def get_blog():
    yield '/post.html'


if __name__ == '__main__':
    freezer.freeze()
