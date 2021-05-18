from flask import Flask, session

app = Flask(__name__)
app.config['SECRET_KEY'] = b'OQX\xf7|]\xd8\xee\xc6\xe5\xeb\x02\xfb\x8f\xc3\xbd'

from app import routes

app.run(debug=True)