# Machine Learning — Web Application

A web application built with Flask that helps understand machine learning concepts in a simple way and shows real-world examples of how they are used. It includes supervised learning models for regression and classification that can be used to make real predictions.

---

## Description

This project was developed as part of the Machine Learning course at Universidad de Cundinamarca.

The goal is to combine theory with practice. It not only explains concepts, but also shows how they work within the application itself. It includes real examples from different industries, concept explanations for each algorithm, and functional models that can be used to make predictions from real input data.

The backend is built with Python and Flask, while the frontend uses HTML, CSS, and Bootstrap — no external JavaScript frameworks required.

---

## Features

- Simple and easy-to-use main menu
- **4 real-world machine learning use cases:**
  - Fraud detection (PayPal)
  - Route optimization (Waze)
  - Heart disease risk prediction (Healthcare)
  - Content recommendation (Instagram)
- **Supervised Machine Learning module** with 3 algorithms:
  - **Linear Regression**
    - Basic concept explanations (variables, regression line, slope and intercept)
    - Practical exercise — body weight prediction using a real obesity dataset
    - Interactive form with results and Actual vs Predicted scatter plot
  - **Logistic Regression**
    - Basic concept explanations
    - Application — diabetes prediction using a real clinical dataset
    - Confusion matrix, ROC curve with real data, and full performance metrics
  - **Ridge Classifier** (assigned model)
    - Basic concept explanations (L2 regularization, decision boundary, advantages and limitations)
    - Application — student dropout prediction using a real academic dataset
    - Confusion matrix, ROC curve with real data, and full performance metrics
- Consistent minimalist design across all pages
- Fully responsive layout

---

## Technologies Used

| Layer | Technology |
|---|---|
| Backend | Python 3, Flask |
| Machine Learning | scikit-learn, pandas, NumPy |
| Frontend | HTML5, CSS3, Bootstrap 5 |
| Charts | Chart.js 4 |
| Typography | IBM Plex Mono, IBM Plex Sans |
| Datasets | ObesityDataSet_raw_and_data_sinthetic.csv · diabetes.csv · Predict_students_dropout.csv |

---

## Installation

### Requirements

- Python 3.8 or higher
- pip

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/bcuitiva/MachineLearnig.git
```

**2. Go to the project folder**

```bash
cd MachineLearnig
```

**3. Create and activate a virtual environment**

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

**4. Install dependencies**

```bash
pip install flask pandas scikit-learn numpy
```

**5. Make sure all datasets are in the project root**

```
MachineLearnig/
├── ObesityDataSet_raw_and_data_sinthetic.csv
├── diabetes.csv
└── Predict_students_dropout.csv
```

**6. Run the application**

```bash
python app.py
```

**7. Open in your browser**

```
http://127.0.0.1:5000
```

---

## Usage

Open the application in your browser and navigate through the available sections.

**To test the Linear Regression model:**
1. Go to Supervised Machine Learning → Linear Regression → Practical Exercise
2. Fill out the form with personal and lifestyle data
3. Run the prediction
4. View the estimated weight and its position on the scatter plot

**To test the Logistic Regression model:**
1. Go to Supervised Machine Learning → Logistic Regression → Application
2. Enter the patient's clinical data
3. Run the prediction
4. View the diabetes risk result, probability, and model metrics

**To test the Ridge Classifier model:**
1. Go to Supervised Machine Learning → Ridge Classifier → Application
2. Enter the student's academic data (age, grades, units approved)
3. Run the prediction
4. View the result — Graduate or Dropout — along with the confusion matrix and ROC curve

---

## Project Structure

```
MachineLearnig/
│
├── app.py                                       # Flask routes
├── LinearRegression.py                          # Weight prediction model
├── LogisticRegression.py                        # Diabetes prediction model
├── RidgeClassifierModel.py                      # Student dropout model
├── ObesityDataSet_raw_and_data_sinthetic.csv    # Obesity dataset
├── diabetes.csv                                 # Diabetes dataset
├── Predict_students_dropout.csv                 # Student dropout dataset
│
└── templates/
    ├── start.html                               # Home menu
    │
    ├── useCases.html                            # Use cases menu
    ├── UseCase_FinancialSecurity.html           # PayPal — fraud detection
    ├── UseCase_Mendez.html                      # Waze — route optimization
    ├── UseCase_Cuitiva.html                     # Healthcare — cardiac risk
    ├── UseCase_Instagram.html                   # Instagram — recommendation
    │
    ├── supervisedML.html                        # Supervised ML menu
    │
    ├── linearRegressionMenu.html                # Linear regression menu
    ├── linearRegressionConcepts.html            # Basic concepts
    ├── linearRegressionGrades.html              # Weight prediction form
    │
    ├── logisticRegressionMenu.html              # Logistic regression menu
    ├── logisticRegressionConcepts.html          # Basic concepts
    ├── logisticRegressionApp.html               # Diabetes prediction form
    │
    ├── assignedClassificationMenu.html          # Ridge Classifier menu
    ├── RCConcepts.html                          # Basic concepts
    └── RCApp.html                               # Dropout prediction form
```

---

## Datasets

### Obesity Dataset
Used for the **Linear Regression** model.

- **Source:** Survey data from Mexico, Peru, and Colombia (partially synthetic via SMOTE)
- **Records:** 2,111
- **Target variable:** Weight in kg (range: 39 – 173 kg)
- **Features:** 15 variables including age, height, eating habits, and physical activity

### Diabetes Dataset
Used for the **Logistic Regression** model.

- **Source:** Pima Indians Diabetes Database (National Institute of Diabetes and Digestive and Kidney Diseases)
- **Records:** 768 patients (female, age ≥ 21)
- **Target variable:** Outcome — 0 = No diabetes · 1 = Diabetes
- **Class distribution:** 500 negative (65.1%) · 268 positive (34.9%)
- **Features:** 8 clinical variables including glucose, BMI, insulin, blood pressure, and age

### Student Dropout Dataset
Used for the **Ridge Classifier** model.

- **Source:** Academic records from a Portuguese higher education institution
- **Records:** 4,424 students
- **Original classes:** Dropout, Enrolled, Graduate (converted to binary)
- **Features:** 5 variables — age at enrollment, units approved and grades for semesters 1 and 2

---

## Model Performance

### Linear Regression — Weight Prediction

| Metric | Value |
|---|---|
| R² Score | 0.579 |
| MAE | 13.82 kg |
| RMSE | 17.23 kg |
| Training set | 1,688 records (80%) |
| Test set | 423 records (20%) |

### Logistic Regression — Diabetes Prediction

| Metric | Value |
|---|---|
| Accuracy | 75.3% |
| Precision | 64.9% |
| Recall | 67.3% |
| F1-Score | 66.1% |
| AUC | 0.815 |
| Training set | 614 records (80%) |
| Test set | 154 records (20%) |

### Ridge Classifier — Student Dropout Prediction

| Metric | Value |
|---|---|
| Accuracy | 79.5% |
| Precision | 78.6% |
| Recall | 93.7% |
| F1-Score | 85.5% |
| AUC | 0.859 |
| Training set | 3,539 records (80%) |
| Test set | 885 records (20%) |

---

## Authors

**Elkin Yamith Almonacid López**
**Brayan David Cuitiva Umbarila**
**Brayan Yair Mendez Rodriguez**

Universidad de Cundinamarca — Systems and Computer Engineering
Machine Learning · 2026
