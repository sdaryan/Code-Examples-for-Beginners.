import requests
from bs4 import BeautifulSoup

# Set the URL of the webpage you want to scrape
url = 'https://www.example.com'

# Send an HTTP request to the URL and retrieve the HTML content
response = requests.get(url)

# Create a BeautifulSoup object that parses the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the webpage
links = soup.find_all('a')

# Print the text and href attribute of each link
for link in links:
    print(link.get('href'), link.text)


'''
Explanation:

In this code, we first import the requests and BeautifulSoup modules which are used to make HTTP requests and parse HTML content, respectively.
Next, we set the URL of the webpage that we want to scrape in a variable called url.
We then use the requests.get() function to send an HTTP GET request to the URL and retrieve the HTML content of the webpage as a response.
We create a BeautifulSoup object called soup that parses the HTML content of the response using the html.parser parser.
We then use the soup.find_all() method to find all the links on the webpage and store them in a variable called links.
Finally, we use a for loop to iterate through each link in links and print the text and href attribute of each link using the link.get() method.
'''