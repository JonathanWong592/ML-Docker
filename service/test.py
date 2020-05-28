from sklearn.externals import joblib
import numpy as np
import os


dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("service", "")
combined_path = dir_path + 'linReg.joblib'
# print(combined_path)
linReg = joblib.load(combined_path)

formData = {
    "reviewCount": 1,
    "averageReviewLength": 1,
    "averageReviewAge": 1
}
print(formData)
data = [val for val in formData.values()]
print(data)
nump = np.array(data).reshape(1,-1)
print(nump)
prediction = linReg.predict(nump)
print(prediction)

