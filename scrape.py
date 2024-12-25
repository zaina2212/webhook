import requests
from bs4 import BeautifulSoup

# Send a GET request to the website you want to scrape
url = 'https://laserstat.pro/?lang=en'  # Replace with the URL you want to scrape
response = requests.get(url)

# If the request was successful, proceed
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Example: Find all links (a tags) on the page
    links = soup.find_all('a')

    # Print out the links
    for link in links:
        print(link.get('href'))
else:
    print("Failed to retrieve the webpage")
