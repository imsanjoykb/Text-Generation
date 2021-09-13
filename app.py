from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def index_phish():
    return render_template('index.html')


@app.route('/index_phishscore.html')
def index_phishscore():
    return render_template('index_phishscore.html')



if __name__ == '__main__':
	  app.run(debug=True)