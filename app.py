from flask import Flask, render_template, request
import os
import re

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/web.html')
def index_phish():
    return render_template('web.html')


if __name__ == '__main__':
	  app.run(debug=True)