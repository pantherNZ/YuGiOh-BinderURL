from flask import Flask
from src.models import ShortUrls
from src import app
from random import choice
import string

@app.route('/')
def hello_world():
    return 'Hello from Flask!'


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))