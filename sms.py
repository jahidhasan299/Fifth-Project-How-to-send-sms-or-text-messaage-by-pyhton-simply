from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC263c5e4acdc4bbd67bb32857874ecf60'
auth_token = 'a778c95e410a633b9ec3d10474a0f925'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hi there!,it/s me from china can we make a friends?',
                              from_='+12013319818',
                              to='+8613224011791'
                          )

print(message.sid)
