import requests

url = 'https://example.com/'  # Url

response = requests.get(url)
content = response.text

# save page code
with open('page.html', 'w') as file:
    file.write(content)
