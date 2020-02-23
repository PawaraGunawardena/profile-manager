import os
import shutil
import time

import pyrebase

# Replace this with your own configuration of firebase
# To get this variable follow the README.md
config = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    'appId': "",
    "measurementId": ""
}

# Replace this with your own configuration of firebase.
# Copy the config variable, add "serviceAccount" and set path to jason as the value. Follow README.md to get the json
config_for_storage = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    'appId': "",
    "measurementId": "",
    "serviceAccount": "path_to_your_json.json"
}


import firebase_admin
from firebase_admin import credentials

json_path = "path_to_your_json.json"
cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred)

local_image_directory = "images"

class FileManager:

    def __init__(self):
        self.firebase = pyrebase.initialize_app(config)
        self.storage = self.firebase.storage()

    def insert(self, id, local_path):
        self.storage.child("images/"+id+"/image.jpg").put(local_path)

    def download(self, id):
        folder_to_download = local_image_directory+"/"+id

        if(not os.path.exists(folder_to_download)):
            os.makedirs(folder_to_download)

        self.storage.child("images/"+id+"/image.jpg").download(folder_to_download+"/image.jpg")
        time.sleep(1)

    def remove_from_local(self, id):
        folder_to_download = local_image_directory + "/" + id
        if (os.path.exists(folder_to_download) and os.path.isdir(folder_to_download)):
            shutil.rmtree(folder_to_download)

    def remove_from_remote(self, id):

        firebase = pyrebase.initialize_app(config_for_storage)
        storage = firebase.storage()
        storage.delete("images/"+id+"/image.jpg")


if __name__ == "__main__":
    file_manager = FileManager()

