import requests

def fetch_youtube_updates(channel_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/search?channelId={channel_id}&order=date&part=snippet&maxResults=3&key={api_key}"
    response = requests.get(url)
    data = response.json()
    videos = []
    for item in data.get('items', []):
        snippet = item['snippet']
        title = snippet.get('title', '')
        description = snippet.get('description', '')
        videos.append(f"{title}: {description}")
    return videos
