from flask import render_template, request, redirect, session
from flask.helpers import url_for
from app import app, solver


@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Reset
        if request.form['sudoku'] == 'Reset':
            session['board'] = solver.create_empty_board()
        # Solve
        elif request.form['sudoku'] == 'Solve':
            cells = request.form.getlist('cells', type=int)
            board = solver.multidict_to_board(cells)
            session['board'] = solver.solve(board)
        # Randomize
        elif request.form['sudoku'] == 'Randomize':
            session['board'] = solver.new_board(level=1)
        return redirect(url_for('index'))

    if request.method == 'GET':
        # Try to get a board from a session
        try:
            return render_template("index.html", board=session['board'])
        except:
            return render_template("index.html", board=solver.create_empty_board())
