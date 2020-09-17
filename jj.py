@app.route('/home')
def home():
    return redirect(url_for('about', name='World'))

@app.route('/about/<name>')
def about(name):
    return f'Hello {name}'