import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the URL of Mani Sharma's discography page on Wikipedia
url = "https://en.wikipedia.org/wiki/Mani_Sharma"
# Step 2: Send an HTTP request to fetch the HTML content of the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Step 3: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'lxml')

    # Step 4: Find all tables with class 'wikitable' that usually contain discography data
    tables = soup.find_all('table', class_='wikitable')

    # Initialize an empty list to store data from all tables
    all_data = []

    # Step 5: Loop through each table and extract rows
    for table in tables:
        # Extract table headers
        headers = [header.text.strip() for header in table.find_all('th')]

        # Extract table rows
        rows = table.find_all('tr')
        table_data = []

        # Loop through each row, skipping the first header row
        for row in rows[1:]:
            # Extract table data cells
            cells = row.find_all(['td', 'th'])
            cell_data = [cell.text.strip() for cell in cells]
            table_data.append(cell_data)

        # Combine headers with the data
        df = pd.DataFrame(table_data, columns=headers)
        all_data.append(df)

    # Display data from the first table as an example
    if all_data:
        print("Extracted data from the first table:")
        print(all_data[0])
    else:
        print("No tables found on the page.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
# Save the first table to a CSV file
if all_data:
    all_data[0].to_csv('mani_sharma_discography.csv', index=False)
    print("Data saved to 'mani_sharma_discography.csv'")
