import fbchat

from getpass import getpass
username = str(input("Username: "))
client= fbchat.Client(username, getpass())
no_of_friends = int(input("Number OF Friends You Got: "))
for i in range(no_of_friends):
    name = str(input("Name You Wish To Send A Message To: "))
    friends = client.getUsers(name)
    friend = friends[0]
    msg = str(input("Message You Wish To Send: "))
    sent = client.send(friend.uid, msg)
    if sent:
        print("Message Sent Successfully!")

