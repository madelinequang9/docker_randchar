from flask import Flask
import random
import string
import os.path
from os import path

app = Flask(__name__)
@app.route('/')
def randstring():
	rand = ''
	continfile = ''
	for i in range(100):
		rand += random.choice(string.ascii_letters + string.digits)

	if(path.exists('random.txt')==True):
		file=open('random.txt')
		continfile=file.read()
		file.close()
	file=open('random.txt', 'w')
	file.write(rand)
	file.close()
	file=open('random.txt')
	newcont=file.read()
	file.close()
	return "Old Content in file: " + continfile + "\nNew Content in file: " + newcont + "\n"


if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5000)

