import os
import json
import requests

#get key from system environment varibles
bearer_token = os.environ.get("BEARER_TOKEN")

#params for twitter users, spaces
params = {"tweet.fields": "created_at"}
query_params_space = {'query': 'NBA', 'space.fields': 'title,created_at', 'expansions': 'creator_id'}

#create url for searching users
def create_url():
    usernames = "usernames=TwitterDev,TwitterAPI,YouTube,TheLancet"
    user_fields = "user.fields=description,created_at"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(usernames, user_fields)
    return url
#create url for searching tweet time-line
def create_url_1():
    user_id = 27013292
    return "https://api.twitter.com/2/users/{}/tweets".format(user_id)

#create url for searching spaces
def create_url_space():
    search_url = "https://api.twitter.com/2/spaces/search"
    return search_url

#oauth authorization
def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "EC601_test_1"
    return r

def connect_to_endpoint(url):
    response = requests.get(url, auth=bearer_oauth)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def connect_to_endpoint_1(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Request returned an error: {} {}".format(
                response.status_code, response.text
            )
        )
    return response.json()

def main():
    url = create_url()
    url_1 = create_url_1()
    url_space = create_url_space()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent = 4, sort_keys = True))
    json_response_timeline = connect_to_endpoint_1(url_1, params)
    print(json.dumps(json_response_timeline, indent=4, sort_keys=True))
    json_response_space = connect_to_endpoint_1(url_space, query_params_space)
    print(json.dumps(json_response_space, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()



