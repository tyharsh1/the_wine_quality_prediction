 # 🍷 Wine Quality Prediction App

This is a Streamlit-based web application that predicts wine quality based on physicochemical properties using a trained machine learning model. The app also includes visualizations and an all-drinks information page.

---

## 🚀 Features

- Predict wine quality using 11 input features
- Visualize wine data with interactive charts
- View categorized information on various wines and drinks
- Persist inputs and predictions across sessions
- Simple UI with multi-page Streamlit navigation

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Scikit-learn
- Pandas / NumPy
- Matplotlib / Seaborn

---

## 📁 Folder Structure

wine-quality-prediction/ │ ├── data/ │ └── winequality.csv ├── models/ │ ├── model.pkl │ └── scaler.pkl ├── notebooks/ │ └── (Jupyter notebooks if any) ├── outputs/ │ └── (optional: visualizations or reports) ├── src/ │ └── (utility code and scripts) ├── streamlit_app/ │ ├── Home.py │ ├── Predict.py │ ├── Model_Info.py │ ├── Data_Visualization.py │ └── All_Drinks.py ├── templates/ │ ├── index.html │ └── result.html ├── requirements.txt └── README.md

yaml
Copy code

---

## 🧠 Model Info

- Model used: `GradientBoostingRegressor`
- Data preprocessing includes `StandardScaler`
- Model and scaler are saved in `models/` as `model.pkl` and `scaler.pkl`

---

## 🧪 How to Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/tyharsh1/wine-quality-prediction/tree/master
cd wine-quality-prediction
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Train the model (if not already)
bash
Copy code
python src/train_model.py
5. Run the app
bash
Copy code
cd streamlit_app
streamlit run Home.py
🌍 Deployment (Streamlit Cloud)
Push your code to GitHub

Go to https://share.streamlit.io

Log in with GitHub and select the repo

Set the app entry point to streamlit_app/Home.py

Click Deploy

📊 Features in Development
Upload your own CSV for batch predictions

Add wine brand and company matching from data

Display nearest wines by quality score

🙌 Author
Your Harsh Tyagi
📧 tyagivatsharsh1@gmail.com
🔗 https://github.com/tyharsh1

📜 License
This project is licensed under the MIT License.

---
