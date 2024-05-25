import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

# URL of the Telegram channel
channel_url = 'https://t.me/s/TikvahEthiopia'

# Request the page content
response = requests.get(channel_url)
response.raise_for_status()  # Check that the request was successful

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'lxml')

# Initialize a list to hold the data
data = []

# Scrape messages
messages = soup.find_all('div', class_='tgme_widget_message')

for message in messages:
    try:
        # Extract the date and time
        date_element = message.find('time')
        if date_element and 'datetime' in date_element.attrs:
            date = date_element['datetime'].split('T')[0]
            post_time = date_element['datetime'].split('T')[1].split('+')[0]
        else:
            continue  # Skip this message if date or time is not available

        # Extract the post link
        post_link_element = message.find('a', class_='tgme_widget_message_date')
        post_link = post_link_element['href'] if post_link_element else ''

        # Extract the view count
        view_count_element = message.find('span', class_='tgme_widget_message_views')
        view_count = view_count_element.text if view_count_element else '0'

        # Determine the time of day
        hour = int(post_time.split(':')[0])
        if 6 <= hour < 12:
            time_of_day = 'Morning'
        elif 12 <= hour < 18:
            time_of_day = 'Afternoon'
        else:
            time_of_day = 'Evening'
        
        # Append the data to the list
        data.append([date, post_link, view_count, post_time, 'Abyssinia Bank', time_of_day])
    except Exception as e:
        print(f"Error processing message: {e}")

# Write data to CSV
with open('bank_ad_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Date', 'Post Link', 'View Count', 'Post Hour', 'Bank', 'Time of Day'])
    writer.writerows(data)