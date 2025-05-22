import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load preprocessor and model
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

with open('lasso_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the columns used in the training data
input_columns = [
    "gender", "race_ethnicity", "parental_level_of_education",
    "lunch", "test_preparation_course", "reading_score", "writing_score"
]

@app.route("/", methods=["GET", "POST"])
def predict_datapoint():
    results = None

    if request.method == "POST":
        # Retrieve form data
        form_data = {
            "gender": request.form.get("gender"),
            "race_ethnicity": request.form.get("ethnicity"),
            "parental_level_of_education": request.form.get("parental_level_of_education"),
            "lunch": request.form.get("lunch"),
            "test_preparation_course": request.form.get("test_preparation_course"),
            "reading_score": float(request.form.get("reading_score")),
            "writing_score": float(request.form.get("writing_score"))
        }

        # Convert to DataFrame
        input_df = pd.DataFrame([form_data], columns=input_columns)

        # Preprocess and predict
        transformed_data = preprocessor.transform(input_df)
        predicted_score = model.predict(transformed_data)[0]

        results = f"Predicted Math Score: {predicted_score:.2f}"

    return render_template("form.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
