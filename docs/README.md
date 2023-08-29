# Project Title: Diabetes Prediction Web App  
   
This project is a web application that uses Flask and a pre-trained machine learning model to predict the likelihood of diabetes based on user input.  
   
## Dependencies  
   
- Flask  
- joblib  
- predict.pred module  
   
## How to use  
   
1. Ensure you have the required dependencies installed. If not, install Flask and joblib using pip:  
  
   ```  
   pip install Flask joblib  
   ```  
   
2. Make sure the pre-trained model file (e.g., `diabetic_80.pkl`) is available in the project directory.  
   
3. Run the web application by executing the following command:  
  
   ```  
   python app.py  
   ```  
   
4. Open your web browser and navigate to `http://localhost:5000/` or `http://127.0.0.1:5000/` to access the web app.  
   
## Functionality  
   
The web application performs the following tasks:  
   
1. Displays a form to collect user input for various health parameters.  
2. Sends the user input to the server for processing and prediction.  
3. Calls the `f_prediction` function from the `predict.pred` module to make predictions using the pre-trained model.  
4. Displays the prediction result on the `predict.html` template.  
   
## Code Structure  
   
- `app`: The Flask app instance.  
- `@app.route('/')`, `@app.route('/home')`, `@app.route('/contact')`: Route decorators for the base, home, and contact pages.  
- `@app.route('/predict', methods=['POST'])`: Route decorator for the predict endpoint that handles form submissions.  
- `predict()`: Function that processes the form data, calls the prediction function, and returns the prediction result.  
- `if __name__ == '__main__': app.run(debug=True)`: Starts the Flask app in debug mode when the script is executed directly.