import os
import webbrowser
from urllib.parse import urlencode

import requests
from dotenv import load_dotenv
from flask import Flask, request

load_dotenv()
client_id = os.environ.get('DRCHRONO_CLIENT_ID')
client_secret = os.environ.get('DRCHRONO_CLIENT_SECRET')

REDIRECT_URI = 'http://localhost:5000/authorize'


def start_oauth_flow():
    oauth_init_url = "https://drchrono.com/o/authorize/?" + urlencode({
        'redirect_uri': REDIRECT_URI,
        'response_type': 'code',
        'client_id': client_id
    })
    webbrowser.open(oauth_init_url)


app = Flask(__name__)


@app.route('/authorize')
def authorize():

    code = request.values.get('code')
    response = requests.post('https://drchrono.com/o/token/', data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'client_id': client_id,
        'client_secret': client_secret
    })
    response.raise_for_status()
    data = response.json()

    # Save these in your database associated with the user
    access_token = data['access_token']
    refresh_token = data['refresh_token']

    with open('oauth_access_token', 'w') as f:
        f.write(access_token)

    return "Authorization successful"


if __name__ == '__main__':
    start_oauth_flow()
    app.run()
