from flask import Flask,render_template
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
	url="https://api.covid19india.org/raw_data2.json"
	res=requests.get(url)
	return render_template('result.html',data=res.json()['raw_data'])



	return render_template('result.html')

if __name__ == '__main__':
	app.run()