import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.externals import joblib
from matplotlib import pyplot as plt
import numpy as np
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))

# Load Yelp Data
businesses = pd.read_json(dir_path + '/yelp_data/yelp_business.json',lines=True)
reviews = pd.read_json(dir_path + '/yelp_data/yelp_review.json',lines=True)
users = pd.read_json(dir_path + '/yelp_data/yelp_user.json',lines=True)
checkins = pd.read_json(dir_path + '/yelp_data/yelp_checkin.json',lines=True)
tips = pd.read_json(dir_path + '/yelp_data/yelp_tip.json',lines=True)
photos = pd.read_json(dir_path + '/yelp_data/yelp_photo.json',lines=True)

# Merge data
df = pd.merge(businesses, reviews, how='left', on='business_id')
df = pd.merge(df, users, how='left', on='business_id')
df = pd.merge(df, checkins, how='left', on='business_id')
df = pd.merge(df, tips, how='left', on='business_id')
df = pd.merge(df, photos, how='left', on='business_id')

# Clean Data
features_to_remove = ['address','attributes','business_id','categories','city','hours','is_open','latitude','longitude','name','neighborhood','postal_code','state','time']
df.drop(labels=features_to_remove, axis=1, inplace=True)
# print(df.isna().any())
df.fillna({'weekday_checkins':0,
           'weekend_checkins':0,
           'average_tip_length':0,
           'number_tips':0,
           'average_caption_length':0,
           'number_pics':0},
          inplace=True)
# print(df.isna().any())


features = df[['review_count','average_review_length','average_review_age']]
ratings = df['stars']


# Split Data into Training & Testing Sets
X_train, X_test, y_train, y_test = train_test_split(features, ratings, test_size = 0.2, random_state = 1)


# Creating & Training The Model w/ Linear Regression
model = LinearRegression()
model.fit(X_train,y_train)
prediction = model.predict(X_test)
# print(X_train, y_train)
# print(model.score(X_train,y_train))
# print(model.score(X_test,y_test))


# Test data array
# arr = np.array([100, 10, 254.741])
# print(arr)


# y_predicted = model.predict(arr.reshape(1, -1))
# print(y_predicted)

# Save the model to disk
joblib.dump(model, 'linReg.joblib')