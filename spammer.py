import requests
import time

def send_message(webhook_url, message, delay, message_count):
    for _ in range(message_count):
        data = {'content': message}
        response = requests.post(webhook_url, json=data)


        time.sleep(delay)

webhook_url = "https://discord.com/api/webhooks/1189735632961019955/WDkgxdIqon_-lNw74FkXHWFAAD-od_22jYY__rQvcMKn2r5sbUOILcrTF1055pmnVnqT"
message = "Onko Nixu Paras? add nixudev @everyone"
delay = 0 
amount_of_messages = 500  

send_message(webhook_url, message, delay, amount_of_messages)
