from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainFunction():
	return "Uh Oh! Looks like something went wrong..."

@app.route('/api/<query>')
def apiFunction(query):
	q = query
	return q

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
