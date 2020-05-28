# Description
I utilized a ML React/Flask template as shown below with the respective links. I built on top of this and created a linear regression ML model to predict a restaurant's ratings based off of three values: review count, average review length, and average review age. I created the Yelp regression model based off of yelp data provided by Codecademy including business, photo, review, and user data. The model has a score of 83% based off of the features I tested with, more can be viewed in service/model_generator.py. I also dockerized the application into two images, one for the react frontend, and the other for the flask backend. Ways to run the application and the roadmap I took to create the application are below. MIT License from the original template is provided below.

# Links
Template: https://github.com/kb22/ML-React-App-Template
Yelp Model & Data: https://www.codecademy.com/learn/machine-learning/modules/yelp-regression-project
Guide: https://towardsdatascience.com/create-a-complete-machine-learning-web-application-using-react-and-flask-859340bddb33


# To run (V1 - Non Docker):
- cd ui
- npm install -g serve
- npm run build
- serve -s build -l 3000

- cd service
- virtualenv -p Python3 .
- source bin/activate
- pip install -r requirements.txt
- FLASK_APP=app.py flask run

# To run (V2 - Docker):
- docker-compose up


# Roadmap (Simplified):
- User enters site
- User puts in values
- User gets prediction


### Roadmap (Developer):
- Initial Setup
    - Create a functional model and save it to joblib, this will be accessed by the flask application
    - Change the frontend and backend code to align with your model
- User enters site
    - Frontend: React
    - Backend: Flask & Flask-RESTPlus (Service in Python which has endpoints which we can call from React)
- User inputs values used for classifier prediction
    - Input values are POSTed to Flask via JSON 
        - (Input values are basically the X_train in the model_generator.py file)
    - Once fed into the classifier, it will make an output guessing what the correct result is
        - (In the IRIS plant case, it will output a number 0,1,2 which represents the actual prediction of 'setosa', 'versicolor', 'virginica', which is what we want to display to the user)
    - The result is then sent back to React via JSON
- User gets prediction back with classifier's best guess 
    - The prediction is displayed after user clicks 'Predict' button by updating the page

# Extra Model Information
- Visualization of how user input can be inputted into the model and output a value
- X_train: [6.4 3.1 5.5 1.8] & y_train: 2
- We train the classifier based on these values, the values above represent 
- [Sepal length, Sepal Width, Petal Length, Petal Width] & Actual plant name
- So in the user interface which is shown through react, we get the change to input our
- own values and have our classifier model predict what type of iris plant it is depending on our values

- Example, if we put in the exact same values as listed in the first X_train and y_train
- X_train: [6.4 3.1 5.5 1.8] & y_train: 2, we should expect to see a result of 2 which indicates that
- our classifier has predicted that the given values is a "Iris Virginica"
- We know that these types identify to their respective plant names because of documentation online or
- print(list(dataset.target_names)) => # ['setosa', 'versicolor', 'virginica'] === [0, 1, 2]

- print(prediction) # => [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0]
- types = { 0: "Iris Setosa", 1: "Iris Versicolour ", 2: "Iris Virginica"}

# MIT License

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
