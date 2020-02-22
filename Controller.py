import DBManager
import FileManager
import InternetConnection
import DBManager

def find_object_id_by_name(name, firebase_manager):

    all_data = firebase_manager.getAllData()

    print(all_data)
    for id in all_data:
        # print(x)
        if(all_data[id]['Name'] == name):
            break;

    print(id)
    return id


def update_feature_by_name(name, data):

    firebase_manager = DBManager.FirebaseDBManager()
    id = find_object_id_by_name(name, firebase_manager)

    firebase_manager.update(id, 'Name', data['Name'])
    firebase_manager.update(id, 'Phone', data['Phone'])
    firebase_manager.update(id, 'Note', data['Note'])
    firebase_manager.update(id, 'Gender', data['Gender'])
    firebase_manager.update(id, 'Address', data['Address'])

def delete_feature_by_name(name):

    firebase_manager = DBManager.FirebaseDBManager()
    id = find_object_id_by_name(name, firebase_manager)

    firebase_manager.delete(id)

def synachronize_sqlite_with_firebase():
    firebaseDBManager = DBManager.FirebaseDBManager()
    all_data = firebaseDBManager.getAllData()
    # print(all_data)
    sqlitebaseDBManager = DBManager.SQLiteDBManager()
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
            # print("E")

    # print("------------")
    # print()
    # print(all_data.keys())
    for sqlite_data_id in sqlitebaseDBManager.getAllIDs():

        if sqlite_data_id not in all_data.keys():
            sqlitebaseDBManager.delete(sqlite_data_id)
            # print("Deleted"+ sqlite_data_id)

def verify_item_existence_in_sqlite(id):
    sqlitebaseDBManager = DBManager.SQLiteDBManager()
    data, existence = sqlitebaseDBManager.getSpecificData(id)
    return data, existence

def compare_two_dictionaries(dict_firebase, dict_sqlite):
    if(dict_firebase == dict_sqlite):
        # print("Yeah!")
        # print(dict_firebase)
        # print(dict_sqlite)
        return
    else:
        # print('Nah!')
        # print(dict_firebase)
        # print(dict_sqlite)

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

# synachronize_sqlite_with_firebase()
