import requests

def ask_chat_gpt(question):
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user', 'content': question}]
    }
    response = requests.post(url, headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['message']['content']
