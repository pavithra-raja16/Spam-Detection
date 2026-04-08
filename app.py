from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model, cv = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    data = cv.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        result = "Spam"
    else:
        result = "Not Spam"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)