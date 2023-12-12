from flask import Flask, render_template, request
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load the model
model_file = "A:/New folder/banglore_home_prices_model.pickle"
with open(model_file, 'rb') as f:
    model = pickle.load(f)

# Load column names
with open('A:/New folder/columns.json', 'r') as f:
    columns = json.load(f)['data_columns']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            location = request.form['location']
            total_sqft = float(request.form['total_sqft'])
            bath = float(request.form['bath'])
            bhk = float(request.form['bhk'])

            # Convert location to one-hot encoding
            loc_index = columns.index(location.lower())
            x = np.zeros(len(columns))
            x[0] = total_sqft
            x[1] = bath
            x[2] = bhk
            if loc_index >= 0:
                x[loc_index] = 1

            # Make prediction
            prediction = model.predict([x])[0]

            return render_template('index.html', prediction_text=f'Predicted Price: {round(prediction, 2)} Lakhs')
        except Exception as e:
            print(e)
            return render_template('index.html', prediction_text='Error in prediction')

if __name__ == '__main__':
    app.run(debug=True)
