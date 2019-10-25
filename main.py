@app.route('/mul')
def mul():
    dict = request.args.to_dict()
    A = eval(dict['A'])
    B = eval(dict['B'])
    result = A*B
    return 'result: %s' % result
