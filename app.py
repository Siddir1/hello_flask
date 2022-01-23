from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "This content was read from git after commit 2nd time"

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)
