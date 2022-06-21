import os
import csv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

#create a .env file in the folder where this .py script lives, and securely add the slack auth token
from dotenv import load_dotenv

load_dotenv()

# auth token for the app installed in your slack workspace
auth_token = os.getenv("slack_user_oauth_token")


# ID of the channel to read the users from

channel_id = os.getenv("slack_channel_id")

client = WebClient(token=auth_token)
file = 'retrieved_users_file.csv' # path to the CSV

channel_members = client.conversations_members(channel=channel_id)

userIDs = channel_members['members']

with open(file, 'w', newline='') as csvfile:
    for i, j in enumerate(userIDs):
        user = client.users_info(user=j)
        name = user['user']['real_name'] 
        name = [name]
        csvwriter = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(name)
