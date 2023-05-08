import requests

def check_facebook_token_validity(access_token):
    url = f"https://graph.facebook.com/me?access_token={access_token}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        return False

access_token = 'EAAAAUaZA8jlABAETiJoktm1vvSKdI9UNXI25XHonDo6sxu7ZBxud8r83XZCuYwZAt5ZC0o0IzN7D1QYcZA3m93AYc9vnwGHxYlKXRZCdF7MdQWQ9OH0SvBIwR2OHVq7YV5fyrWxrHLZAM6OIUQyzl225XI8Mpw1XzCQ4lKnXPwPo0XzQsnQgNmRQHOVR5UJHdQkZD'
is_valid = check_facebook_token_validity(access_token)

if is_valid:
    print("Facebook access token is valid.")
else:
    print("Facebook access token is not valid.")