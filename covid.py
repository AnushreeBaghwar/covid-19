from flask import Flask,render_template
app=Flask(__name__)
@app.route('/')
def covid():
	return render_template('home.html')
if __name__ == '__main__':
	app.run()#kuch ni ki hu abhi ayi