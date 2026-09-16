from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

# --------------------------------------------------
# Load dataset
# --------------------------------------------------

DATA_PATH = "food_waste_data.csv"

df = pd.read_csv(DATA_PATH)


# --------------------------------------------------
# Load trained Random Forest model
# --------------------------------------------------

MODEL_PATH = "food_waste_model.pkl"

model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Column definitions
# --------------------------------------------------

categorical_columns = [
    "Type of Food",
    "Event Type",
    "Storage Conditions",
    "Purchase History",
    "Seasonality",
    "Preparation Method",
    "Geographical Location",
    "Pricing"
]

numerical_columns = [
    "Number of Guests",
    "Quantity of Food"
]


# --------------------------------------------------
# Get dropdown options
# --------------------------------------------------

dropdown_options = {}

for column in categorical_columns:
    dropdown_options[column] = sorted(
        df[column].dropna().unique().tolist()
    )


# --------------------------------------------------
# Find most similar row
# --------------------------------------------------

def find_similar_row(user_data):

    # Start with the complete dataset
    candidates = df.copy()

    # --------------------------------------------------
    # Filter using categorical values entered by user
    # --------------------------------------------------

    for column in categorical_columns:

        value = user_data.get(column)

        if value and value != "":

            candidates = candidates[
                candidates[column] == value
            ]

    # If filtering leaves no rows,
    # use the complete dataset
    if len(candidates) == 0:
        candidates = df.copy()

    # --------------------------------------------------
    # Calculate similarity for numerical values
    # --------------------------------------------------

    numerical_input = []

    for column in numerical_columns:

        value = user_data.get(column)

        if value is not None and value != "":

            numerical_input.append(
                (column, float(value))
            )

    # If numerical values were provided,
    # find the closest row
    if numerical_input:

        distances = np.zeros(len(candidates))

        for column, value in numerical_input:

            # Scale the difference so that
            # large-value columns don't dominate
            column_range = (
                df[column].max() -
                df[column].min()
            )

            if column_range == 0:
                column_range = 1

            distances += (
                (candidates[column] - value)
                / column_range
            ) ** 2

        candidates = candidates.copy()

        candidates["similarity_distance"] = distances

        # Smallest distance = most similar
        similar_row = candidates.sort_values(
            "similarity_distance"
        ).iloc[0]

    else:

        # If all numerical fields are blank,
        # use the first matching row
        similar_row = candidates.iloc[0]

    return similar_row


# --------------------------------------------------
# Home page
# --------------------------------------------------

@app.route("/", methods=["GET", "POST"])
def home():

    prediction = None
    filled_values = None
    error = None

    if request.method == "POST":

        try:

            # --------------------------------------------------
            # Collect user input
            # --------------------------------------------------

            user_data = {}

            for column in categorical_columns:

                user_data[column] = request.form.get(
                    column,
                    ""
                )

            for column in numerical_columns:

                value = request.form.get(
                    column,
                    ""
                )

                user_data[column] = value


            # --------------------------------------------------
            # Find most similar dataset row
            # --------------------------------------------------

            similar_row = find_similar_row(
                user_data
            )


            # --------------------------------------------------
            # Fill missing numerical values
            # --------------------------------------------------

            completed_data = {}

            for column in categorical_columns:

                completed_data[column] = user_data[column]


            for column in numerical_columns:

                value = user_data[column]

                if value == "" or value is None:

                    completed_data[column] = float(
                        similar_row[column]
                    )

                else:

                    completed_data[column] = float(value)


            # --------------------------------------------------
            # Create DataFrame for model
            # --------------------------------------------------

            input_df = pd.DataFrame(
                [completed_data]
            )


            # --------------------------------------------------
            # Add engineered feature
            # --------------------------------------------------

            input_df["Food_Per_Guest"] = (
                input_df["Quantity of Food"] /
                input_df["Number of Guests"]
            )


            # --------------------------------------------------
            # Make prediction
            # --------------------------------------------------

            prediction = model.predict(
                input_df
            )[0]

            prediction = max(
                0,
                round(prediction, 2)
            )


            # --------------------------------------------------
            # Store values used by model
            # --------------------------------------------------

            filled_values = completed_data.copy()


        except Exception as e:

            error = str(e)


    return render_template(
        "index.html",
        categorical_columns=categorical_columns,
        numerical_columns=numerical_columns,
        dropdown_options=dropdown_options,
        prediction=prediction,
        filled_values=filled_values,
        error=error
    )


# --------------------------------------------------
# Run application
# --------------------------------------------------

if __name__ == "__main__":

    app.run(
        debug=True
    )