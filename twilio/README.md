## How to use

- Go to the [Twilio website](https://www.twilio.com/docs/libraries/python) and create an app.
- Copy the ACCOUNT_SID and AUTH_TOKEN keys
- Create a file called `config.py` in the root of the project
- Add the following lines to the file: ```
ACCOUNT_SID = 'YOUR_ACCOUNT_SID'
AUTH_TOKEN = 'YOUR_AUTH_TOKEN'```
- Call `send_sms` function with the following parameters: `to_number`, `from_number`, `message`