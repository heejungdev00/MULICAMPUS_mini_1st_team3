pip install google-api-python-client

import pandas
from googleapiclient.discovery import build

import warnings # 경고창 무시
warnings.filterwarnings('ignore')

comments=list()
api_obj= build('youtube', 'v3', developerKey='AIzaSyBdRH5cIjDW4mwKaGnIyp_q99blQjP0Pxc')
response = api_obj.commentThreads().list(part='snippet,replies', videoId='xOBW-CRjrCQ', maxResults=100).execute()

while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId='sWC-pp6CXpA', pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break

comments

df = pandas.DataFrame(comments)
df.to_excel('results.xlsx', header=['comment', 'author', 'date', 'num_likes'], index=None)

pip install beautifulsoup4

from bs4 import BeautifulSoup

cleaned_comments = []

for comment_data in comments:
    text_display = comment_data[0]
    cleaned_text = BeautifulSoup(text_display, "html.parser").get_text()
    cleaned_comments.append([cleaned_text] + comment_data[1:])

cleaned_comments

pip install --upgrade pip

pip install JPype1-0.5.7-cp27-none-win_amd64.whl

pip install konlpy

from konlpy.tag import Kkma
from konlpy.tag import Okt

from konlpy.utils import pprint

kkma= Kkma()

pprint(kkma.nouns('안녕하세요'))

okt = Okt()

nouns=[]
for comment_data in comments:
    text_display = comment_data[0]
    cleaned_text = BeautifulSoup(text_display, "html.parser").get_text()
    noun=okt.nouns(cleaned_text)
    nouns.append(noun)
    

print(nouns)

str_nouns=[','.join(map(str,i))for i in nouns]
result=','.join(str_nouns)
result

from collections import Counter