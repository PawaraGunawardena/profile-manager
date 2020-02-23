# profile-data-collector

How to setup firebase:

##1. Create new Database:

* Visit firebase: https://firebase.google.com/

* Give your credentials and log in

* Click Console on upper corner of RHS

* Click Add Project (If you do not have one)

* Click Database from LHS side-bar

* Create a new Database

* Copy the URL and paste it to StorageManager/DBManager.py DB_URL variable. Update DB_Name accordingly

##2. Create new Storage

* From previous window LHS side-bar click Storage

* Follow steps and create the Storage

##3. To get the 'config' variable for StorageManager/FileManager.py:

* Visit firebase: https://firebase.google.com/

* Give your credentials and log in

* Click Console on upper corner of RHS

* Click on the project name

* Click to add an App (Web App)

* Give an App name and Click register App

* Copy the variable called firebaseConfig 

* Set this value as the Config variable of StorageManager/FileManager.py

* Close the window

* After App creation Settings of firebase also shows the config variable under the App created

##4. To set 'config_for_storage' variable for StorageManager/FileManager.py:

* Go to settings

* Click Service accounts bar

* Select the language (Python)

* Click 'Generate new private key' and it will generate and download a json file

* Copy the 'config' variable from previous section, paste in StorageManager/FileManager.py and rename as 'config_for_storage'

* Add new "serviceAccount" and path to generated .json file set as the value of "serviceAccount"



## Functions provided and description of UI

Can refresh, edit firebase, remove rom firebase, save to firebase, load images, Inquiry and exit

Add - Refresh and clear fields to make a new entry
Edit - Edit data (which stored in firebase)
Del - Delete data (which stored in firebase)
Save - Save all the input profile data and loaded image (Directly to firebase)
New Photo - Uses to load an image 
Inquiry - Use to make inquiries
Exit - Use to exit the application
Table elements - Table rows with images can click to view images in large scale



   
  




