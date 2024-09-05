import requests

url = "https://pub-f13217639d6446309ebabc652f18d0ad.r2.dev/movies-data.json"
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    with open('movies-data.json', 'w', encoding='utf-8') as file:
        file.write(response.text)
    print("File downloaded successfully.")
else:
    print(f"Failed to download file. Status code: {response.status_code}")
