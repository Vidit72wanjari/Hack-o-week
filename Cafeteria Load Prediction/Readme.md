# Cafeteria Load Prediction Dashboard

## Overview

Cafeteria Load Prediction Dashboard is a machine learning–powered web application designed to forecast cafeteria crowd levels over time. The system predicts the number of students expected in the cafeteria using historical data and visualizes the results through an interactive dashboard.

The application combines a Python backend for machine learning predictions with a React frontend for real-time visualization. It helps analyze peak cafeteria usage periods and enables better planning of seating, food preparation, and resource allocation.

This project demonstrates how predictive analytics can be applied to crowd management and campus resource optimization.

---
![](<Screenshot 2026-03-06 215343.png>)


## Key Features

### 1. Cafeteria Crowd Prediction

The system predicts the expected number of students in the cafeteria at different time intervals using a trained machine learning model.

Input features used for prediction may include:

* Time of day
* Historical cafeteria usage
* Environmental conditions (optional)

Output:

Predicted cafeteria occupancy.

---

### 2. Machine Learning Model

A regression-based machine learning model is trained using historical cafeteria data stored in a CSV dataset.

The model learns patterns such as:

* Lunch rush hours
* Low traffic periods
* Periodic crowd fluctuations

After training, the model generates predictions that are sent to the frontend dashboard.

---

### 3. Interactive Visualization Dashboard

The React-based dashboard visualizes predictions using a line chart.

The chart displays:

* Time on the x-axis
* Predicted number of students on the y-axis

This allows users to clearly see cafeteria load changes throughout the day.

---

### 4. Real-Time Graph Updates

The frontend periodically fetches prediction data from the backend server and updates the graph dynamically. This simulates real-time monitoring of cafeteria crowd levels.

---

### 5. Prediction Indicator

Below the graph, the application displays the current predicted cafeteria load, highlighting the expected number of students at the latest timestamp.

---

## Technology Stack

Frontend

* React.js
* Chart.js
* JavaScript
* HTML
* CSS

Backend

* Python
* Flask

Machine Learning

* Scikit-Learn
* Pandas
* NumPy

Data Storage

* CSV dataset (`cafeteria_data.csv`)

---

## Project Structure

```
Cafeteria Load Prediction
│
├── backend
│   ├── server.py
│   ├── model.py
│   └── cafeteria_data.csv
│
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── App.css
│   │   └── index.js
│   │
│   ├── public
│   └── package.json
│
└── README.md
```

---

## How the System Works

1. Historical cafeteria usage data is stored in a dataset.

2. The machine learning model (`model.py`) trains on this dataset to learn patterns in cafeteria crowd behavior.

3. The backend server (`server.py`) loads the trained model and exposes an API endpoint.

4. The React frontend requests prediction data from the backend.

5. The dashboard visualizes the predictions using a line chart.

6. The latest predicted cafeteria load is displayed below the graph.

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/cafeteria-load-prediction.git
```

Navigate into the project folder:

```
cd cafeteria-load-prediction
```

---

## Running the Backend

Navigate to the backend directory:

```
cd backend
```

Install dependencies:

```
pip install flask pandas scikit-learn numpy
```

Start the server:

```
python server.py
```

The backend API will run on:

```
http://localhost:5000
```

---

## Running the Frontend

Open a new terminal and navigate to the frontend directory:

```
cd frontend
```

Install dependencies:

```
npm install
```

Start the React application:

```
npm start
```

The dashboard will open automatically in your browser:

```
http://localhost:3000
```

---

## Example Use Cases

This system can be used for:

* Campus cafeteria crowd prediction
* Resource planning for food services
* Queue management
* Smart campus infrastructure
* Data visualization projects

---

## Future Improvements

Possible enhancements include:

* Weather-based prediction models
* Deep learning time-series forecasting
* Real-time sensor integration
* Mobile dashboard interface
* AI-based queue prediction

---
