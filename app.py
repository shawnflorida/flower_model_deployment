from flask import Flask, request, jsonify
import joblib
import numpy as np

model = joblib.load("model.joblib")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Credit Scoring API from Easycall!"})

# Flower class names
flower_names = np.array(["setosa", "versicolor", "virginica"])

@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict the class of a flower based on input features.
    """
    try:
        data = request.get_json()
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        class_name = flower_names[prediction][0]
        return jsonify({"prediction": class_name, "flower_names": flower_names.tolist()})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
