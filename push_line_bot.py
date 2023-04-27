
import requests
import json

# 設定Line Bot的Channel Access Token和Channel Secret
channel_access_token = "gd2k8snxpn3PP+nC+spxDIgQF6ZTtjfS/vHmqOIEJ8W/B1bryahPh61EfFIepnHqfjTQ4zhc29120TvtHVjk4dMB5vkrJFtvcjO07389gomlkggI/rMJCoid9PCCr6O3v0dTY2R3n4FFA6IMr1D5twdB04t89/1O/w1cDnyilFU="
channel_secret = "82ab0090dc70c5f7d3a6c62fb1e09eb8"

# 設定推送訊息的URL
url = "https://api.line.me/v2/bot/message/push"

# 設定推送的消息
payload = {
    "to": "U65614b139436a7af7d95a8fba65611d3",
    "messages": [
        {
            "type": "text",
            "text": "你好，這是一條來自Line Bot(push_line_bot)的訊息！"
        }
    ]
}

# 設定Header，包括Channel Access Token和Content-Type
headers = {
    "Authorization": "Bearer " + channel_access_token,
    "Content-Type": "application/json"
}

# 發送POST請求，推送消息
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 列印回應結果
print(response.content)

exit ()