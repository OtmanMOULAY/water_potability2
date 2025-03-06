import numpy as np
import pandas as pd
import pickle
import json

from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score


def load_data(file_path:str)->pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error loading data from {file_path}:{e}")
#test_data = pd.read_csv("./data/processed/test_processed.csv")
def prepare_data(data:pd.DataFrame)->tuple[pd.DataFrame,pd.Series]:
    try:
        x= data.drop(columns=["Potability"],axis  = 1)
        y= data["Potability"]
        return x, y
    except Exception as e:
        raise Exception(f"Error preparing data :{e}")


#x_test = test_data.iloc[:,0:-1].values
#y_test = test_data.iloc[:,-1].values

def load_model(file_path:str):
    try:
        with open(file_path, 'rb') as file:
            model  = pickle.load(file)
        return model
    except Exception as e:
        raise Exception(f"Error loading model from {file_path}:{e}")


# model = pickle.load(open("model.pkl", "rb"))
def model_eval(model,x_test:pd.DataFrame,y_test:pd.Series)->dict:
    try:
        y_pred = model.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)

        precision = precision_score(y_test, y_pred)

        recall = recall_score(y_test, y_pred)

        f1 = f1_score(y_test, y_pred)

        metrics = {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1
        }
        return metrics
    except Exception as e:
        raise Exception(f"Error evaluating model :{e}")

  
def save_metrics(metrics:dict,file_path:str)->None:
    try:
        with open(file_path, "w") as file:
            json.dump(metrics, file, indent=4)
    except Exception as e:
        raise Exception(f"Error saving metrics to {file_path}:{e}")
def main():
    try : 
        file_path = "./model.pkl"
        metrics_path = "metrics.json"
        test_data_path = "./data/processed/test_processed.csv"
        test_data = load_data(test_data_path)
        x_test, y_test = prepare_data(test_data)
        model = load_model(file_path)
        metrics = model_eval(model, x_test, y_test)
        save_metrics(metrics, metrics_path)
    except Exception as e :
        raise Exception(f"error occured: {e}")
    
if __name__ == "__main__":
    main()

