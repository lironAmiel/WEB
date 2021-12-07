import os
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello world'

@app.route('/redirect')
def helloRedirect():
    return redirect(url_for('hello'))

@app.route('/amazone')
def helloAmazone():
    return redirect('/')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)