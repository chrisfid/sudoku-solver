from app.solve import SudokuSolver
from flask import Flask
from app.solve import SudokuSolver
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
solver = SudokuSolver()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

from app import routes

app.run(debug=os.environ.get('DEBUG'))
