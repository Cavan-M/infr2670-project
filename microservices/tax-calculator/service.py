from flask import Flask
import requests

app = Flask(__name__)

@app.route('/')
def mainFunction():
	return "Uh Oh! Looks like something went wrong..."


@app.route('/api/<query>')
def microservice(query):
	q = query.split('+')
	rates = {'AB': 1.05,
		'BC': 1.12,
		'MN': 1.12,
		'NB': 1.15,
		'NF': 1.15,
		'NT': 1.05,
		'NS': 1.15,
		'NV': 1.05,
		'ON': 1.13,
		'PE': 1.15,
		'QC': 1.14975,
		'SK': 1.11,
		'YK': 1.05}
	total = rates[q[0]] * float(q[1])
	return "%.2f" % total


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=7865)
