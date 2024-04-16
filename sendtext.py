#import moduleName
import requests

#moduleName.methodName()

url = ' https://api.telegram.org/bot6959397103:AAE0ukBh8tQPR8GZFjc83zJxCBWcRRM0QIk/sendMessage?chat_id=5656784248&text=ranu123'
hdrs= {
    "Accept":"*/*",
    "Accept-Encoding":"gzip, deflate, br",
    "Connection":"keep-alive"
}
response = requests.get(url,headers=hdrs)

if response.status_code == 200:
    print('Sent Successfully :) ')
    pass
else:
    print('Unable to Send :( ')
    pass