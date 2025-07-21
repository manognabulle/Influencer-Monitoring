import requests

def send_to_slack(message, webhook_url):
    payload = {"text": message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code != 200:
        print(f"Slack notification failed: {response.text}")
