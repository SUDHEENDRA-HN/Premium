import joblib
rf=joblib.load('predictions.joblib')
def prediction(age,sex,bmi,children,smoker,region):
  x=[[age,sex,bmi,children,smoker,region]]
  predictions=rf.predict(x)
  return predictions
