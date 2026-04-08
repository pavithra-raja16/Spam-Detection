Spam Detection System

A simple AI/ML-based web application that detects whether a given message is **spam** or **not spam** using Natural Language Processing (NLP) and Machine Learning.

Features

* Detects spam messages instantly
* Simple and user-friendly web interface
* Built using Flask (Python)
* Uses Machine Learning (Naive Bayes)
* Real-time prediction

Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* HTML & CSS
* NLP (CountVectorizer)


Project Structure

Spam_Detection/
│
├── app.py
├── train_model.py
├── model.pkl
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
└── README.md

How It Works

1. The system is trained using sample messages labeled as spam or not spam
2. Input message is converted into numerical format using CountVectorizer
3. A Naive Bayes model analyzes the message
4. The system predicts:

   * **spam**
   * **not spam**


Installation & Setup

 Step 1: Clone the repository

git clone https://github.com/pavithra-raja16/Spam-Detection
cd spam-detection

Step 2: Install dependencies

pip install flask pandas scikit-learn

Step 3: Train the model

python train_model.py

Step 4: Run the application

python app.py

Step 5: Open in browser

http://127.0.0.1:5000/

Usage

* Enter a message in the input box
* Click **Validate**
* The system will display:

  * `spam`
  * `not spam`


Output Example

| Input Message | Output   |
| ------------- | -------- |
| Win money now | spam     |
| Hello friend  | not spam |

Future Improvements

* Use a larger dataset
* Improve accuracy with advanced models
* Add user authentication
* Deploy online

Author

Pavithra

This project is created for educational purposes and demonstrates basic AI/ML concepts.
