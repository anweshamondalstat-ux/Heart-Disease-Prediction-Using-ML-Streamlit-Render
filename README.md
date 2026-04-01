# ❤️ Heart Disease Prediction Using Machine Learning

_Predicting heart disease risk using clinical health indicators with end-to-end Machine Learning, Streamlit deployment, and Render cloud hosting._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#problem-statement">Problem Statement</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-preprocessing">Data Preprocessing</a>
- <a href="#exploratory-data-analysis-eda">Exploratory Data Analysis (EDA)</a>
- <a href="#feature-engineering--encoding">Feature Engineering & Encoding</a>
- <a href="#model-building">Model Building</a>
- <a href="#model-performance">Model Performance</a>
- <a href="#streamlit-application">Streamlit Application</a>
- <a href="#deployment">Deployment</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#future-improvements">Future Improvements</a>
- <a href="#author--contact">Author & Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project predicts the likelihood of **heart disease** using patient clinical data and multiple machine learning classification algorithms.

The complete workflow covers:
- Data collection from Kaggle
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering and encoding
- Model training and evaluation
- Streamlit app development
- Cloud deployment on Render

This is an **end-to-end healthcare ML project** designed for **portfolio, resume, GitHub, and interview showcase**.

---

<h2><a class="anchor" id="problem-statement"></a>Problem Statement</h2>

Heart disease is one of the leading causes of death worldwide. Early prediction using clinical patient data can support faster diagnosis and preventive healthcare decisions.

This project aims to:
- Predict whether a patient is at risk of heart disease
- Compare multiple ML classification models
- Select the best-performing model
- Build a deployable real-world healthcare app

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- **Source:** Kaggle
- **Domain:** Healthcare / Clinical Data
- **Problem Type:** Binary Classification

### 📌 Features
- Age
- Sex
- ChestPainType
- RestingBP
- Cholesterol
- FastingBS
- RestingECG
- MaxHR
- ExerciseAngina
- Oldpeak
- ST_Slope
- HeartDisease (Target)

### 🎯 Target Variable
- `0` → No Heart Disease
- `1` → Heart Disease

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- **Python**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**
- **Scikit-learn**
- **Jupyter Notebook**
- **VS Code**
- **Streamlit**
- **Pickle**
- **Render**
- **GitHub**

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```bash
heart-disease-prediction-ml/
│
├── app.py
├── README.md
├── requirements.txt
├── heart.csv
│
├── models/
│   ├── logistic_regression.pkl
│   ├── svm.pkl
│   ├── decision_tree.pkl
│   └── random_forest.pkl
│
├── notebooks/
│   └── heart_disease_prediction.ipynb
│
├── images/
│   ├── app_ui.png
│   ├── prediction_result.png
│   ├── eda_chart.png
│   └── heatmap.png
```

---

<h2><a class="anchor" id="data-preprocessing"></a>Data Preprocessing</h2>

The dataset was cleaned and prepared carefully before model training.

### ✅ Steps Performed
- Loaded dataset in Jupyter Notebook
- Checked dataset info using `df.info()`
- Reviewed summary statistics using `df.describe()`
- Detected invalid values:
  - `RestingBP = 0`
  - `Cholesterol = 0`
- Replaced:
  - **Cholesterol 0 values → sex-wise median**
  - **RestingBP 0 values → mean**
- Checked for:
  - Null values ✅
  - Duplicate rows ✅
- No missing or duplicate values found

This improved data quality and prevented unrealistic medical records from affecting the model.

---

<h2><a class="anchor" id="exploratory-data-analysis-eda"></a>Exploratory Data Analysis (EDA)</h2>

EDA was performed to understand relationships between patient features and heart disease risk.

### 📊 Visualizations Included
- Sex distribution pie chart
- Sex vs heart disease
- Age group distribution
- Age group vs heart disease
- Blood pressure groups vs disease
- Chest pain type vs disease
- Correlation heatmap

```md
![EDA](https://github.com/user-attachments/assets/583c7869-1df7-47fc-a233-a62a06ea2729)

![Correlation Heatmap](https://github.com/user-attachments/assets/69a7be1b-5a06-4987-aae0-217fc54572d0)

```

---

<h2><a class="anchor" id="feature-engineering--encoding"></a>Feature Engineering & Encoding</h2>

### 🔢 Encoding Mapping
- **Sex**: M = 0, F = 1
- **ChestPainType**:
  - ATA = 0
  - NAP = 1
  - ASY = 2
  - TA = 3
- **RestingECG**:
  - Normal = 0
  - ST = 1
  - LVH = 2
- **ExerciseAngina**:
  - N = 0
  - Y = 1
- **ST_Slope**:
  - Up = 0
  - Flat = 1
  - Down = 2

All categorical variables were converted into integer format.

---

<h2><a class="anchor" id="model-building"></a>Model Building</h2>

### 🤖 Models Trained
- Logistic Regression
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

The dataset was split into training and testing sets for fair evaluation.

---

<h2><a class="anchor" id="model-performance"></a>Model Performance</h2>

| Model | Accuracy |
|---|---:|
| Logistic Regression | 85.86% |
| SVM | 83.16% |
| Decision Tree | 80.97% |
| Random Forest | **86.41% ✅** |

### 🏆 Best Model
**Random Forest Classifier** achieved the highest accuracy.

```md
![Model Performance](images/model_performance.png)
```

---

<h2><a class="anchor" id="streamlit-application"></a>Streamlit Application</h2>

A user-friendly **Streamlit web application** was built with two tabs.

### 🔍 Prediction Tab
- User inputs patient details
- Model predicts heart disease risk instantly

### 📈 Model Performance Tab
- Shows accuracy comparison of all models
- Highlights best model

```md
!<img width="1184" height="662" alt="Streamlit App" src="https://github.com/user-attachments/assets/97fa52a2-5e96-4a25-b938-7090f100b657" />

!<img width="1173" height="674" alt="Streamlit result" src="https://github.com/user-attachments/assets/405e505a-0ad4-4464-b00a-a6c683b82557" />

```

---

<h2><a class="anchor" id="deployment"></a>Deployment</h2>

The application is deployed on **Render**.

### 🌐 Live Demo
👉 (https://heart-disease-prediction-using-machine-ikso.onrender.com)

This demonstrates:
- production deployment
- real-time accessibility
- cloud hosting experience

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:
```bash
git clone https://github.com/yourusername/heart-disease-prediction-ml.git
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run Streamlit app:
```bash
streamlit run app.py
```

---

<h2><a class="anchor" id="future-improvements"></a>Future Improvements</h2>

- Hyperparameter tuning
- Cross-validation
- ROC-AUC evaluation
- SHAP explainability
- Probability confidence score
- Better UI/UX
- Docker deployment

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Anwesha Mondal**  
📧 Email: anweshamondal.stat@gmail.com 

---
