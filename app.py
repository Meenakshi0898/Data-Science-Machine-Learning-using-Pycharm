import pandas as pd
from flask import Flask, request, jsonify    #Flask- via app, jsonify-converting rows & columns the file, request-request to consume the URL
import pickle



app = Flask(__name__)

#Linear model exercise
@app.route("/linearpredict", methods=["POST"])
def linearpredict():
    # Load the saved model
    with open("linear_regression_model_01.pkl", "rb") as f:
        model = pickle.load(f)
    # Get the input data as JSON
    data = request.get_json()
    Year = data["year"]  # Expecting input as {"features": [[value1], [value2], ...]}

    # Make prediction
    predictions = model.predict([Year])
    return jsonify({"predictions": predictions.tolist()})

#Logistic model exercise
@app.route("/logisticpredict", methods=["POST"])
def logisticpredict():
    # Load the saved model
    with open("logistic_regression_model_01.pkl", "rb") as f:
        model = pickle.load(f)
    # Get the input data as JSON
    data = request.get_json()
    features1= data["year"]  # Expecting input as {"features": [[value1], [value2], ...]}
    features2= data["house_price"]
    Data=pd.DataFrame(data)
    # Make prediction
    predictions = model.predict(Data)
    return jsonify({"predictions": predictions.tolist()})

if __name__ == "__main__":
    app.run(debug=True)
