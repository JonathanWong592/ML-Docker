# ML-React-App
It's a template on which we can build a React app and call endpoints to make predictions.
https://github.com/kb22/ML-React-App-Template

### Usage
The complete guide to use this repository: https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33

Frontend: React
Backend: Flask & Flask-RESTPlus

To run:

cd ui
npm install -g serve
npm run build
serve -s build -l 3000

cd service
virtualenv -p Python3 .
source bin/activate
pip install -r requirements.txt
FLASK_APP=app.py flask run


Roadmap (Simplified):
User enters site
User puts in values
User gets prediction


Roadmap (Developer):
Initial Setup
    Create a functional model and save it to joblib, this will be accessed by the flask application
    Change the frontend and backend code to align with your model
User enters site
    Frontend: React
    Backend: Flask & Flask-RESTPlus (Service in Python which has endpoints which we can call from React)
User inputs values used for classifier prediction
    Input values are POSTed to Flask via JSON 
        (Input values are basically the X_train in the model_generator.py file)
    Once fed into the classifier, it will make an output guessing what the correct result is
        (In the IRIS plant case, it will output a number 0,1,2 which represents the actual prediction of 'setosa', 'versicolor', 'virginica', which is what we want to display to the user)
    The result is then sent back to React via JSON
User gets prediction back with classifier's best guess 
    The prediction is displayed after user clicks 'Predict' button by updating the page



MIT License

Copyright (c) 2019 Karan Bhanot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
