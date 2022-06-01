import requests
import json


def get_api_data():
    response_API = requests.get('https://api.covid19india.org/data.json')
        #response_API = requests.get('https://6djst4shy1.execute-api.us-east-1.amazonaws.com/Covid_Api_Deploy/sno/%d' % (num))
        #num+=1
        
    data = response_API.text
    data2 = json.loads(data)
    return (data2)

if __name__=="__main__":
    print(get_api_data())