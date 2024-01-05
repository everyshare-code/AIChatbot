import requests
# import openai
from openai import OpenAI
import json,os

# print(os.getenv('OPENAI_API_KEY'))
# print(dir(openai))

#REST API로 요청 pip install openai가 필요없다(단, pip install requests만 실행)


'''
url='https://api.openai.com/v1/chat/completions'
headers = {"Content-Type": "application/json","Authorization":f'Bearer {OPENAI_API_KEY}'}
data = {
    'model':"gpt-3.5-turbo",
    'messages':[{"role": "system", "content": "you are a kindergarten teacher"},
                {"role": "user", "content": "What is Artificial Intelligence?"}]
}


res=requests.post(url=url,data=json.dumps(data),headers=headers)
print(res.json())
data=res.json()
content=data['choices'][0]['message']['content']
print('ChatGPT응답:',content)
'''
OPENAI_API_KEY=os.getenv('OPENAI_API_KEY')
model='gpt-3.5-turbo'
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)
messages=[{"role": "system", "content": "you are a kindergarten teacher"},
                {"role": "user", "content": "What is Artificial Intelligence?"}]

def chatComplete(client,model,messages):
    response = client.chat.completions.create(messages=messages, model=model)
    return response

response=chatComplete(client,model,messages)
print('type(response):',type(response))
print('dir(response):',dir(response))
print('response:',response)
answer=response.choices[0].message.content
print('ChatGPT응답:',answer)

messages.append({"role": "assistant", "content": answer})
messages.append({"role": "user", "content": "한국어로 번역해줘"})
'''
role은 assistant로 content은 이전 응답으로 설정 추가
ChatGPT가 이전에 응답한 결과를 알 수 있도록하기 위함
왜냐하면 대화의 문맥을 유지하기 위함
아래 주석시 이전의 응답을 번역하지 않고
질문을 번역한다(인공지능이란 무엇인가요?)
'''

response=chatComplete(client,model,messages)
korean=response.choices[0].message.content
print('ChatGPT응답:',korean)
