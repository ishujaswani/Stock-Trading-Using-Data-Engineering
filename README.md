# Stock Trading Using Data Engineering

![GitHub License](https://img.shields.io/github/license/ishujaswani/Stock-Trading-Using-Data-Engineering)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)

## 📌 Overview
This project is a **large-scale stock market data processing and visualization application** designed for traders. It leverages **Apache Spark** for distributed data processing, **Flask** for the web interface, and **Plotly** for interactive visualizations. The system provides access to **6,875 stocks**, enabling traders to perform **algorithmic trading** and **technical analysis**.

## 🚀 Features and Functionality

### 📈 Stock Data Processing
- Utilizes **Apache Spark** to process large volumes of stock data efficiently.
- Reads and integrates stock data from multiple CSV files.
- Cleans and prepares data for further analysis.

### 📊 Data Visualization
- Uses **Plotly** for interactive stock market visualizations.
- Provides traders with historical data analysis and market trends.

### 🖥️ Web Application
- Built with **Flask** for an intuitive web interface.
- Displays stock data in **charts and tables**.
- Allows users to filter and analyze stocks dynamically.

### ⚡ Performance Optimization
- Spark configurations optimized for large-scale processing.
- Supports real-time data integration for improved accuracy.

## 📂 Technology Stack
- **Programming Language:** Python
- **Libraries:** Flask, Pandas, NumPy, Plotly, PySpark
- **Data Processing:** Apache Spark
- **Visualization:** Plotly, HTML/CSS (for frontend styling)

## ✅ Prerequisites
Ensure you have the following installed:
```sh
pip install flask pandas numpy plotly pyspark

## 🔧 Installation Instructions

### Clone the repository:
```sh
git clone https://github.com/ishujaswani/Stock-Trading-Using-Data-Engineering.git
cd Stock-Trading-Using-Data-Engineering
```

### Create a virtual environment (recommended):
```sh
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Install dependencies:
```sh
pip install -r requirements.txt
```

## 📖 Usage Guide

### 🗂 Data Preparation
- Ensure stock data is stored in **CSV files** inside the appropriate directory.
- The system will automatically read and process these files using **Apache Spark**.

### ⚙️ Running the Application
- Start the Flask web server:
  ```sh
  python app.py
  ```
- The application will be accessible at **http://127.0.0.1:5000**.

### 📊 Output Interpretation
- View **stock price trends** using interactive **Plotly charts**.
- Analyze and filter stock data dynamically within the web interface.

## 🤝 Contributing Guidelines

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit changes with descriptive messages.
4. Push to your forked repository.
5. Create a pull request to merge into the `main` branch.

## 📜 License Information

This project is licensed under the **Creative Commons Zero v1.0 Universal License**. See the LICENSE file for details.

## 📬 Contact/Support Information

For any questions or support, please contact **ij2243@columbia.edu**.


