from tkinter import messagebox

from StorageManager import DBManager, FileManager
import InternetConnection
from PIL import Image
Image.LOAD_TRUNCATED_IMAGES = True

def find_object_id_by_name(name, firebase_manager):
    all_data = firebase_manager.getAllData()
    found = False
    for id in all_data:

        if(all_data[id]['Name'] == name):
            found = True
            break;
    if (found):
        return id
    else:
        return None

def update_feature_by_name(name, data):

    firebase_manager = DBManager.FirebaseDBManager()
    id = find_object_id_by_name(name, firebase_manager)

    if(id != None):
        firebase_manager.update(id, 'Name', data['Name'])
        firebase_manager.update(id, 'Phone', data['Phone'])
        firebase_manager.update(id, 'Note', data['Note'])
        firebase_manager.update(id, 'Gender', data['Gender'])
        firebase_manager.update(id, 'Address', data['Address'])
    else:
        messagebox.showwarning("Not found",
                               "Name Not Found!!")

def delete_feature_by_name(name):

    firebase_manager = DBManager.FirebaseDBManager()
    id = find_object_id_by_name(name, firebase_manager)

    if(id != None):
        firebase_manager.delete(id)

        try:
            fileManager = FileManager.FileManager()
            fileManager.remove_from_remote(id)
        except:
            print("")
    else:
        messagebox.showwarning("Not found",
                               "Name Not Found!!")

def synachronize_sqlite_with_firebase():
    if (InternetConnection.is_connected_to_network()):
        firebaseDBManager = DBManager.FirebaseDBManager()
        all_data = firebaseDBManager.getAllData()

        sqlitebaseDBManager = DBManager.SQLiteDBManager()
        if (all_data != None):
            for id in all_data:
                data, existence = verify_item_existence_in_sqlite(id)
                # break;
                if (not existence):

                    temp_dict = all_data[id]
                    temp_dict['ID'] = id
                    sqlitebaseDBManager.insert(temp_dict)

                    fileManager = FileManager.FileManager()
                    fileManager.download(id)

                if (existence):
                    dict_firebase = all_data[id]
                    dict_firebase['ID'] = id

                    # sqlitebaseDBManager = DBManager.SQLiteDBManager()
                    dict_sqlite, existence = sqlitebaseDBManager.getSpecificData(id)

                    # dict_sqlite = convert_to_dict(data_sqlite)

                    compare_two_dictionaries(dict_firebase, dict_sqlite)

                    fileManager = FileManager.FileManager()
                    fileManager.download(id)

            for sqlite_data_id in sqlitebaseDBManager.getAllIDs():

                try:
                    if sqlite_data_id not in all_data.keys():
                        sqlitebaseDBManager.delete(sqlite_data_id)

                        fileManager = FileManager.FileManager()
                        fileManager.remove_from_local(sqlite_data_id)

                except:
                    print("")
        else:
            for sqlite_data_id in sqlitebaseDBManager.getAllIDs():
                try:
                    sqlitebaseDBManager.delete(sqlite_data_id)
                    fileManager = FileManager.FileManager()
                    fileManager.remove_from_local(sqlite_data_id)

                except:
                    print("")

def verify_item_existence_in_sqlite(id):
    sqlitebaseDBManager = DBManager.SQLiteDBManager()
    data, existence = sqlitebaseDBManager.getSpecificData(id)
    return data, existence

def compare_two_dictionaries(dict_firebase, dict_sqlite):
    if(dict_firebase == dict_sqlite):

        return
    else:
        sqlitebaseDBManager = DBManager.SQLiteDBManager()
        sqlitebaseDBManager.update(dict_sqlite['ID'], 'Name', dict_firebase['Name'])
        sqlitebaseDBManager.update(dict_sqlite['ID'], 'Phone', dict_firebase['Phone'])
        sqlitebaseDBManager.update(dict_sqlite['ID'], 'Note', dict_firebase['Note'])
        sqlitebaseDBManager.update(dict_sqlite['ID'], 'Gender', dict_firebase['Gender'])
        sqlitebaseDBManager.update(dict_sqlite['ID'], 'Date', dict_firebase['Date'])
        sqlitebaseDBManager.update(dict_sqlite['ID'], 'Address', dict_firebase['Address'])

def convert_to_dict(data):
    temp_dict = {}
    for record in data:
        temp_dict['ID'] = str(record[0])
        temp_dict['Name'] = str(record[1])
        temp_dict['Phone'] = str(record[2])
        temp_dict['Note'] = str(record[3])
        temp_dict['Gender'] = str(record[4])
        temp_dict['Date'] = str(record[5])
        temp_dict['Address'] = str(record[6])

    return temp_dict

def get_dictionary_of_single_results_row(data_dictionary):
    return data_dictionary


def get_selected_image(name):
    sqliteManager = DBManager.SQLiteDBManager()
    id_dict, exist = sqliteManager.getSpecificDataFromName(name)

    if (exist == 1):
        path = "./images/"+id_dict['ID']+"/image.jpg"
        im = Image.open(path)

        width = 300
        wpercent = (width / float(im.size[0]))
        hsize = int((float(im.size[1]) * float(wpercent)))
        newsize = (width, hsize)
        im = im.resize(newsize)
        im.show()

def inquiry_data(data):
    firebaseDBManager = DBManager.FirebaseDBManager()
    all_data = firebaseDBManager.getAllData()

    equal = False
    for id in all_data:
        dict_firebase = all_data[id]

        new_dict = {'Name':dict_firebase['Name'], 'Phone':dict_firebase['Phone'], 'Note':dict_firebase['Note'],
                    'Gender':dict_firebase['Gender'], 'Date':dict_firebase['Date'], 'Address':dict_firebase['Address']
                    }

        if(data == new_dict):
            equal = True

    return equal

def get_no_of_images():
    sqliteManager = DBManager.SQLiteDBManager()
    count = sqliteManager.getImageCount()
    return count