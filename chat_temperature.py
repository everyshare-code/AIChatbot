import requests
# import openai
from openai import OpenAI
import json,os,time

def chatComplete(client,model,messages,temperature):
    response = client.chat.completions.create(messages=messages, model=model,temperature=temperature)
    return response

'''
- 설치한 openai 라이브러리는 ChatGPT API 외에도 DALL-E API도 사용가능
(DALL-E API 사용시 API KEY가 필요없다)
-생성된 이미지는 URL 형태(기본값)로 제공(URL은 1시간 후에 만료)
https://platform.openai.com/docs/quides/images/usage
URLs will expire after an hour.
-response_format를 b64_json 설정시 base64로 인코딩된 문자열을 반환
※한글로 이미지 생성 prompts를 전달하면 원하는 이미지가 생성이 안된다.
그래서 영어로 번역후 번역된 prompts를 DALL-E모델에 전달한다
팁 : 한글을 gpt-3.5-turbo에게 번역 의뢰->번역된 영어로 DALL-E모델에게 전송
'''