from openai import OpenAI
import openai
import os

#https://platform.openai.com/docs/guides/gpt/chat-completions-api의 질의어로 테스트해보자
client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def AIChatBot(content,model='gpt-3.5-turbo',messages=[],temperature=1):
    error=None
    try:
        messages.append({'role':'user','content':content})
        response = client.chat.completions.create(messages=messages, model=model)
        answer=response.choices[0].message.content
        messages.append({'role':'user','content':answer})
        return {'status':'SUCCESS','messages':messages}
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        error=e
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        error = e
    except openai.error.InvalidRequestError as e:
        print(f"Invalid Request to OpenAI API: {e}")
        error = e
    except openai.error.RateLimitError as e:
        # Handle rate limit error (we recommend using exponential backoff)
        print(f"OpenAI API request exceeded rate limit: {e}")
        error = e
    return {'status': 'FAIL', 'messages': error}




if __name__=='__main__':
    messages=[]
    while True:
        content=input('질의하세요')
        response=AIChatBot(content,messages=messages)

