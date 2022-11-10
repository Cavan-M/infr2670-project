from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def mainFunction():
	return "Uh Oh! Looks like something went wrong..."


@app.route('/api/<query>')
def microservice(query):
	q = query.split('+')
	endpoints = ["https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/",
		"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/",
		"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/latest/currencies/",
		"https://raw.githubusercontent.com/fawazahmed0/currency-api/1/latest/currencies/"]
	
	for url in endpoints:
		r = requests.get(url + q[0] + '/' + q[1] + '.json')
		if r.status_code != 403:
			break	
	
	return r.text


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=7863)
