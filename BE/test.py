import requests

url = "https://us-central1-rich-agency-372104.cloudfunctions.net/chat_function"
data = {"message": "Hello, how are you?"}  # Replace with your desired message

response = requests.post(url, json=data)

if response.status_code == 200:
    print(response.json())
else:
    print("Error:", response.text)
