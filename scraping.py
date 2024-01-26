import requests
from bs4 import BeautifulSoup
import tabula
import logging
from flask import Flask, request, jsonify, send_file
import sqlite3
import pandas as pd

def extract_tables(pdf_path):
    try:
        tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
        return tables
    except Exception as e:
        print(f"Error during PDF scraping: {str(e)}")
        return None
pdf_path = 'C:/Users/Maira/Downloads/pdf_web_scraping/sample.pdf'
extracted_tables = extract_tables(pdf_path)
if extracted_tables:
    for i, table in enumerate(extracted_tables):
        print(f"Table {i + 1}:\n{table}\n")
else:
    print("PDF scraping failed.") 

req = requests.get("https://www.python.org/")
soup = BeautifulSoup(req.content, "html.parser")
res = soup.title
print(res.get_text())

req = requests.get("https://www.python.org/")
soup = BeautifulSoup(req.content, "html.parser")
res = soup.title
print(res.get_text())
print(res.prettify())

import requests
from bs4 import BeautifulSoup
req = requests.get("https://www.python.org/")
soup = BeautifulSoup(req.content, "html.parser")
res = soup.title
print(res.get_text())
print(res.prettify())
print(soup.prettify())



url = 'https://www.python.org/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
news_headlines = []
for headline in soup.find_all('div', class_='shrubbery')[0].find_all('li'):
    news_headlines.append(headline.text.strip())
for headline in news_headlines:
    print(headline)

# Extracted PDF data
pdf_data = [
    {"Name": "John Doe", "Age": 30, "Occupation": "Engineer"},
    {"Name": "Jane Smith", "Age": 25, "Occupation": "Designer"},
    {"Name": "Bob Johnson", "Age": 40, "Occupation": "Teacher"},
    {"Name": "Alice Brown", "Age": 35, "Occupation": "Doctor"},
    {"Name": "Charlie Wilson", "Age": 28, "Occupation": "Developer"},
    {"Name": "Eva Davis", "Age": 45, "Occupation": "Writer"},
    {"Name": "Frank White", "Age": 32, "Occupation": "Artist"},
    {"Name": "Grace Miller", "Age": 38, "Occupation": "Scientist"},
    {"Name": "Henry Moore", "Age": 50, "Occupation": "Manager"}
]

# Extracted web data
web_data = [
    {"date": "2024-01-18", "title": "Announcing Python Software Foundation Fellow Members for Q3 2023! 🎉"},
    {"date": "2024-01-18", "title": "Announcing the Deputy Developer in Residence and the Supporting Developer in Residence"},
    {"date": "2024-01-18", "title": "Python 3.13.0 alpha 3 is now available."},
    {"date": "2024-01-12", "title": "EU’s Cyber Resilience Act Passes with Wins for Open Source"},
    {"date": "2023-12-15", "title": "Python Software Foundation - December 2023 Newsletter"}
]

# Combine PDF and web data into a unified format
combined_data = []

for pdf_record, web_record in zip(pdf_data, web_data):
    combined_record = {
        "Name": pdf_record["Name"],
        "Age": pdf_record["Age"],
        "Occupation": pdf_record["Occupation"],
        "Date": web_record["date"],
        "Title": web_record["title"]
    }
    combined_data.append(combined_record)

# Display the combined data
for record in combined_data:
    print(record)

import sqlite3

# Connect to SQLite database (or create one if it doesn't exist)
conn = sqlite3.connect('data.db')

import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('data.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Execute a SELECT query to fetch data from the combined_data table
cursor.execute('SELECT * FROM combined_data')

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

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
