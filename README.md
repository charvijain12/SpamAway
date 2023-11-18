# SpamAway: Email Spam Filtering System 📧🚫

SpamAway is an API that utilizes a machine learning algorithm to predict whether an email ID is spam or not. When an email ID is passed as a parameter to the API, it responds with a boolean value (True/False) indicating the spam status.

## Overview 🌐

SpamAway aids in identifying spam emails using a machine learning model trained on a dataset of 4601 email messages with associated attributes. The system is built using Python and Flask, leveraging the Random Forest Classifier from scikit-learn for classification.

### Dataset 📊
The dataset used for training the machine learning algorithm can be found at [Spambase Dataset](https://archive.ics.uci.edu/ml/datasets/Spambase/). It comprises 4601 email messages, each associated with a set of attributes.

### Technical Details ⚙️
- Built using Python and Flask framework for the API.
- Machine learning algorithm: Random Forest Classifier from the scikit-learn library.
- Model trained using the Spambase dataset.

## Usage 🚀

### Installation 🛠️
To use this project:
1. Install Python on your system.
2. Clone this repository and navigate to the project directory in your terminal.
3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API 🏃‍♂️
Start the API server by running:

```bash
python app.py
```

The API server will be available at http://localhost:5000/. Send a GET request to http://localhost:5000/predict with the email ID as a parameter in the query string. For example:

```http
http://localhost:5000/predict?email_id=hello@world.com
```

The API will respond with a boolean value indicating whether the email ID is classified as spam or not.

## Contributing 🤝

Contributions are welcome! Feel free to submit pull requests or open issues if you have suggestions or feedback.

## License 📜

This project is licensed under the `MIT License`. See the LICENSE file for more details.
