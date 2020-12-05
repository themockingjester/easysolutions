"""
version: 1.0 (alpha - for release)
author : yash mathur (Themockingjester)
compatibility: linux , android
python3 version : 3.6.9
kivy module version: 1.11.1

"""
import pyrebase
import datetime

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
    "measurementId": "G-0PV8VMF6ZM"

}

class SignupWindow(BoxLayout):
    new_user_name = ObjectProperty(None)
    new_user_phonenumber = ObjectProperty(None)

    new_user_password = ObjectProperty(None)
    new_user_passwordretype = ObjectProperty(None)
    new_user_email = ObjectProperty(None)
class FileLoader(BoxLayout):
    filechooser = ObjectProperty(None)
class MainWindow(BoxLayout):
    pass
class SearchlessonsWindow(BoxLayout):
    publisher_name = ObjectProperty(None)
    class_ = ObjectProperty(None)
    book_name = ObjectProperty(None)
    lesson_name = ObjectProperty(None)
class ContributeWindow(BoxLayout):
    transaction_mode = ObjectProperty(None)
    transaction_mobile_number = ObjectProperty(None)
    publisher_name = ObjectProperty(None)
    lesson_name = ObjectProperty(None)
    class_for_pdf = ObjectProperty(None)
    book_name = ObjectProperty(None)
    donebutton = ObjectProperty(None)
class UserchoiceWindow(BoxLayout):
    pass
class RewardsWindow(BoxLayout):
    balance = ObjectProperty(None)
class SigninWindow(BoxLayout):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    checkbox = ObjectProperty(None)
class LoadingWindow(BoxLayout):
    loadingimage1 = ObjectProperty(None)
    loadingimage2 = ObjectProperty(None)
    loadingimage3 = ObjectProperty(None)

class SearchResultWindow(BoxLayout):
    lay = ObjectProperty(None)
class MyWid(BoxLayout):
    one = ObjectProperty(None)
    two = ObjectProperty(None)
    three = ObjectProperty(None)
    four = ObjectProperty(None)
    five = ObjectProperty(None)
    six = ObjectProperty(None)
class MyWid2(BoxLayout):
    one = ObjectProperty(None)
    two = ObjectProperty(None)
    three = ObjectProperty(None)
    four = ObjectProperty(None)
    five = ObjectProperty(None)
    six = ObjectProperty(None)
    seven = ObjectProperty(None)
class ShowResult(BoxLayout):
    lay = ObjectProperty(None)
class SettingsWindow(BoxLayout):
    remove_saved_login = ObjectProperty(None)
    storage_path = ObjectProperty(None)
class uiApp(MDApp):
    try:
        internalstorage = (Environment.getExternalStorageDirectory().getAbsolutePath())
    except:
        internalstorage = "/"
    def on_start(self):
        from kivy.base import EventLoop
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)

    def hook_keyboard(self, window, key, *largs):
        if key == 27:
            if self.screen_manager.current == 'mainscreen' or self.screen_manager.current == 'userchoicescreen':
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
        try:
            downloading_path = "files_meta_info/"
            shutil.rmtree(downloading_path)
        except:
            pass
        self.theme_cls.primary_palette = "Pink"
        self.theme_cls.theme_style = "Dark"  # "Light"
        self.stop_load = True
        self.file = ""
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
        try:
            os.mkdir((Environment.getExternalStorageDirectory().getAbsolutePath() + '/AckedmicDownloads'))
        except:
            pass
        try:
            os.makedirs("resources/files")
        except:
            pass
        path_of_resources = "resources/files/"
        if os.path.exists(path_of_resources+"settings.txt"):
            pass
        else:
            try:
                storing_path = (Environment.getExternalStorageDirectory().getAbsolutePath() + '/AckedmicDownloads')
            except:
                storing_path = "/home/themockingjester"
            file = open(path_of_resources+"settings.txt","w")
            file.write("0,")
            file.write(storing_path)
            file.write("\n")
            file.close()

        f = open(path_of_resources+"settings.txt","r")
        self.settings_file_contents = f.read()
        f.close()
        self.settings_file_contents = self.settings_file_contents.split(",")
        self.screen_manager = ScreenManager()
        self.mainscreen = MainWindow()
        screen = Screen(name='mainscreen')
        screen.add_widget(self.mainscreen)
        self.screen_manager.add_widget(screen)
        self.stoploading = False
        self.signupscreen = SignupWindow()
        screen = Screen(name='signupscreen')
        screen.add_widget(self.signupscreen)
        self.screen_manager.add_widget(screen)

        self.loadingscreen = LoadingWindow()
        screen = Screen(name='loadingscreen')
        screen.add_widget(self.loadingscreen)
        self.screen_manager.add_widget(screen)

        self.searchresultscreen = SearchResultWindow()
        screen = Screen(name='searchresultscreen')
        screen.add_widget(self.searchresultscreen)
        self.screen_manager.add_widget(screen)

        self.searchlessonsscreen = SearchlessonsWindow()
        screen = Screen(name='searchlessonsscreen')
        screen.add_widget(self.searchlessonsscreen)
        self.screen_manager.add_widget(screen)

        self.signinscreen = SigninWindow()
        screen = Screen(name='signinscreen')
        screen.add_widget(self.signinscreen)
        self.screen_manager.add_widget(screen)

        self.userchoicescreen = UserchoiceWindow()
        screen = Screen(name='userchoicescreen')
        screen.add_widget(self.userchoicescreen)
        self.screen_manager.add_widget(screen)

        self.contributescreen = ContributeWindow()
        screen = Screen(name='contributescreen')
        screen.add_widget(self.contributescreen)
        self.screen_manager.add_widget(screen)

        self.fileloaderscreen = FileLoader()
        screen = Screen(name='fileloaderscreen')
        screen.add_widget(self.fileloaderscreen)
        self.screen_manager.add_widget(screen)

        self.showresultscreen = ShowResult()
        screen = Screen(name='showresultscreen')
        screen.add_widget(self.showresultscreen)
        self.screen_manager.add_widget(screen)

        self.rewardsscreen = RewardsWindow()
        screen = Screen(name='rewardsscreen')
        screen.add_widget(self.rewardsscreen)
        self.screen_manager.add_widget(screen)

        self.settingsscreen = SettingsWindow()
        screen = Screen(name='settingsscreen')
        screen.add_widget(self.settingsscreen)
        self.screen_manager.add_widget(screen)
        if self.settings_file_contents[0]=="1":
            self.settingsscreen.remove_saved_login.active = True
        else:
            self.settingsscreen.remove_saved_login.active = False
        self.settingsscreen.storage_path.text = "0"  #self.settings_file_contents[1]
        if self.settings_file_contents[0]=="1":
            try:
                os.remove("resources/usr/user.txt")
            except:
                pass


        return self.screen_manager
    def settings_reset(self):
        path_of_resources = "resources/files/"
        file = open(path_of_resources + "settings.txt", "w")
        file.write("0,")
        file.write(self.settings_file_contents[1])
        file.write("\n")
        file.close()
        self.settingsscreen.remove_saved_login.active = False
    def save_settings(self):
        path_of_resources = "resources/files/"
        file = open(path_of_resources + "settings.txt", "w")
        if self.settingsscreen.remove_saved_login.active == False:
            file.write("0,")
        else:
            file.write("1,")
            try:
                os.remove("resources/usr/user.txt")
            except:
                pass
        file.write(self.settings_file_contents[1])
        file.write("\n")
        file.close()
    def callback_for_menu_items(self, *args):
        self.contributescreen.transaction_mode.text = args[0]

    def show_transaction_mode_list_bottom_sheet(self):
        bottom_sheet_menu = MDListBottomSheet(radius_from="top_right",radius=45)
        lis = ["google pay","paytm"]
        for i in lis:
            bottom_sheet_menu.add_item(
                f"{i}",
                lambda x, y=i: self.callback_for_menu_items(
                    f"{y}"
                ),
            )
        bottom_sheet_menu.open()

    def load(self, path, filename):

        self.file = filename
        self.file = self.file[0]

        self.fileloaderscreen_to_contributescreen()
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
        k = self.email_spliitter(self.email)
        record = self.database.child("users_record").child(k).get()
        self.name_of_user = record.val()["name"]

        if self.signinscreen.checkbox.active == True:
            file = open("resources/usr/user.txt","w")
            file.write(self.email)
            file.write("\n")
            file.write(password)
            file.close()

        self.signinscreen_to_userchoicescreen()
    def clicked_done_at_searchlessonsscreen(self):
        publisher = str(self.searchlessonsscreen.publisher_name.text)
        if len(publisher) == 0:
            toast("check publisher name")
            return 0
        if "." in publisher:
            toast("remove . from publisher")
            return 0
        class_ = str(self.searchlessonsscreen.class_.text)
        try:
            class_to_int = int(class_)
        except:
            toast("check class properly")
            return 0

        if class_to_int > 0 and class_to_int < 13:
            pass

        else:
            toast("check class properly")
            return 0
        try:
            del class_to_int
        except:
            pass
        bookname = str(self.searchlessonsscreen.book_name.text)
        if len(bookname) == 0:
            toast("check book name")
            return 0
        if "." in publisher:
            toast("remove . from book name")
            return 0
        lesson = str(self.searchlessonsscreen.lesson_name.text)
        if len(lesson) == 0:
            toast("check lesson name properly")
            return 0
        if "." in lesson:
            toast("remove . from lesson")
            return 0
        try:
            new_folder = "files_meta_info/"
            os.mkdir(new_folder)
        except:
            pass
        full_path = "server_data/"+publisher+"/"+class_+"/"+bookname+"/"+lesson+"/"  ##  path on server
        path_on_local = "files_meta_info/"
        self.searchlessonsscreen_to_searchresultsscreen()
        self.addcontent_to_seachresultscreen(path_on_local,full_path)
    def addcontent_to_seachresultscreen(self,path_on_local, full_path):
        self.storage.child(full_path + 'main.csv').download(path_on_local+'main.csv')  # download
        path1, dirs1, files = next(os.walk(path_on_local))
        self.searchresultscreen.lay.clear_widgets()
        if 'main.csv' not in files:  # if no such file exist on server

            toast('file doesn\'t exist')

        else:

            df = pd.read_csv(path_on_local+'main.csv')
            all_files_names = df["path"].tolist()
            all_files_submitters = df["submittedby"].tolist()
            all_files_submitters_email = df["email"].tolist()

            for i in range(len(all_files_names)):
                k = all_files_names[i]
                k = str(k).split("/")
                card = MyWid2()
                card.one.text = "Publisher: "+str(k[1])
                card.two.text = "Class: " + str(k[2])
                card.seven.text = "Book Name: " + str(k[3])  # correct
                card.three.text = "Lesson name: "+str(k[4])
                card.six.text = "File name: "+str(k[5])
                card.four.text = "Submitted By: "+str(all_files_submitters[i])
                card.five.text = "Submitter Email: "+str(all_files_submitters_email[i])
                self.searchresultscreen.lay.add_widget(card)
            toast("completely loaded!!")
            try:
                os.remove(path_on_local+'main.csv')

            except:
                pass
    def download(self,instance):


        publisher = instance.parent.parent.parent.one.text
        publisher = str(publisher).replace("Publisher: ","",1)
        class_ = instance.parent.parent.parent.two.text
        class_ = str(class_).replace("Class: ","",1)
        bookname = instance.parent.parent.parent.seven.text
        bookname = str(bookname).replace("Book Name: ","",1)
        lesson = instance.parent.parent.parent.three.text
        lesson = str(lesson).replace("Lesson name: ","",1)
        filename = instance.parent.parent.parent.six.text
        filename = str(filename).replace("File name: ","",1)
        try:
            os.makedirs(
                Environment.getExternalStorageDirectory().getAbsolutePath() + '/AckedmicDownloads/' + publisher + "/" + class_ + "/" + bookname +"/" + lesson)
        except:
            pass
        try:
            os.makedirs(
                "/home/themockingjester" + '/AckedmicDownloads/' + publisher + "/" + class_ + "/" + bookname + "/" + lesson)
        except:
            pass

        try:
            path_on_local = (Environment.getExternalStorageDirectory().getAbsolutePath() + '/AckedmicDownloads/' + publisher + "/" + class_ + "/"  + bookname +"/" + lesson+"/")
        except:
            path_on_local = "/home/themockingjester"+ '/AckedmicDownloads/' + publisher + "/" + class_ + "/"  + bookname +"/" + lesson+"/"
        address_on_database = "server_data/"+str(publisher)+'/'+str(class_)+'/'+ str(bookname)+"/"+str(lesson)+'/'+filename
        try:

            self.storage.child(address_on_database).download(path_on_local + filename)  # download

            toast("Downloaded in phone AckedmicDownloads folder")
        except:
            toast("Something wrong happened!!")
    def clicked_done_at_contributescreen(self):

        publisher = str(self.contributescreen.publisher_name.text)
        if len(publisher)==0:
            toast("check publisher name")
            return 0
        if "." in publisher:
            toast("remove . from publisher")
            return 0
        class_ = str(self.contributescreen.class_for_pdf.text)
        try:
            class_to_int =int(class_)
        except:
            toast("check class properly")
            return 0

        if class_to_int > 0 and class_to_int < 13:
            pass

        else:
            toast("check class properly")
            return 0
        try:
            del class_to_int
        except:
            pass
        lesson = str(self.contributescreen.lesson_name.text)
        if len(lesson)==0:
            toast("check lesson name properly")
            return 0
        if "." in lesson:
            toast("remove . from lesson")
            return 0
        if self.file == "":
            toast("select file first")
            return 0
        bookname = str(self.contributescreen.book_name.text)
        if len(bookname)==0:
            toast("check bookname name")
            return 0
        if "." in bookname:
            toast("remove . from bookname")
            return 0
        transaction_mobile_number = str(self.contributescreen.transaction_mobile_number.text)
        transaction_mobile_number = self.verify_phone(transaction_mobile_number)
        if transaction_mobile_number == "null":
            toast("enter transaction number properly")
            return 0

        if self.contributescreen.transaction_mode.text not in ["paytm","google pay"]:
            toast("select transaction mode")
            return 0
        self.contributescreen.donebutton.disabled = True
        path_on_server = publisher + "/" + class_ + "/" + bookname + "/" + lesson + "/"
        #content_for_verification=self.email+"/"+publisher + "/" + class_ + "/" + bookname + "/" + lesson
        path_on_local = self.file
        transaction_mode = self.contributescreen.transaction_mode.text
        self.upload(path_on_local,path_on_server,transaction_mode,transaction_mobile_number)
    def upload(self,path_on_local, full_path,transaction_mode,transaction_mobile_number):
        verification_file_path = "content_for_verification/"+self.email_spliitter(self.email)+"/"+full_path+"pdffile"
        path_for_storing_in_contribution = "content_for_verification/"+full_path+"pdffile"

        full_path = "server_data/"+full_path

        self.storage.child(full_path + 'main.csv').download('main.csv')  # download
        path1, dirs1, files = next(os.walk('.'))
        if 'main.csv' not in files:  # if no such file exist on server

            #print('file_doesnnot_exist')
            self.storage.child(verification_file_path+".pdf").put(path_on_local)  # uploading pdf file first

            #print('done uploading')
            date = str(datetime.date.today())
            data = {'name': self.name_of_user, 'files_before_contribution': 0, 'mode': transaction_mode ,
                    'transaction_number': transaction_mobile_number, "money_status": "not_sent","date of upload":date,"reward earned":0}
            k = self.email_spliitter(self.email)
            l = path_for_storing_in_contribution
            l = l.replace("/","@")
            self.database.child("contributions_at_0_for_verification").child(k).child(l).set(data)
            toast('fresh content uploaded for verification')
        else:


            df = pd.read_csv('main.csv')
            all_files_submitters_email = df["email"].tolist()
            for k in all_files_submitters_email:
                if k == str(self.email):
                    toast("you can't upload further your response already recorded")
                    self.contributescreen.donebutton.disabled = False
                    try:
                        os.remove('main.csv')
                    except:
                        pass
                    return 0

            total_rows = len(df.axes[0])
            current_file_number = total_rows + 1




            self.storage.child(verification_file_path+".pdf").put(path_on_local)  # uploading pdf file first

            #print('done uploading')
            date = str(datetime.date.today())
            data = {'name': self.name_of_user, 'files_before_contribution': total_rows, 'mode': transaction_mode,
                    'transaction_number': transaction_mobile_number, "money_status": "not_sent","date of upload":date,"reward earned":0}
            k = self.email_spliitter(self.email)
            l = path_for_storing_in_contribution
            l = l.replace("/", "@")
            self.database.child("contributions_for_verification").child(k).child(l).set(data)
            try:
                os.remove('main.csv')
            except:
                pass
            toast("uploaded for verification")

        self.contributescreen.donebutton.disabled = False

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

        # data = {'username': newuser_username}
        # self.database.child("usernames").push(data)
        if newuser_passwordretype == newuser_password:
            try:


                self.auth.create_user_with_email_and_password(newuser_email, newuser_password)



                res = requests.get("https://ipinfo.io/")
                info = res.json()
                country = info['country']
                country_name = pytz.country_names[country]

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
    def dataloading_at_showresultscreen_from_mycontributionhistoryscreen(self):
        k = self.email_spliitter(self.email)
        check_for_contribution = 0
        try:
            records = self.database.child("contributions").child(k).get()
            for n in records.each():
                data_in_records = self.database.child("contributions").child(k).child(n.key()).get()
                date = str(data_in_records.val()["date of upload"])
                file = str(n.key())
                file = file.split("@")
                b = MyWid()

                b.one.text = "publisher: "+file[1]
                b.two.text = "class: " + file[2]
                b.six.text = "book name: " + file[3]     #correct
                b.three.text = "lesson name: "+file[4]
                b.four.text = "file name: " + file[5]+".pdf"
                b.five.text = "date of upload: " + date

                self.showresultscreen.lay.add_widget(b)
        except:
            check_for_contribution +=1
        try:
            records = self.database.child("contributions_at_0").child(k).get()
            for n in records.each():
                data_in_records = self.database.child("contributions_at_0").child(k).child(n.key()).get()
                date = str(data_in_records.val()["date of upload"])
                file = str(n.key())
                file = file.split("@")
                b = MyWid()

                b.one.text = "publisher: " + file[1]
                b.two.text = "class: " + file[2]
                b.six.text = "book name: " + file[3]  # correct
                b.three.text = "lesson name: " + file[4]
                b.four.text = "file name: " + file[5] + ".pdf"
                b.five.text = "date of upload: " + date
                self.showresultscreen.lay.add_widget(b)
        except:
            check_for_contribution += 1
        if check_for_contribution == 2:
            toast("you havn't contributed yet")
            self.mycontributionhistoryscreen_to_userchoicescreen()

    def loadingfunc(self,screen):
        self.screen_manager.transition.duration = 0
        self.screen_manager.current = 'loadingscreen'
        while self.stop_load != True:
            if self.ctr == 0:
                self.loadingscreen.loadingimage1.opacity = 1
                self.loadingscreen.loadingimage2.opacity = 0
                self.loadingscreen.loadingimage3.opacity = 0
            if self.ctr == 1:
                self.loadingscreen.loadingimage1.opacity = 0
                self.loadingscreen.loadingimage2.opacity = 1
                self.loadingscreen.loadingimage3.opacity = 0
            if self.ctr == 2:
                self.loadingscreen.loadingimage1.opacity = 0
                self.loadingscreen.loadingimage2.opacity = 0
                self.loadingscreen.loadingimage3.opacity = 1
            self.ctr+=1
            if self.ctr == 3:
                self.ctr = 0

        self.screen_manager.transition.duration = 0
        self.screen_manager.current = screen
    def reward_calculator(self):
        k = self.email_spliitter(self.email)
        try:
            record = self.database.child("users_rewards").child(k).get()
            reward_earned = str(record.val()["reward earned"])
            text_ = "[font=first][color=#184B29][size=130]"+reward_earned+"[/size][/color][/font] [font=first][color=#184B29][size=30]inr.[/size][/color][/font]"
            self.rewardsscreen.balance.text = text_
        except:
            toast("user is not added in users_reward database")
    def searchlessonsscreen_to_searchresultsscreen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'searchresultscreen'
    def searchresultsscreen_to_searchlessonsscreen(self):
        self.screen_manager.transition.direction = 'right'

        self.screen_manager.current = 'searchlessonsscreen'
    def userchoicescreen_to_searchlessonsscreen(self):
        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'searchlessonsscreen'
    def searchlessonsscreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'userchoicescreen'
        try:
            downloading_path = "files_meta_info/"
            shutil.rmtree(downloading_path)
        except:
            pass
    def userchoicescreen_to_rewardsscreen(self):

        self.screen_manager.transition.direction = 'left'
        self.screen_manager.current = 'rewardsscreen'
        self.reward_calculator()
    def rewardsscreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'userchoicescreen'
    def userchoicescreen_to_mycontributionhistoryscreen(self):
        self.showresultscreen.lay.clear_widgets()
        self.screen_manager.transition.direction = 'left'

        self.screen_manager.current = 'showresultscreen'
        self.dataloading_at_showresultscreen_from_mycontributionhistoryscreen()
    def mycontributionhistoryscreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'right'

        self.screen_manager.current = 'userchoicescreen'
    def contributescreen_to_fileloaderscreen(self):
        self.screen_manager.transition.direction = 'up'

        self.screen_manager.current = 'fileloaderscreen'
    def fileloaderscreen_to_contributescreen(self):
        self.screen_manager.transition.direction = 'down'

        self.screen_manager.current = 'contributescreen'
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
    def userchoicescreen_to_contributescreen(self):
        self.screen_manager.transition.direction = 'left'

        self.screen_manager.current = 'contributescreen'
    def userchoicescreen_to_settingsscreen(self):
        self.screen_manager.transition.direction = 'down'

        self.screen_manager.current = 'settingsscreen'
    def settingsscreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'up'

        self.screen_manager.current = 'userchoicescreen'

    def contributescreen_to_userchoicescreen(self):
        self.screen_manager.transition.direction = 'right'

        self.screen_manager.current = 'userchoicescreen'

    def userchoicescreen_to_loginscreen(self):
        self.screen_manager.transition.direction = 'down'

        self.screen_manager.current = 'signinscreen'
    def mainscreen_to_signupscreen(self):
        self.screen_manager.transition.direction = 'left'

        self.screen_manager.current = 'signupscreen'
    def signupscreen_to_mainscreen(self):
        self.screen_manager.transition.direction = 'right'
        self.screen_manager.current = 'mainscreen'



#upload(database,storage,path_on_local,full_path)
#download(storage,path_on_local,full_path)
if __name__ == '__main__':
    LabelBase.register(name='second',fn_regular='resources/fonts/FFF_Tusj.ttf')
    LabelBase.register(name='first',fn_regular='resources/fonts/Pacifico.ttf')


    uiApp().run()
