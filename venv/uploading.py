#
# import firebase_admin
# from firebase_admin import credentials
#
# cred = credentials.Certificate("resources/chapters-adf11-firebase-adminsdk-64rx8-cafbf99e63.json")
# firebase_admin.initialize_app(cred)

import pyrebase
config = {
    "apiKey": "AIzaSyBu62-6p7fwccVoFOlYZuaYPtMew1CaXmg",
    "authDomain": "chapters-adf11.firebaseapp.com",
    "databaseURL": "https://chapters-adf11.firebaseio.com",
    "projectId": "chapters-adf11",
    "storageBucket": "chapters-adf11.appspot.com",
    "messagingSenderId": "1069752858928",
    "appId": "1:1069752858928:web:273583bc6355ca54a6b0f5",
    "measurementId": "G-0PV8VMF6ZM"

}
firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

path_on_cloud = 'pdf_files/text.wav'
path_on_local = '/home/themockingjester/540387__eldiariosonoro__abrir-ventana-g5-open-window.wav'
path_after_download = '/home/themockingjester/downlo-aded.wav'
# storage.child(path_on_cloud).put(path_on_local) #uploading
# print('uploaded')
storage.child(path_on_cloud).download(path_after_download) #download
print('downloaded')


