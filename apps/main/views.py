
import os
import requests
from django.http import JsonResponse

def search(request, query="dynamodb python"):
    subscription_key = os.environ.get('BING_SEARCH_V7_SUBSCRIPTION_KEY')
    endpoint = "https://api.cognitive.microsoft.com/bing/v7.0/search"

    # Construct a request
    mkt = 'en-US'
    params = { 'q': query, 'mkt': mkt }
    headers = { 'Ocp-Apim-Subscription-Key': subscription_key }

    try:
        print(hea)
        response = requests.get(endpoint, headers=headers, params=params, verify=False)
        data = response.json()

    except Exception as ex:
        data = {
            "error": str(ex)
        }

    return JsonResponse(data)
