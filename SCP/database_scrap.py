import requests
from bs4 import BeautifulSoup
import csv
import re
import time

# Function to extract text for a given label
def extract_text(soup, label):
    element = soup.find(string=lambda text: label in text)
    if element and element.parent.name == 'strong':
        return element.parent.next_sibling.strip()
    return None

# Function to extract clearance level from containment procedures
def extract_clearance_level(soup, object_class):
    # Priority 1: Based on Object Class
    class_to_clearance = {
        'Safe': 1,
        'Euclid': 2,
        'Keter': 3,
        'Thaumiel': 4,
        'Apollyon': 5,
        'Neutralized': 0
    }
    if object_class in class_to_clearance:
        return class_to_clearance[object_class]

    # Priority 2: Search entire page content for clearance levels
    page_content = soup.find(id='page-content')
    if page_content:
        content_text = page_content.get_text(separator=" ")

        # Search for clearance levels mentioned as "Level x"
        matches = re.findall(r'(?:[Ll][Ee][Vv][Ee][Ll]\s*|\s*)\d+', content_text)
        if matches:
            levels = [int(re.search(r'\d+', match).group()) for match in matches if
                      0 <= int(re.search(r'\d+', match).group()) <= 6]
            if levels:
                return max(levels)

        # Search for clearance levels in "Class-x" or "Class x" format
        class_matches = re.findall(r'[Cc][Ll][Aa][Ss][Ss][\s-]*(\d+)', content_text)
        if class_matches:
            class_levels = [int(num) for num in class_matches if 0 <= int(num) <= 6]
            if class_levels:
                return max(class_levels)

    return 'NA'  # Default to 'NA' if no level found

# URL format for SCP entries
base_url = 'https://scp-wiki.wikidot.com/scp-'

# CSV file setup
csv_file = 'scp_data.csv'
csv_columns = ['number', 'class', 'clearance_level', 'description', 'image_url']

def clean_text(text):
    """Clean text to ensure it's in UTF-8 and replace problematic characters with a blank space."""
    if text:
        return text.encode('utf-8', errors='replace').decode('utf-8')
    return ''

# Open the CSV file for writing
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=csv_columns)
    writer.writeheader()

    # Loop through SCP entries from 1 to 1000
    for i in range(0, 1001):
        scp_number = str(i).zfill(3)  # Format the SCP number (e.g., 001, 002, ..., 999)
        url = base_url + scp_number

        try:
            # Send a GET request to fetch the content of the page
            response = requests.get(url)
            if response.status_code != 200:
                continue  # Skip if the page does not exist

            content = response.content

            # Parse the content with BeautifulSoup
            soup = BeautifulSoup(content, 'html.parser')

            # Extracting the details
            item_no_text = extract_text(soup, 'Item #:')
            item_no = re.search(r'\d+', item_no_text).group() if item_no_text else None

            object_class = extract_text(soup, 'Object Class:')
            description_start = soup.find('strong', string='Description:')
            description = description_start.find_parent('p').get_text(separator=" ").replace('Description: ', '') if description_start else None

            # Extract the image URL from the specific SCP image block
            image_block = soup.find('div', class_='scp-image-block')
            image_url = image_block.find('img')['src'] if image_block and image_block.find('img') else None

            # Extract the clearance level from Special Containment Procedures
            clearance_level = extract_clearance_level(soup, object_class)

            # Clean and ensure description is in UTF-8
            description = clean_text(description)

            # Write to the CSV file
            writer.writerow({
                'number': item_no,
                'class': object_class,
                'clearance_level': clearance_level,
                'description': description,
                'image_url': image_url
            })

            print(f"Processed SCP-{scp_number}")

            # Delay for server
            time.sleep(0.1)

        except Exception as e:
            print(f"Error processing SCP-{scp_number}: {e}")

print(f"Data has been written to {csv_file}")
