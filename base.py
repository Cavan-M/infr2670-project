from flask import Flask

app = Flask(__name__)

@app.route('/')
def mainFunction():
	return "TEST"

if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0")
