"""
version: 1.0 (beta - for server purpose)
author : yash mathur (Themockingjester)
compatibility: linux , android
python3 version : 3.6.9
kivy module version: 1.11.1
pyrebase module version: 3.0.25

"""
import pyrebase
import datetime
from kivy.uix.gridlayout import GridLayout
from kivy.uix.checkbox import CheckBox
from kivymd.uix.bottomsheet import MDListBottomSheet
import shutil
import pandas as pd
import pytz
import requests
from kivymd.toast import toast
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivymd.icon_definitions import md_icons
from kivy.clock import Clock
from kivy.graphics.opengl import *
from kivy.graphics import *
from kivy.properties import ListProperty, ObjectProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivymd.uix.behaviors import TouchBehavior
import threading
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
import os,threading,time
from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton
try:
    from jnius import autoclass

    Environment = autoclass('android.os.Environment')
except:
    pass
from kivy.uix.behaviors import ButtonBehavior
class ImageButton(ButtonBehavior, Image):
    pass
config = {
    "apiKey": "AIzaSyBu62-6p7fwccVoFOlYZuaYPtMew1CaXmg",
    "authDomain": "chapters-adf11.firebaseapp.com",
    "databaseURL": "https://chapters-adf11.firebaseio.com",
    "projectId": "chapters-adf11",
    "storageBucket": "chapters-adf11.appspot.com",
    "messagingSenderId": "1069752858928",
    "appId": "1:1069752858928:web:273583bc6355ca54a6b0f5",
    "measurementId": "G-0PV8VMF6ZM",
}
class SignupWindow(BoxLayout):
    new_user_name = ObjectProperty(None)
    new_user_phonenumber = ObjectProperty(None)
    new_user_password = ObjectProperty(None)
    new_user_passwordretype = ObjectProperty(None)
    new_user_email = ObjectProperty(None)
class Cardforaddcontentsscreen(BoxLayout):
    contributor_name = ObjectProperty(None)
    file_contributor_email = ObjectProperty(None)
    file_address = ObjectProperty(None)
    date_of_upload = ObjectProperty(None)
    files_before_contribution = ObjectProperty(None)
    mode = ObjectProperty(None)
    money_status = ObjectProperty(None)
    reward_earned = ObjectProperty(None)
    transaction_number = ObjectProperty(None)
    indicator = ObjectProperty(None)
class PopupScreen_at_Addcontent(BoxLayout):
    pass
class MainWindow(BoxLayout):
    pass
class AddcontentsWindow(BoxLayout):
    result = ObjectProperty(None)

class UserchoiceWindow(BoxLayout):
    pass

class SigninWindow(BoxLayout):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    checkbox = ObjectProperty(None)
    keyring = ObjectProperty(None)
class ImageButtonWithDoubleTouch(ImageButton,TouchBehavior):
    def on_double_tap(self,instance,*args):
        ######### double tap pressed
        if 1==1:
            if self.parent.parent.parent.parent.indicator.source == "resources/icons/notadded.png":
                self.parent.parent.parent.parent.indicator.source = "resources/icons/added.png"
            else:
                self.parent.parent.parent.parent.indicator.source = "resources/icons/notadded.png"


class uiApp(MDApp):

    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if self.screen_manager.current == 'mainscreen':
                pass
            else:
                return True
    def build(self):
        try:
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.READ_EXTERNAL_STORAGE,Permission.WRITE_EXTERNAL_STORAGE])
        except:
            pass
        self.ctr = 0

        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Dark"  # "Light"
        firebase = pyrebase.initialize_app(config)
        self.storage = firebase.storage()
        self.database = firebase.database()
        self.auth = firebase.auth()
        self.get_details_using_email = False
        universal_version=None
        self.storage.child('version.txt').download('version.txt')  # download
        file = open("version.txt","r")
        file_content = file.read()
        file_content=file_content.split("\n")
        for i in file_content:
            if len(i)!=0:
                universal_version = i
        try:
            os.remove('version.txt')
        except:
            pass
        my_version="1.0"
        if my_version==universal_version:
            pass
        else:
            toast("update the app first")

            App.get_running_app().stop()            # closing the app
        try:
            shutil.rmtree(Environment.getExternalStorageDirectory().getAbsolutePath()+"/AckedmicServer/Downloads")       #cleaning server's download folder for android
        except:
            pass
        try:
            shutil.rmtree("/home/themockingjester/AckedmicServer/Downloads")                                             ##cleaning server's download folder for linux
        except:
            pass
        try:
            os.makedirs(Environment.getExternalStorageDirectory().getAbsolutePath()+"/AckedmicServer/Downloads")
            self.internal_storage = (Environment.getExternalStorageDirectory().getAbsolutePath())+"/AckedmicServer/Downloads"      # setting path for download in android
        except:
            os.makedirs("/home/themockingjester/AckedmicServer/Downloads")
            self.internal_storage = "/home/themockingjester/AckedmicServer/Downloads"            # setting path for download in linux

        self.screen_manager = ScreenManager()
        self.mainscreen = MainWindow()
        screen = Screen(name='mainscreen')
        screen.add_widget(self.mainscreen)
        self.screen_manager.add_widget(screen)

        self.signupscreen = SignupWindow()
        screen = Screen(name='signupscreen')
        screen.add_widget(self.signupscreen)
        self.screen_manager.add_widget(screen)

        self.signinscreen = SigninWindow()
        screen = Screen(name='signinscreen')
        screen.add_widget(self.signinscreen)
        self.screen_manager.add_widget(screen)

        self.userchoicescreen = UserchoiceWindow()
        screen = Screen(name='userchoicescreen')
        screen.add_widget(self.userchoicescreen)
        self.screen_manager.add_widget(screen)

        self.addcontentsscreen = AddcontentsWindow()
        screen = Screen(name='addcontentsscreen')
        screen.add_widget(self.addcontentsscreen)
        self.screen_manager.add_widget(screen)

        return self.screen_manager

    def verify_name(self,name):
        if len(name)!=0:
            if(str(name).isalpha()):
                return name
        return 'null'
    def verify_phone(self,phone):
        lis = ["+","0","1","2","3","4","5","6","7","8","9"]
        if len(str(phone))!=0:
            for i in str(phone):
                if i not in lis:
                    return "null"
            return phone
        return "null"

    def clicked_done_at_signinscreen(self):

        self.email = self.verify_email(self.signinscreen.email.text)

        password = str(self.signinscreen.password.text)
        if self.email=="null":
            toast("check your email")
            return 0
        if len(password)<6:
            toast("password length is small")
            return 0
        try:
            self.auth.sign_in_with_email_and_password(self.email,password)
            toast("Loading..")
        except:
            toast("Account doesn't exist")
            return 0
        self.storage.child('keyring.txt').download('ring.txt')  # download
        file = open("ring.txt", "r")
        keyring = file.read()
        file.close()
        os.remove('ring.txt')
        keyring = str(keyring).split()[0]

        if self.signinscreen.keyring.text == str(keyring):
            toast("welcome developer")
        else:
            toast("wrong keyring")
            return 0
        k = self.email_spliitter(self.email)
        record = self.database.child("users_record").child(k).get()
        self.name_of_user = record.val()["name"]

        if self.signinscreen.checkbox.active == True:               # if user wants to save id and password
            file = open("resources/usr/user.txt","w")
            file.write(self.email)
            file.write("\n")
            file.write(password)
            file.close()

        self.signinscreen_to_userchoicescreen()

    def content_for_verification_download(self,instance):
        curr_card = instance.parent.parent.parent.parent
        file = str(curr_card.file_address.text).replace("@","/")
        try:
            shutil.rmtree(self.internal_storage)        # cleaning server's download folder
        except:
            pass
        try:
            os.mkdir(self.internal_storage)         # making server download folder
        except:
            pass
        email = curr_card.file_contributor_email.text
        email = str(email).replace("contributor_email: ","",1)
        file = str(file).replace("content_for_verification/","content_for_verification/"+self.email_spliitter(email)+"/",1)     # fetching fileaddress from current card
        self.storage.child(file+".pdf").download(self.internal_storage+"/userfile.pdf")  # downloading file for paticular selected folder
        toast("downloaded")

    def show_popup_at_addcontentscreen_for_confirming_upload(self):
        show = PopupScreen_at_Addcontent()
        try:
            from jnius import autoclass             # checking if platform is android
            popup_size = 1000
        except:
            popup_size = 400
        self.popupWindow_at_addcontent = Popup(title="Popup Window", content=show, size_hint=(None, None), size=(popup_size,popup_size))

        self.popupWindow_at_addcontent.open()
    def close_popup_at_addcontentscreen_for_confirming_upload(self):
        self.popupWindow_at_addcontent.dismiss()
    def upload_current_files(self,instance):
        self.all_available_cards = instance.parent.parent.parent.parent.result.children
        self.show_popup_at_addcontentscreen_for_confirming_upload()

    def upload_current_files_part2(self):
        self.close_popup_at_addcontentscreen_for_confirming_upload()        # closing the popup

        for card in self.all_available_cards:           # iterating through the cards on add content window
            if card.indicator.source == "resources/icons/added.png":            # if check mark is available on that particular card
                email = card.file_contributor_email.text                # fetching email from current card
                email = str(email).replace("contributor_email: ", "", 1)    # filtering email
                name_of_contributor = str(card.contributor_name.text).replace("contributor_name: ", "", 1)      # fetching name of contributor from card
                file_address = card.file_address.text                                   # fetching file address on unverified server from card and also it is going to be used as path of file for verified server
                file_address = str(file_address).replace("@","/")                           # filtering file address
                try:
                    os.remove(self.internal_storage + "/userfile.pdf")                  # removing all available downloaded files first from server download folder
                except:
                    pass
                file = str(card.file_address.text).replace("@", "/")                # fetching file address on unverified server and it is going to be used as a file address for unverified server
                file = str(file).replace("content_for_verification/","content_for_verification/" + self.email_spliitter(email) + "/", 1)    # combining email with file address for unverified server

                self.storage.child(file + ".pdf").download(self.internal_storage + "/userfile.pdf")  # downloading contributor file for particular card
                real_database_path = file_address.replace("content_for_verification/","server_data/",1)
                real_database_path = real_database_path[0:-8]           # removing file name from path of file for verified server
                path_on_local = self.internal_storage + "/userfile.pdf"     # this variable will now hold  path for contributors's downloaded file

                full_path = real_database_path          # this variable will now hold path of file for verified server but in its path name of file will not be available
                self.storage.child(full_path + '/main.csv').download('main.csv')  # downloading csv file available at file path on verified server
                path1, dirs1, files = next(os.walk('.'))
                if 'main.csv' not in files:                         # if app doesn't receive any csv

                    #print('file_doesnnot_exist')

                    file = pd.DataFrame([[full_path + '/pdf_1.pdf', name_of_contributor, email]],columns=['path', 'submittedby', 'email'])
                    file.to_csv('main.csv', index=False)                            # making csv and adding contributor content to that csv
                    self.storage.child(full_path + '/pdf_1.pdf').put(path_on_local)  # uploading pdf file first
                    self.storage.child(full_path + '/main.csv').put('main.csv')  # uploading csv file later
                    # print('done uploading')
                    date = str(card.date_of_upload.text).replace("date_of_upload: ","",1)

                    transaction_mode = str(card.mode.text).replace("mode: ","",1)
                    transaction_mobile_number = str(card.transaction_number.text).replace("transaction_number: ","",1)
                    data = {'name': name_of_contributor, 'files_before_contribution': 0, 'mode': transaction_mode,
                            'transaction_number': transaction_mobile_number, "money_status": "not_sent",
                            "date of upload": date, "reward earned": 0}
                    k = str(card.file_contributor_email.text).replace("contributor_email: ","",1)
                    k = self.email_spliitter(k)
                    l = full_path + "/pdf_1"
                    l = l.replace("/", "@")
                    self.database.child("contributions_at_0").child(k).child(l).set(data)       # updating database at verified server
                    toast('fresh content uploaded')


                    try:
                        self.database.child("contributions_at_0_for_verification_copy").child(self.email_spliitter(email)).child(card.file_address.text).set(data)  # uploading copy of unverified database record
                        self.database.child("contributions_at_0_for_verification").child(self.email_spliitter(email)).child(card.file_address.text).remove()        # removing database record at unverified server

                    except:
                        pass
                    try:
                        # here no need to upload copy of unverified database record
                        self.database.child("contributions_for_verification").child(self.email_spliitter(email)).child(card.file_address.text).remove()             # removing database record at unverified server
                    except:
                        pass
                    ################################# approach for deleting content from storage of content_for_verificaton directory but not working ##################


                    # path = str(card.file_address.text).replace("@","/")
                    # path = path.replace("content_for_verification","content_for_verification/"+self.email_spliitter(email))
                    # path = path+".pdf"
                    # print(path)
                    # #path = papth[0:-8]
                    # path = path.split("/")
                    # print(path)
                    # self.storage.child(path[0]).child(path[1]).child(path[2]).child(path[3]).child(path[4]).child(path[5]).delete("pdffile.pdf")

                    ################################################### end ####################################################
                else:                   # if app receives a csv file
                    #print("received")
                    user_has_already_contributed = False
                    df = pd.read_csv('main.csv')
                    all_files_submitters_email = df["email"].tolist()               # getting all contributors email from that csv file
                    for k in all_files_submitters_email:
                        if k == str(card.file_contributor_email.text).replace("contributor_email: ","",1):          # if contributor email at current card has already present in csv
                            toast("you can't upload further your response already recorded")

                            try:
                                os.remove('main.csv')
                            except:
                                pass
                            user_has_already_contributed = True
                            break
                    if user_has_already_contributed == False:           # if current card contributor email is not present in csv
                        total_rows = len(df.axes[0])                #getting total rows in csv
                        current_file_number = total_rows + 1

                        transaction_mode = str(card.mode.text).replace("mode: ", "", 1)
                        transaction_mobile_number = str(card.transaction_number.text).replace("transaction_number: ","", 1)
                        # write out new rows

                        df2 = {'path': full_path + '/pdf_' + str(current_file_number) + '.pdf',
                               'submittedby': name_of_contributor, 'email': email}
                        df = df.append(df2, ignore_index=True)

                        df.to_csv('main.csv', index=False)

                        self.storage.child(full_path + '/pdf_' + str(current_file_number) + '.pdf').put(path_on_local)  # uploading pdf file first at file path  at verified server
                        self.storage.child(full_path + '/main.csv').put('main.csv')  # uploading csv file later at file path at verified server
                        # print('done uploading')
                        date = str(card.date_of_upload.text).replace("date_of_upload: ","",1)
                        data = {'name': name_of_contributor, 'files_before_contribution': total_rows,
                                'mode': transaction_mode,
                                'transaction_number': transaction_mobile_number, "money_status": "not_sent",
                                "date of upload": date, "reward earned": 0}
                        k = str(card.file_contributor_email.text).replace("contributor_email: ", "", 1)
                        k = self.email_spliitter(k)
                        l = full_path + "/pdf_" + str(current_file_number)
                        l = l.replace("/", "@")
                        self.database.child("contributions").child(k).child(l).set(data)        # updating database record at verified server
                        try:
                            os.remove('main.csv')       # removing downloaded csv
                        except:
                            pass
                        toast("uploaded")
                        try:
                            self.database.child("contributions_for_verification_copy").child(self.email_spliitter(email)).child(card.file_address.text).set(data)  # uploading copy of unverified database record
                            self.database.child("contributions_for_verification").child(self.email_spliitter(email)).child(card.file_address.text).remove()         # removing contributor database record at unverified server
                        except:
                            pass
                        try:
                            # here no need to upload copy of unverified database record
                            self.database.child("contributions_at_0_for_verification").child(self.email_spliitter(email)).child(card.file_address.text).remove()        # removing contributor database record at unverified server
                        except:
                            pass
        self.addcontentsscreen_to_userchoicescreen()            # coming back to userchoice window


    def fetch_new_content(self):                # fetching database content from unverified server
        self.addcontentsscreen.result.clear_widgets()       # removing previous cards
        people= self.database.child("contributions_at_0_for_verification").get()        # fetching all records from unverified server
        try:

            for person in people.each():
                name_of_user = str(person.key())
                content_of_user = self.database.child("contributions_at_0_for_verification").child(name_of_user).get()
                for content in content_of_user.each():
                    file_address = content.key()

                    metadata_for_content = self.database.child("contributions_at_0_for_verification").child(name_of_user).child(file_address).get()     # it will hold contributor file database record for
                    b = Cardforaddcontentsscreen()      # creating card for gui
                    b.date_of_upload.text = "date_of_upload: "+metadata_for_content.val()["date of upload"]
                    b.file_contributor_email.text = "contributor_email: "+name_of_user+"@gmail.com"
                    b.files_before_contribution.text = "files_before_contribution: "+str(metadata_for_content.val()["files_before_contribution"])
                    b.mode.text = "mode: "+metadata_for_content.val()["mode"]
                    b.money_status.text = "money_status: "+ metadata_for_content.val()["money_status"]
                    b.contributor_name.text = "contributor_name: "+metadata_for_content.val()["name"]
                    b.reward_earned.text = "reward_earned: "+str(metadata_for_content.val()["reward earned"])
                    b.transaction_number.text = "transaction_number: "+metadata_for_content.val()["transaction_number"]
                    b.file_address.text = file_address
                    self.addcontentsscreen.result.add_widget(b)
        except:
            pass
        try:
            people = self.database.child("contributions_for_verification").get()

            for person in people.each():
                name_of_user = str(person.key())
                content_of_user = self.database.child("contributions_for_verification").child(name_of_user).get()
                for content in content_of_user.each():
                    file_address = content.key()

                    metadata_for_content = self.database.child("contributions_for_verification").child(name_of_user).child(file_address).get()
                    b = Cardforaddcontentsscreen()
                    b.date_of_upload.text = "date_of_upload: " + metadata_for_content.val()["date of upload"]
                    b.file_contributor_email.text = "contributor_email: " + name_of_user + "@gmail.com"
                    b.files_before_contribution.text = "files_before_contribution: " + str(metadata_for_content.val()["files_before_contribution"])
                    b.mode.text = "mode: " + metadata_for_content.val()["mode"]
                    b.money_status.text = "money_status: " + metadata_for_content.val()["money_status"]
                    b.contributor_name.text = "contributor_name: " + metadata_for_content.val()["name"]
                    b.reward_earned.text = "reward_earned: " + str(metadata_for_content.val()["reward earned"])
                    b.transaction_number.text = "transaction_number: " + metadata_for_content.val()["transaction_number"]
                    b.file_address.text = file_address
                    self.addcontentsscreen.result.add_widget(b)
        except:
            pass
    def verify_email(self,email):
        if len(str(email)) != 0:
            if str(email).endswith("@gmail.com"):
                return email
        return "null"
    def email_spliitter(self,data):
        data = str(data)
        data = data.replace("@gmail.com","")
        #print(data)
        return data
    def clicked_done_at_signupscreen(self):
        newuser_name = self.verify_name(self.signupscreen.new_user_name.text)
        if newuser_name == "null":
            toast("check name properly")
            return  0
        newuser_phone = self.verify_phone(self.signupscreen.new_user_phonenumber.text)
        if newuser_phone == "null":
            toast("check phonenumber properly")
            return 0

        newuser_email = str(self.verify_email(self.signupscreen.new_user_email.text))

        if newuser_email == "null":
            toast("check email properly")
            return 0
        newuser_password = self.signupscreen.new_user_password.text
        if len(str(newuser_password))==0 and len(str(newuser_password))<6:
            toast("check password properly")
            return 0
        newuser_passwordretype = self.signupscreen.new_user_passwordretype.text
        if len(str(newuser_passwordretype))==0:
            toast("both passwords doesn't match")
            self.signupscreen.new_user_passwordretype.text = ""
            self.signupscreen.new_user_password.text = ""
            return 0


        if newuser_passwordretype == newuser_password:              # checking if both passwords are equal or not
            try:


                self.auth.create_user_with_email_and_password(newuser_email, newuser_password)



                res = requests.get("https://ipinfo.io/")                # accessing current user ip
                info = res.json()
                country = info['country']
                country_name = pytz.country_names[country]
                #print(country_name)
                date = str(datetime.date.today())
                data = {'name': newuser_name, 'phone': newuser_phone, "password": newuser_password,
                        "country": country_name,"date of joining" : date}
                k = self.email_spliitter(newuser_email)
                self.database.child("users_record").child(k).set(data)
                data2 = {'reward earned':0}
                self.database.child("users_rewards").child(k).set(data2)


                toast("Account created")
                self.signupscreen_to_mainscreen()
                return 0
            except:

                toast("something wrong with this email!!")
                return 0
        else:

            toast("both passwords doesn't match!!")



    def signinscreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'right'

        self.screen_manager.current = 'mainscreen'
    def mainscreen_to_signinscreen(self):
        self.screen_manager.transition.direction = 'left'

        self.screen_manager.current = 'signinscreen'
        try:
            file = open("resources/usr/user.txt","r")
            k = file.readline()
            k = k.split("\n")

            for j in k :
                if len(j)>8:
                    k = j
            self.signinscreen.email.text = k
            self.signinscreen.password.text = file.readline()
        except:
            pass
    def signinscreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'up'

        self.screen_manager.current = 'userchoicescreen'
    def userchoicescreen_to_signinscreen(self):
        self.screen_manager.transition.direction = 'down'
        self.email = ""
        self.name_of_user = ""
        self.screen_manager.current = 'signinscreen'
    def userchoicescreen_to_addcontentsscreen(self):
        self.screen_manager.transition.direction = 'left'

        self.screen_manager.current = 'addcontentsscreen'
        self.fetch_new_content()
    def addcontentsscreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'right'

        self.screen_manager.current = 'userchoicescreen'

    def mainscreen_to_signupscreen(self):
        self.screen_manager.transition.direction = 'left'

        self.screen_manager.current = 'signupscreen'
    def signupscreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'mainscreen'




if __name__ == '__main__':
    LabelBase.register(name='second',fn_regular='resources/fonts/FFF_Tusj.ttf')
    LabelBase.register(name='first',fn_regular='resources/fonts/Pacifico.ttf')


    uiApp().run()
