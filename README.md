# Appointment booking starter

## Getting access token

1. Create virtual environment and run `pip install -r requirements.txt`
1. Copy Client ID and Client Secret from https://app.drchrono.com/api-management/
    and save in the `.env` file
    
    OR 
    ```
    export DRCHRONO_CLIENT_ID=
    export DRCHRONO_CLIENT_SECRET=
   ```

1. Run 
    ```
    python oauth.py
   ```
1. Authenticate with your Drchrono credentials on the opened web page. 

## Using the token

Token is saved as plain text in the `./oauth_access_token` file. Feel free to modify
this code and use the oauth_access_token as you want.

Read the docs on the actual API here https://app.drchrono.com/api-docs/#operation/appointments_update
