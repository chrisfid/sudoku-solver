from app.solve import SudokuSolver
from flask import Flask
from app.solve import SudokuSolver
import os


app = Flask(__name__)
solver = SudokuSolver()

app.config['SECRET_KEY'] = 'WuAIg9VzjDlAopVxSK9xfQ'

from app import routes

app.run(debug=1)
