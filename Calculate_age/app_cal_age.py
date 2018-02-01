from flask import Flask, request
from flask_restful import Resource , Api , reqparse
import json , time 
from datetime import datetime, date

app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('info')
parser.add_argument('birthdate')

def cal_age(born):
	today = date.today()
	return today.year-born.year-((today.month,today.day)<(born.month,born.day))

class Hello(Resource):
	def get(self):
		return {"massage": "'./born' to calculate age or './image' to upload picture file"}

class Birthdate(Resource):
	def get(self):
		return {"massage": "This get method you should change to method post"}
	def post(self):
		args = parser.parse_args()
		birthdate = args['birthdate']
		datetime_object = datetime.strptime(birthdate,'%d-%m-%Y')
		age = int(cal_age(datetime_object))
		return {"birthdate": datetime_object.strftime('%d-%m-%Y') , "age":age}

api.add_resource(Hello,'/')
api.add_resource(Birthdate,'/born')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
