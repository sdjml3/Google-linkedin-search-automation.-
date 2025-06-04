import requests


def search_gemini(query):
    api_key = "your Api key"
    
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" + api_key

    headers = {
        "Content-Type": "application/json"
    }
    data = {
    "contents": [
        {
            "parts": [
                {
                    "text": query,
                }
            ]
        }
    ]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()   
        return response.json()  
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"



