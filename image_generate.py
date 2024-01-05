import requests
from openai import OpenAI #OpenAI사가 제공하는 클라이언트용 함수 호출용
import openai
import os,json
import urllib.request

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

'''
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
url = 'https://api.openai.com/v1/images/generations'

header ={"Content-Type": "application/json","Authorization": f'Bearer {OPENAI_API_KEY}'}
data = {
        "model":"dall-e-3",
        "prompt":"very very cute cat",
        'n':1, # 이미지 수
        'size':'1024x1024', # 이미지 크기 1024
        'response_format':'b64_json'
        }
res = requests.post(url = url,data=json.dumps(data),headers=header)
#print(res) # <Response [200]>
#print(res.json())

answer = res.json()
print(answer['data'][0]['b64_json']) #response_format이 "url"일때 디폴트값
b64_json = answer['data'][0]['b64_json']
#b64_json 인코딩 문자열(base64로 인코딩된 문자열)을 로컬에 이미지로 저장
import base64
binary_image = base64.b64decode(b64_json) #바이너리 데이타로 디코딩
with open('otter.jpg','wb') as f:
    f.write(binary_image)
'''

'''
try:
  prompts=input('생성할 이미지를 묘사해주세요?')

  client = OpenAI()

  response = client.images.generate(
    model="dall-e-3",
    prompt=prompts,
    size="1024x1024",
    quality="standard",
    n=1,
  )

  image_url = response.data[0].url
  print(image_url)

  # urllib.request.urlretrieve(image_url,f'{prompts.strip()}.jpg')
  res=requests.get(image_url)
  with open(f'{prompts.replace(" ","")}.jpg','wb') as f:
    f.write(res.content)
'''
#https://platform.openai.com/docs/guides/error-codes/python-library-error-types
'''
except openai.error.APIError as e:
    # Handle API error here, e.g. retry or log
    print(f"OpenAI API returned an API Error: {e}")
except openai.error.APIConnectionError as e:
    # Handle connection error here
    print(f"Failed to connect to OpenAI API: {e}")
except openai.error.InvalidRequestError as e:
    print(f"Invalid Request to OpenAI API: {e}")
except openai.error.RateLimitError as e:
    # Handle rate limit error (we recommend using exponential backoff)
    print(f"OpenAI API request exceeded rate limit: {e}")
'''

model = 'gpt-3.5-turbo'
client = OpenAI()
def chatComplete(client, model, messages):
    response = client.chat.completions.create(model = model, messages=messages)
    return response
prompt=input('생성할 이미지를 묘사해주세요?')
messages=[{"role":"system", "content":"you are a translation expert who translates korean into english"},
                {"role": "user", "content": prompt}]

response=chatComplete(client,model,messages)
english=response.choices[0].message.content
print(english)
response = client.images.generate(
    model="dall-e-3",
    prompt=english,
    size="1024x1024",
    quality="standard",
    n=1,
  )

image_url = response.data[0].url
print(image_url)

# urllib.request.urlretrieve(image_url,f'{prompts.strip()}.jpg')
res=requests.get(image_url)
with open(f'{prompt.replace(" ","")}.jpg','wb') as f:
    f.write(res.content)