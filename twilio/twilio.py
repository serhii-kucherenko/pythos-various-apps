from twilio.rest import Client
from config import ACCOUNT_SID, AUTH_TOKEN

client = Client(ACCOUNT_SID, AUTH_TOKEN)


def send_sms(to_number: str, from_number: str, message: str):
    message = client.messages.create(
        to=to_number,
        from_=from_number,
        body=message)

    print(message.sid)
