from flask import Flask, request, render_template
import joblib
import pandas as pd

app = Flask(__name__)

# Load trained model and encoder
model = joblib.load("revenue_model.pkl")
ohe = joblib.load("encoder.pkl")

# Define expected categorical and numerical features
categorical_features = ['Customer', 'Location', 'BusinessType']
numerical_features = ['OrderCount', 'NumberOfPieces', 'DayOfWeek']



@app.route('/')
def index():
    return render_template('form.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        #data = request.get_json()
        data = {x: request.form[x] for x in ['Customer', 'Location', 'BusinessType', 'OrderCount', 'NumberOfPieces', 'DayOfWeek']}


        # Ensure required fields are present
        for field in categorical_features + numerical_features:
            if field not in data:
                return render_template('return.html', predicted_revenue=f"Missing field: {field}"), 400

        # Create dataframe for input
        cat_values = [[data[feature] for feature in categorical_features]]
        num_values = [[data[feature] for feature in numerical_features]]

        # Encode categorical data
        cat_encoded = ohe.transform(cat_values)
        cat_encoded_df = pd.DataFrame(cat_encoded, columns=ohe.get_feature_names_out(categorical_features))
        num_df = pd.DataFrame(num_values, columns=numerical_features)

        # Combine features
        input_df = pd.concat([num_df, cat_encoded_df], axis=1)

        # Predict
        prediction = model.predict(input_df)[0]
        return render_template('return.html', predicted_revenue=f'{round(prediction, 2)}')

    except Exception as e:
        return render_template('return.html', predicted_revenue=f"❌ Error: {str(e)}"), 500

if __name__ == '__main__':
    app.run(debug=True)
