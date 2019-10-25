#!/usr/bin/env python
from flask import Flask, request, redirect, url_for

# create app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        # show html form
        return '''
            <form method="post">
                A: <input type="text" name="A" />
                B: <input type="text" name="B" />
                <p><input type="submit" name="operator" value="Add" />
                <input type="submit" name="operator" value="Sub" />
                <input type="submit" name="operator" value="Mul" />
                <input type="submit" name="operator" value="Div" />
            </form>
        '''
    elif request.method == 'POST':
        # calculate result
        a = request.form.get('operator')
        if a == 'Add':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('add', A=A, B=B))

        if a == 'Sub':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('sub', A=A, B=B))

        if a == 'Mul':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('mul', A=A, B=B))

        if a == 'Div':
            A = request.form.get('A')
            B = request.form.get('B')
            return redirect(url_for('div', A=A, B=B))
