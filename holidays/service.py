from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def mainFunction():
	return "Uh Oh! Looks like something went wrong..."


@app.route('/api/<query>')
def microservice(query):
	q = query.split('-')
	endpoint = "https://holidays.abstractapi.com/v1/?api_key=7317002954904e1890da6aafd4c23643&country=" + q[0] + "&year=" + q[1] + "&month=" + q[2] + "&day=" + q[3]
	r = requests.get(endpoint)
	
	return r.text


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=7864)
