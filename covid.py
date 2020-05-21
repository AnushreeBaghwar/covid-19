from flask import Flask,render_template
from bs4 import BeautifulSoup as bs
import requests
app=Flask(__name__)
@app.route('/')
def covid():
	return render_template('home.html')

@app.route('/update')
def update():
	return render_template('updatecor.html')

@app.route('/reslt')
def reslt():
	return render_template('result.html')

if __name__ == '__main__':
	app.run()