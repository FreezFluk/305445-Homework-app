from flask import Flask, request
from flask_restful import Resource , Api , reqparse
import json , time 
from werkzeug.datastructures import FileStorage

app = Flask (__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('info')
parser.add_argument('image',type=FileStorage,location='files')

class Hello(Resource):
	def get(self):
		return {"massage": "'./born' to calculate age or './image' to upload picture file"}


class Image(Resource):
	def get(self):
		return {"massage": "This get method you should change to method post"}
	def post(self):
		args = parser.parse_args()
		image = args['image']
		image_name = image.filename
		image.save(image_name)
		return {"code":200,"desc":"upload success"}

api.add_resource(Hello,'/')
api.add_resource(Image, '/image')

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5500)
