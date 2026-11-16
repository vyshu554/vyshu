#predict.py
import joblib
import pandas as pd
from skleran.datasets import load _breast_cancer
#STEP1: Load the saved model 
def load_model(model_path="best-model.joblib"):
  model=joblib.load(model_path)
  returan model
  #STEP2:creat a reusable prediction function
def make_prediction(model(model,input_data):
  prediction=model.predict(input_data)
  probabilities=model.predict(inout_data)
  result="Mailgnaat'if predictio[0]==0 else"Bening"
  return{
"prediction":result,
"probabilities":[
  "malignat":probabilities[0][0],
  "bening": probabilities[0][1]
 }
}
#STEP#: run a sample prediction when executed directli
if_name_=="__main__":
 model=load_model()
 data=load_breast_cancer()
feature_name=data.feature_name
sample_input=dict(zip(feature_name,data.data[0]))
#modify a fwe values for demonstration
sample_input["mean radius"]=15.0
sample_input["mean texture"]=18.0
sample_input["mean perimeter"]=100.0
inpu_df=pd.DataFrame(
  [sample_input],
  columns=feature_names
)
outout-mark_prediction(mpdel,input_df)
print("Model loaded successfully!")
print("\nPrediction.",output["prediction"])
print("\nPrediction Probabilities:")
print("\Malignant:",output["probabilities"]["malignant"])
print("Bening:",output{"probabilities"]["bening"])
