## Running the PDF and Web Data Scraping Script:
This document provides instructions on how to run the Python script for extracting data from PDF files and performing web scraping to collect additional information. The script also integrates with a database to store the extracted data and provides an API endpoint for data storage.

## Dependencies
Before running the script, following dependencies are required:

Download from these websites:
Python : https://www.python.org/
vs code: https://code.visualstudio.com/
jupyter : https://jupyter.org/
Required Python packages:
Flask
pandas
requests
tabula-py
BeautifulSoup (bs4)
sqlite3

## Installing these dependencies using pip:

pip install flask pandas requests tabula-py beautifulsoup4

## Running the Script
Clone the Repository: 
git clone https://github.com/maira000/pdf_web_scraping
cd your-repository

Open a Jupyter notebook or a Python script editor.

Run the script.

python script.py

Script Configuration
The script does not require any additional configuration. However, you can customize the following variables in the script:

pdf_path: sample.pdf
web_url: https://www.python.org/

Navigate to the Directory: 
Open a terminal or command prompt and navigate to the directory where the script is located.

Run the Script: 
Execute the script using the following command:
python script.py

# Accessing the API Endpoint: 
Once the script is running, you can access the API endpoint to store data in the database. By default, the endpoint URL is http://127.0.0.1:5000/store_data.

# Downloading Data: 
To download the stored data as an Excel file, access the download endpoint. The download URL is http://127.0.0.1:5000/download_data.

# Usage
PDF Data Extraction: The script automatically extracts structured data from PDF files located in the specified directory. Ensure that the PDF files are in a readable format and accessible to the script.

# Web Scraping: 
The script performs web scraping to gather additional information related to the extracted PDF data. It accesses predefined web pages and extracts relevant data from them.

# Data Storage: 
The extracted data is stored in a SQLite database. Each run of the script appends the new data to the database.

# Additional Notes
Ensure that you have proper permissions to read/write files in the specified directories.
Handle any errors or exceptions encountered during the execution of the script.
Modify the script as needed to suit your specific requirements or use cases.

# Conclusion
By following these instructions, you can successfully run the PDF and web data scraping script, extract structured data from PDF files, perform web scraping, store the data in a database, and access it via an API endpoint.





