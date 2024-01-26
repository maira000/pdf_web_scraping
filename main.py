import logging
from flask import Flask, request, jsonify, send_file
import sqlite3
import pandas as pd

app = Flask(__name__)

# Configure logging settings
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Connect to SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create combined_data table if not exists
try:
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS combined_data (
            id INTEGER PRIMARY KEY,
            Name TEXT,
            Age INTEGER,
            Occupation TEXT,
            Date TEXT,
            Title TEXT
        )
    ''')
    conn.commit()
except Exception as e:
    logging.error(f"Error creating database table: {e}")

# API endpoint to receive data and store in the database
@app.route('/store_data', methods=['POST'])
def store_data():
    try:
        data = request.json
        cursor.execute('''
            INSERT INTO combined_data (Name, Age, Occupation, Date, Title)
            VALUES (?, ?, ?, ?, ?)
        ''', (data['Name'], data['Age'], data['Occupation'], data['Date'], data['Title']))
        conn.commit()
        return jsonify({"message": "Data stored successfully"}), 200
    except Exception as e:
        logging.error(f"Error storing data: {e}")
        return jsonify({"error": str(e)}), 500

# Download button for Excel file
@app.route('/download_excel')
def download_excel():
    try:
        df = pd.read_sql_query('SELECT * FROM combined_data', conn)
        excel_file_path = 'data.xlsx'
        df.to_excel(excel_file_path, index=False)
        return send_file(excel_file_path, as_attachment=True), 200
    except Exception as e:
        logging.error(f"Error downloading Excel file: {e}")
        return jsonify({"error": str(e)}), 500

# Root URL route
@app.route('/')
def welcome():
    return 'Welcome to the API for PDF and Web Data Scraping'

if __name__ == '__main__':
    app.run(debug=True)
