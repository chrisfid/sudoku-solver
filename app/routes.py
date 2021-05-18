from flask.helpers import url_for
from app import app
from flask import render_template, request, redirect, session
from app.solve import SudokuSolver
import random

@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    if request.form['sudoku'] == 'Reset':
      session['board'] = SudokuSolver.empty_board()
    elif request.form['sudoku'] == 'Solve':
      cells = request.form.getlist('cells', type=int)
      board = SudokuSolver.multidict_to_board(cells)
      s1 = SudokuSolver(board)
      s1.solve()
      session['board'] = s1.board
    elif request.form['sudoku'] == 'Random':
      session['board'] = random.choice(SudokuSolver.samples())
    return redirect(url_for('index'))

  if request.method == 'GET':
    board = SudokuSolver.empty_board()
    try:
      board = session['board']
    except Exception as e:
      print(e)
    return render_template("index.html", board=board)