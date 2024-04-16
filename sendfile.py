#import moduleName
import requests

#moduleName.methodName()

url = 'https://api.telegram.org/bot6959397103:AAE0ukBh8tQPR8GZFjc83zJxCBWcRRM0QIk/sendDocument'
with open("ry.png", 'rb') as file:

    fls = {'document':file}
    dt = {'chat_id': "5656784248"}


    response = requests.post(url,files=fls, data=dt)

    if response.status_code == 200:
        print('File Sent Successfully :) ')
        pass
    else:
        print('Unable to Send File :( ')
        pass