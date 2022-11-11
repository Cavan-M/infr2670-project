from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def mainFunction():
	return "Uh Oh! Looks like something went wrong..."


@app.route('/api/<query>')
def microservice(query):
	q = query.split('%')
	endpoint = "http://" + q[0] + '/api/' + q[1]
		
	r = requests.get(endpoint)
	return r.text


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=7860)
