import sqlite3
import time

from firebase import firebase
from tkinter import PhotoImage
from PIL import ImageTk,Image
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True

# TODD Update the DB_URL and DB_NAME. How to get the DB_URL is explain in the README.md
DB_URL = "https://your_db_url.com/"
DB_NAME = "your-db-name"
TABLE_FEATURE_NAME = "Feature"
TABLE_FEATURE_PATH = DB_NAME+"/"+TABLE_FEATURE_NAME

class FirebaseDBManager:

    def __init__(self):
        self.firebase = firebase.FirebaseApplication(DB_URL, None)

    def getFirebaseDB(self):
        return firebase

    def insert(self, data):
        results = self.firebase.post(TABLE_FEATURE_PATH, data)
        return results
    def getAllData(self):
        results = self.firebase.get(TABLE_FEATURE_PATH, '')
        return results
    def getSpecificData(self, id):
        results = self.firebase.get(TABLE_FEATURE_PATH,  id)
        return results

    def update(self, id, attribute, new_value):
        results = self.firebase.put(TABLE_FEATURE_PATH+"/"+id, attribute, new_value)
        return results


    def delete(self, id):
        results = self.firebase.delete(TABLE_FEATURE_PATH, id)
        return results


import _sqlite3

class SQLiteDBManager:
    def __init__(self):
        self.firebase = firebase.FirebaseApplication(DB_URL, None)
        self.database = self.initialize_db(DB_NAME+'.db')
        self.initialize_table()

    def initialize_db(self, db_name):
        database = _sqlite3.connect(db_name)
        return database

    def initialize_table(self):
        self.database.execute(
            ''' CREATE TABLE IF NOT EXISTS Feature(
            ID TEXT,
            NAME TEXT,
            PHONE TEXT, 
            NOTE TEXT,
            GENDER TEXT,
            DATE TEXT,
            ADDRESS TEXT,
            IMAGE TEXT) '''
                              )

    def getSQLiteDB(self):
        return self.database

    def insert(self, data):
        self.database.execute(''' INSERT INTO Feature(ID, NAME, PHONE, NOTE, GENDER, DATE, ADDRESS, IMAGE)
                    VALUES(?,?,?,?,?,?,?,?)''', (data['ID'], data['Name'], data['Phone'], data['Note'], data['Gender'], data['Date'], data['Address'], data['Image']))
        self.database.commit()

    def getAllData(self):
        data = self.database.execute(''' SELECT * FROM Feature ORDER BY NAME''')

    def getAllIDs(self):
        data = self.database.execute(''' SELECT ID FROM Feature ORDER BY NAME''')

        temp_list =[]
        for record in data:
            temp_list.append(str(record[0]))

        return temp_list

    def getSpecificData(self, id):
        data = self.database.execute("SELECT * FROM Feature WHERE ID = '"+id+"'")

        exist = False

        temp_dict = {}
        for record in data:
            exist = True

            temp_dict['ID'] = str(record[0])
            temp_dict['Name'] = str(record[1])
            temp_dict['Phone'] = str(record[2])
            temp_dict['Note'] = str(record[3])
            temp_dict['Gender'] = str(record[4])
            temp_dict['Date'] = str(record[5])
            temp_dict['Address'] = str(record[6])
            temp_dict['Image'] = str(record[7])

        # return data, exist
        return temp_dict, exist

    def getSpecificDataFromName(self, name):

        data = self.database.execute("SELECT Id, Image FROM Feature WHERE Name = '"+name+"'")
        exist = False
        temp_dict = {}

        for record in data:

            temp_dict['ID'] = str(record[0])
            temp_dict['Image'] = int(record[1])

            if(temp_dict['Image'] == 1):
                exist = True

        return temp_dict, exist

    def convert_to_dict(self, data):
        temp_dict = {}
        for record in data:
            temp_dict['ID'] = str(record[0])
            temp_dict['Name'] = str(record[1])
            temp_dict['Phone'] = str(record[2])
            temp_dict['Note'] = str(record[3])
            temp_dict['Gender'] = str(record[4])
            temp_dict['Date'] = str(record[5])
            temp_dict['Address'] = str(record[6])
            temp_dict['Image'] = str(record[7])
        return temp_dict

    def update(self, id, attribute, new_value):
        self.database.execute("UPDATE Feature set "+attribute+"='" +new_value+"' WHERE ID='"+id+"'")
        self.database.commit()

    def delete(self, id):
        self.database.execute("DELETE from Feature WHERE ID='"+id+"'")
        self.database.commit()

    def fill_treeview(self, tree):

        self.image_list = []

        data = self.database.execute(''' SELECT Name, Phone, Gender, Date, Address, Note, ID, Image FROM Feature ORDER BY NAME ASC''')

        for record in data:
            if int(record[7]) == 1:
                Id = str(record[6])


                image_path = "./images/"+Id+"/image.jpg"

                saved_image, opened = self.open_resized_image(image_path)

                while (not opened):
                    saved_image, opened = self.open_resized_image(image_path)
                    continue
                self.image_list.append(saved_image)
                tuple= (str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4]), str(record[5]))
                tree.insert("", "end", image=self.image_list[-1], values=tuple)

                tree.image = self.image_list[-1]

            else:
                tuple= (str(record[0]), str(record[1]), str(record[2]), str(record[3]), str(record[4]), str(record[5]))
                tree.insert("", "end", values=tuple)


    def open_resized_image(self, image_path):
        try:
            saved_image = Image.open(image_path)

            imwidth =20  # the new width you want

            # the next three lines of codes are used to keep the aspect ration of the image
            wpersent = (imwidth / float(saved_image.size[0]))
            hsize = int(float(saved_image.size[1]) * float(
                wpersent))
            # size[1] means the height and the size[0] means the width you can read more about this in th PIL documentation
            saved_image = ImageTk.PhotoImage(saved_image.resize((
                imwidth, hsize),
                Image.ANTIALIAS)
            )
            # set the width and put it back in the chromelogo variable

            return saved_image, True

        except FileNotFoundError:
            return None, False
    def open_resized_image_with_tk(self, image_path):
        saved_image = ImageTk.PhotoImage(image_path)
        # imwidth = 50  # the new width you want
        # # the next three lines of codes are used to keep the aspect ration of the image
        # wpersent = (imwidth / float(saved_image.size[0]))
        # hsize = int(float(saved_image.size[1]) * float(
        #     wpersent))  # size[1] means the height and the size[0] means the width you can read more about this in th PIL documentation
        # saved_image = ImageTk.PhotoImage(saved_image.resize((imwidth, hsize),
        #                                                     Image.ANTIALIAS))  # set the width and put it back in the chromelogo variable

        return saved_image

    def getImageCount(self):

        data = self.database.execute("SELECT COUNT(*) FROM Feature WHERE Image = '1'")
        count = 0

        for record in data:
            count = record[0]

        return count

if __name__ == "__main__":
    # firebase_db_manager = FirebaseDBManager()

    data = {
        'Name': 'Sample Name 1',
        'Phone': '000111222333444',
        'Note': 'Sample Note 1',
        'Gender': 'FeMale',
        'Date': '2010-11-02',
        'Address': 'No 4, Y'
    }

    sqlite_db_manager = SQLiteDBManager()

    sqlite_db_manager.getImageCount()

