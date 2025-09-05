# Uncomment the imports below before you add the function code
import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="https://arjames1128-3030.theiadockernext-0-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/fetchDealers/")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="https://sentianalyzer.1zydvyygiwwx.us-south.codeengine.appdomain.cloud/")

def get_request(endpoint, **kwargs):
    params = ""
    if(kwargs):
        for key,value in kwargs.items():
            params=params+key+"="+value+"&"

    request_url = backend_url+endpoint+"?"+params

    print("GET from {} ".format(request_url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except:
        # If any error occurs
        print("Network exception occurred")

def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    print(f"POST to {request_url}")
    print(f"Data being sent: {data_dict}")
    
    try:
        response = requests.post(request_url, json=data_dict)
        print(f"Response status code: {response.status_code}")
        print(f"Response text: {response.text}")
        
        if response.status_code == 200:
            try:
                return response.json()
            except:
                return {"status": 200, "message": "Review posted successfully"}
        else:
            return {"status": response.status_code, "message": f"Backend error: {response.text}"}
            
    except requests.exceptions.ConnectionError as e:
        print(f"Connection error: {e}")
        return {"status": 500, "message": "Cannot connect to backend service"}
    except requests.exceptions.Timeout as e:
        print(f"Timeout error: {e}")
        return {"status": 500, "message": "Request timed out"}
    except Exception as e:
        print(f"Unexpected error in post_review: {e}")
        return {"status": 500, "message": f"Network exception: {str(e)}"}

