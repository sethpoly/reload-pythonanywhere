# Simple script to reload your pythonanywhere application so the data refreshes'
import requests
import os
import time
from dotenv import load_dotenv

# load local env file
load_dotenv()

username = os.environ['user']
api_token = os.environ['api_token']
domain_name = os.environ['domain_name']
timer = 1800;  # Seconds before rerun

while True:
    try:
        response = requests.post(
            'https://www.pythonanywhere.com/api/v0/user/{username}/webapps/{domain_name}/reload/'.format(
                username=username, domain_name=domain_name
            ),
            headers={'Authorization': 'Token {token}'.format(token=api_token)}
        )
        if response.status_code == 200:
            print(f'{time.strftime("%H:%M:%S", time.localtime())} - Successfully reloaded {domain_name}.')
        else:
            print('Error: Status code {}: {!r}'.format(response.status_code, response.content))
        print(f'Will reload in {timer / 60} minutes.')
        time.sleep(timer)
    except KeyboardInterrupt:
        print('Interrupted... Ending application')
        exit()
