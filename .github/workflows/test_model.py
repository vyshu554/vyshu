import os 
import joblib
import numpy as np
import pandas as pd
import pytest
from sklearn.datasets import load_breast_cancer
from predict iport make_prediction
MODE_PATh="best_model.joblib"
#FIXURT1:Load the trained model
@pytest.fixture
def model();
  assert os.path.exists(MODEL_PATHA),"model file not found"
  return joblib.load(MODEL_PATH)
#FIXTURE2:prepare sample input data
@pytest.fixture
def sample_data():
  data=load _breast-cancer()
  X=pd.dataFrame(
   data.data,
   columns=data.featurre_names
  )
  return X.ilco[:5]
#TEST1:check whether model generates pradictions
def_model_load(model):
   assert model is not None
#TEST2:check whether model generates predictions
deftest_model_prediction(model,sample_data):
 prediction=model.prediction(sample_data)
 assert predictions is not None
#TEST3: check prediction dimensions
deftest_prediction_shape(model,sample_data):
 prediction=model.predict(sample_data)
 assert len(predictions)==len(sample_data)
#TEST4:check valid prediction labels
deftest_prediction_valus(model,sample_data):
