from flask import Flask, request, jsonify, make_response
from flask_restplus import Api, Resource, fields
from sklearn.externals import joblib
import numpy as np
import os 
from flask_cors import CORS

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("service", "")

flask_app = Flask(__name__)
CORS(flask_app)
app = Api(app = flask_app, 
		  version = "1.0", 
		  title = "ML Yelp Flask/React App", 
		  description = "Predict yelp restaurant rating")

name_space = app.namespace('prediction', description='Prediction APIs')

model = app.model('Prediction parameters', 
				  {'reviewCount': fields.Float(required = True, 
				  							   description="Amount of reviews restaurant recieved", 
    					  				 	   help="Review count cannot be blank"),
				  'averageReviewLength': fields.Float(required = True, 
				  							   description="Average length of reviews restaurant received", 
    					  				 	   help="Average Review Length cannot be blank"),
				  'averageReviewAge': fields.Float(required = True, 
				  							description="Average age of reviews restaurant received", 
    					  				 	help="Average Review Age cannot be blank")})

# classifier = joblib.load('classifier.joblib')
combined_path = dir_path + 'linReg.joblib'
print(combined_path)
linReg = joblib.load(combined_path)

@name_space.route("/")
class MainClass(Resource):

	def options(self):
		response = make_response()
		response.headers.add("Access-Control-Allow-Origin", "*")
		response.headers.add('Access-Control-Allow-Headers', "*")
		response.headers.add('Access-Control-Allow-Methods', "*")
		return response

	@app.expect(model)		
	def post(self):
		try: 
			formData = request.json
			print(formData)
			data = [float(val) for val in formData.values()]
			print(data)
			prediction = linReg.predict(np.array(data).reshape(1,-1))[0]
			if(prediction < 0):
				prediction = 0
			# Edit decimals
			num = "{:.2f}".format(prediction)
			response = jsonify({
				"statusCode": 200,
				"status": "Yelp Prediction made",
				"result": "Yelp Model Predicts: " + str(num) + " star(s)!"
				})
			response.headers.add('Access-Control-Allow-Origin', '*')
			return response
		except Exception as error:
			return jsonify({
				"statusCode": 500,
				"status": "Could not make prediction",
				"error": str(error)
			})


# if __name__=="__main__":
# 	flask_app.run(host='127.0.0.1', port=5000, debug=True)
if __name__=="__main__":
	flask_app.run(host='0.0.0.0', port=5000, debug=True)