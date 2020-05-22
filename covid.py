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
	url="https://api.covid19india.org/data.json"
	res=requests.get(url)
	return render_template('result.html',data=res.json()['cases_time_series'],l=len(res.json()['cases_time_series']))


@app.route('/all')
def all():
	url="https://worldometers.info/coronavirus"
	res=requests.get(url)
	soup=bs(res.text)
	t_body_list=soup.select('tbody')
	t_body = t_body_list[0]
	tr_list=t_body.select('tr')
	countries_data=[]
	flags = []
	for country in tr_list:
		c=[]
		for td in country.select('td'):
			c.append(td.text)
		r = requests.get('https://restcountries.eu/rest/v2/name/'+c[1]+'?fullText=true')
		r_data = r.json()
		try:
			flags.append(r_data[0]['flag'])
		except Exception:
			flags.append('none')
			pass
		countries_data.append(c)
	return render_template('all.html',data=countries_data,l=len(countries_data),flags=flags)



if __name__ == '__main__':
	app.run()
