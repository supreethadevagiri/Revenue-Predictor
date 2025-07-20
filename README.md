# 📦 Revenue Prediction Web App

This is a Flask-based web application that predicts **total revenue generated** based on user inputs related to logistics and business context. It uses a trained machine learning model and a one-hot encoder to process form data and return revenue estimates.

---

## 🚀 Features

- User-friendly HTML form for inputs (`form.html`)
- Dynamic revenue prediction using a trained ML model (`revenue_model.pkl`)
- Preprocessing of categorical inputs using a pre-trained OneHotEncoder (`encoder.pkl`)
- Styled HTML result page (`return.html`)

---

## 🛠 Technologies Used

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- HTML + CSS
- Joblib

---

## 📁 File Structure

```
.
├── app.py                    # Flask backend app
├── form.html                # Input form (served at '/')
├── return.html              # Output page showing prediction
├── revenue_model.pkl        # Trained regression model
├── encoder.pkl              # Trained OneHotEncoder for categorical features
└── static/
    ├── form_image.png       # Background for form page
    └── logistics_background.png  # Background for result page
```

---

## 📋 Input Fields

Users must fill the following fields in the form:

- `Customer` (text)
- `Location` (text)
- `Business Type` (text)
- `Order Count` (integer)
- `Number of Pieces` (integer)
- `Day of Week` (0 = Monday, 6 = Sunday)

---

## 📦 How to Run Locally

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/revenue-prediction-app.git
   cd revenue-prediction-app
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure the following files are present:
   - `revenue_model.pkl`
   - `encoder.pkl`

4. Run the app:
   ```bash
   python app.py
   ```

5. Open in browser:
   ```
   http://127.0.0.1:5000/
   ```

---

## 📈 Example

Submit the following sample input:
```
Customer: ACME Corp
Location: Berlin
Business Type: Retail
Order Count: 10
Number of Pieces: 500
Day of Week: 2
```

And get a predicted revenue like:
```
The predicted value is $12,348.55
```

---

## 🧠 Notes

- This app assumes the encoder and model were trained on the same categorical features: `['Customer', 'Location', 'BusinessType']`.
- The numeric inputs are used directly without scaling.

---

## 🔐 License

This project is released under the [MIT License](LICENSE).
