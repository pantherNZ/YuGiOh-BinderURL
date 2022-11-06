from src.models import ShortUrls
from src import app, db
from random import choice
import string
from datetime import datetime
from flask import request, Response, redirect


def generate_short_id(num_of_chars: int):
    """Function to generate short_id of specified number of characters"""
    return ''.join(choice(string.ascii_letters+string.digits) for _ in range(num_of_chars))


@app.route('/', methods=['POST'])
def index():
    url = request.form['url']

    if not url:
        return Response("Request requires input URL to generate from", status=400)

    short_id = str()
    while len(short_id) == 0 or ShortUrls.query.filter_by(short_id=short_id).first() is not None:
        short_id = generate_short_id(8)

    new_link = ShortUrls(original_url=url, short_id=short_id, created_at=datetime.now())
    db.session.add(new_link)
    db.session.commit()
    short_url = request.host_url + short_id

    return {'url': short_url}



@app.route('/<short_id>')
def redirect_url(short_id):
    link = ShortUrls.query.filter_by(short_id=short_id).first()
    if link:
        return redirect(link.original_url)
    else:
        return Response("Invalid redirect URL", status=400)