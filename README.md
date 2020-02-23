# profile-data-collector

How to setup firebase:

## 1. Create new Database:

    * Visit firebase: https://firebase.google.com/
    
    * Give your credentials and log in
    
    * Click 'Go to Console' on upper corner of RHS
    
    * Click 'Create a Project' (If you do not have one), give the project name and follow steps to complete project creation
    
    * Click Develop->Database from LHS side-bar
    
    * Click 'Create database' (for testing use 'Start in test mode') and complete steps to create DB
    
    * Change database type to 'Realtime Database' (from 'Cloud Firestore')
    
    * Copy the URL and paste it to StorageManager/DBManager.py DB_URL variable. Update DB_Name accordingly
    
    * Click 'Rules' and make ".read":true and ".write:true"

## 2. Create new Storage
    
    * From previous window LHS side-bar click Storage
    
    * Click 'Get Started', follow steps and create the Storage

## 3. To get the 'config' variable for StorageManager/FileManager.py:

    * Go to 'Settings -> General'
    
    * Create an App by clicking to add an App (Web App)
    
    * Give an App name and Click register App. Give a name and complete app creation (by registering).
    
    * In 'Add Firebase SDK section' copy the variable called firebaseConfig 
    
    * Set this value as the Config variable of StorageManager/FileManager.py 
        
        StorageManager/FileManager.py -> config 
        
        
    * Close the App adding section sub window

## 4. To set 'config_for_storage' variable for StorageManager/FileManager.py:

    * Go to Settings->'Service accounts' 
    
    * Select the language (Python)
    
    * Click 'Generate new private key' and it will generate and download a json file
    
    * Copy the 'config' variable from previous section, paste in StorageManager/FileManager.py and rename as 'config_for_storage'
    
        StorageManager/FileManager.py -> config_for_storage
    
    * Add new "serviceAccount" variable into 'config_for_storage' variable and path of the generated (downloaded) .json file set as the value of "serviceAccount"



## Functions provided and description of UI

Can do refresh, edit firebase, remove from firebase, save to firebase, load images, inquiry and exit operations

    Add - Refresh and clear fields to make a new entry
    
    Edit - Edit data (which stored in firebase)
    
    Del - Delete data (which stored in firebase)
    
    Save - Save all the input profile data and loaded image (Directly to firebase)
    
    New Photo - Uses to load an image 
    
    Inquiry - Use to make inquiries
    
    Exit - Use to exit the application
    
    Table elements - Table rows with images can click to view images in large scale



   
  




