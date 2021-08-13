from flask import render_template, request, redirect, session
from flask.helpers import url_for
from app import app, solver


@app.route("/index", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'sudoku-option' in request.form:
            # Reset
            if request.form['sudoku-option'] == 'Reset':
                session['board'] = solver.create_empty_board()
            # Solve
            elif request.form['sudoku-option'] == 'Solve':
                cells = request.form.getlist('cells', type=int)
                board = solver.multidict_to_board(cells)
                session['board'] = solver.solve(board)
            # Randomize
            elif request.form['sudoku-option'] == 'Randomize':

                session['board'] = solver.new_board(
                    level=session.get('level') if session.get('level') is not None else 1)
        elif 'sudoku-level' in request.form:
            if request.form['sudoku-level'] == 'Easy':
                session['level'] = 1
            elif request.form['sudoku-level'] == 'Medium':
                session['level'] = 2
            elif request.form['sudoku-level'] == 'Hard':
                session['level'] = 3
        return redirect(url_for('index'))

    if request.method == 'GET':
        # Try to get a board from a session
        try:
            return render_template('index.html', board=session['board'])
        except:
            return render_template('index.html', board=solver.create_empty_board())
