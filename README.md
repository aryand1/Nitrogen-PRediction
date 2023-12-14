# Nitrogen-PRediction



🌾 Nitrogen Prediction Streamlit App
Welcome to the Nitrogen Prediction Streamlit App! This interactive tool leverages a trained model to predict crop nitrogen levels based on user-provided inputs. 🚀

Getting Started
Installation
Clone this repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/nitrogen-prediction-app.git
Install the required dependencies:

bash
Copy code
pip install streamlit pandas scikit-learn joblib
Run the App
Navigate to the project directory and run the Streamlit app:

bash
Copy code
streamlit run app.py
Access the app in your web browser at http://localhost:8501.

Usage
Fill in Input Fields: Enter values for pH, rainfall, temperature, humidity, phosphorus, and potassium.
Choose Crop Type: Select the crop type from the provided options.
Predict Nitrogen: Click the "Predict Nitrogen" button to get the predicted nitrogen value.
Results
The app will display the prediction results, including the selected crop type and the predicted nitrogen value.

Project Structure
app.py: The main Streamlit app script.
best_model.pkl: The pre-trained machine learning model file.
requirements.txt: Dependencies required for the app.
Model Loading
The machine learning model is loaded only once during the initialization for optimal performance.

Crop Types
The app supports prediction for a variety of crops, including rice, maize, chickpea, and more. 🌱

Author
Your Name
📧 Contact: aryand@ksu.edul

License
This project is licensed under the MIT License - see the LICENSE file for details.

On how to run please other readme.pdf file in repo

Acknowledgments
We appreciate the contributors and data sources that contributed to the success of this project.

Happy predicting! 🌾✨

