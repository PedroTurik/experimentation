from flask import Flask, request
from subprocess import PIPE, Popen

app = Flask(__name__)

@app.route('/')
def std():
	get_request = request.args.get('s')
	
	a = Popen(f"figlet {get_request}", shell=True, stdout=PIPE)
	
	print(b:=a.communicate()[0].decode())
	return f'Hello, ' + b.replace('\n', "<br >\n")
