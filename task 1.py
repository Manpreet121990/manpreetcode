import os
import requests
from bs4 import BeautifulSoup

# Define the URL of the article
url = "https://www.consumerreports.org/cars/new-cars-on-the-horizon-a1920770135/"

# Create a folder to store the scraped articles
output_folder = "scraped_articles"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define headers to mimic a browser
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )
}

try:
    # Send a GET request with headers
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for HTTP request errors

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the main content of the article (adjust tag if necessary)
    article_body = soup.find('main')  # Find the main tag for the article content
    if article_body:
        article_text = article_body.get_text(separator="\n").strip()
    else:
        article_text = "Could not find the main content of the article."

    # Save the content to a .txt file
    output_file = os.path.join(output_folder, "scraped_article.txt")
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(article_text)

    print(f"Article successfully saved to {output_file}")

except Exception as e:
    print(f"An error occurred: {e}")
