import json
import pandas as pd

def convert_pandas(data):
    data = pd.DataFrame.from_dict(data)
    return data


# from google.cloud import pubsub_v1
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\kamil\Desktop\de\AirPollutionApp\secrets\shining-rampart-426818-e1-b7a4fe01e204.json"


# def create_pubsub_connection():

#     client = pubsub_v1.SubscriberClient()
#     project_id = "shining-rampart-426818-e1"
#     subscription_id = "AirPollutionTopic-sub"

#     # Create a Pub/Sub subscriber client
#     subscriber = pubsub_v1.SubscriberClient()
#     subscription_path = subscriber.subscription_path(project_id, subscription_id)

#     return subscription_path

# # Callback function to process and transform messages
# def callback(message):
#     try:
#         create_pubsub_connection()

#         # Decode the message data
#         message_data = message.data.decode("utf-8")
        
#         # Transform the message (example: convert to uppercase)
#         transformed_message = message_data.upper()
        
#         print(f"Received message: {message_data}")
#         print(f"Transformed message: {transformed_message}")
        
#         # Acknowledge the message
#         message.ack()
#     except Exception as e:
#         print(f"Error processing message: {e}")
#         message.nack()

# # Subscribe to the subscription and listen for messages
# streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
# print(f"Listening for messages on {subscription_path}...")

# # Block the main thread indefinitely to keep the subscriber running
# try:
#     streaming_pull_future.result()
# except TimeoutError:
#     streaming_pull_future.cancel()