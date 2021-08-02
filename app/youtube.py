from apiclient.discovery import build
import os
from dotenv import load_dotenv
load_dotenv()

YOUTUBE_API_KEY = os.getenv('YOUTUBE_KEY')

youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def search_query(query: str):
    search_response = youtube.search().list(
        part='snippet',
        #検索したい文字列を指定
        q=query,
        #視聴回数が多い順に取得
        order='viewCount',
        type='video',
    ).execute() 
    
    videoIds = []
    for res in search_response['items']:
        videoIds.append(res['id']['videoId'])
            
    return videoIds