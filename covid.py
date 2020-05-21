from flask import Flask,render_template
from bs4 import BeautifulSoup as bs
import requests
app=Flask(__name__)
@app.route('/')
def covid():
	return render_template('home.html')

@app.route('/update')
def update():
	return render_template('updatecor')

@app.route('/reslt')
def reslt():
	url="https://www.worldometers.info/coronavirus/"
	res=requests.get(url)
	soup=bs(res.text,"html.parser")
	table=soup.select_one("#main_table_countries_today")
	tbody=table.select_one("tbody")
	tr_list=tbody.select("tr")
	return render_template('result.html')

if __name__ == '__main__':
	app.run()