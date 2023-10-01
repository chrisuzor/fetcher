# Description: This file is responsible for sending data to Parser microservice.

url = ''
def send_to_mews(mews_object: str) -> str:
    print('sending parser data to mews ', mews_object)
    return 'success'
    # client = httpx.Client()
    # response = client.get(url, params=mews_object)
    # response_json = json.loads(response.text)
