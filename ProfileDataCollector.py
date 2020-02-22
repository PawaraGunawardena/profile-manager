#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.1
#  in conjunction with Tcl version 8.6
#    Feb 21, 2020 02:38:08 PM +0530  platform: Linux

import sys

import FileManager

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import ProfileDataCollector_support
import DBManager
import ProfileDataCollectorEdit
import DeleteWindow
from tkinter import filedialog

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    ProfileDataCollector_support.set_Tk_var()
    top = Toplevel1 (root)
    ProfileDataCollector_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    ProfileDataCollector_support.set_Tk_var()
    top = Toplevel1 (w)
    ProfileDataCollector_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("600x450+348+350")
        top.minsize(1, 1)
        top.maxsize(2545, 994)
        top.resizable(1, 1)
        top.title("Feature")
        top.configure(cursor="watch")
        top.configure(highlightcolor="black")

        self.photo_path = None

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.013, rely=0.016, relheight=0.967
                , relwidth=0.975)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(cursor="watch")

        self.LabelTitle = tk.Label(self.Frame1)
        self.LabelTitle.place(relx=0.41, rely=0.023, height=21, width=79)
        self.LabelTitle.configure(activebackground="#f9f9f9")
        self.LabelTitle.configure(text='''Feature:''')

        self.Frame2 = tk.Frame(self.Frame1)
        self.Frame2.place(relx=0.846, rely=0.009, relheight=0.471
                , relwidth=0.145)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")

        self.ButtonAdd = tk.Button(self.Frame2, command=lambda:self.clear_records())
        self.ButtonAdd.place(relx=0.082, rely=0.02, height=21, width=71)
        self.ButtonAdd.configure(text='''Add''')

        self.ButtonEdit = tk.Button(self.Frame2, command=lambda:self.edit_feature())
        self.ButtonEdit.place(relx=0.082, rely=0.132, height=21, width=71)
        self.ButtonEdit.configure(activebackground="#f9f9f9")
        self.ButtonEdit.configure(text='''Edit''')

        self.ButtonDel = tk.Button(self.Frame2, command=lambda:self.delete_feature())
        self.ButtonDel.place(relx=0.082, rely=0.249, height=21, width=71)
        self.ButtonDel.configure(activebackground="#f9f9f9")
        self.ButtonDel.configure(text='''Del''')

        self.ButtonSave = tk.Button(self.Frame2, command=lambda:self.add_feature())
        self.ButtonSave.place(relx=0.082, rely=0.366, height=21, width=71)
        self.ButtonSave.configure(activebackground="#f9f9f9")
        self.ButtonSave.configure(text='''Save''')

        self.ButtonNewPhoto = tk.Button(self.Frame2, command=lambda:self.add_new_photo())
        self.ButtonNewPhoto.place(relx=0.024, rely=0.478, height=51, width=81)
        self.ButtonNewPhoto.configure(activebackground="#f9f9f9")
        self.ButtonNewPhoto.configure(cursor="watch")
        self.ButtonNewPhoto.configure(text='''New Photo''')

        self.LabelPhotoCount = tk.Label(self.Frame2)
        self.LabelPhotoCount.place(relx=0.576, rely=0.493, height=11, width=29)
        self.LabelPhotoCount.configure(text='''0''')

        self.ButtonInquiry = tk.Button(self.Frame2)
        self.ButtonInquiry.place(relx=0.082, rely=0.746, height=21, width=71)
        self.ButtonInquiry.configure(activebackground="#f9f9f9")
        self.ButtonInquiry.configure(text='''Inquiry''')

        self.ButtonExit = tk.Button(self.Frame2, command=lambda:self.client_exit())
        self.ButtonExit.place(relx=0.082, rely=0.868, height=21, width=71)
        self.ButtonExit.configure(activebackground="#f9f9f9")
        # self.ButtonExit.bind( self.client_exit)
        # self.ButtonExit.configure(text='''Exit''', command= self.client_exit())
        self.ButtonExit.configure(text='''Exit''')

        self.LabelName = tk.Label(self.Frame1)
        self.LabelName.place(relx=0.017, rely=0.138, height=21, width=69)
        self.LabelName.configure(activebackground="#f9f9f9")
        self.LabelName.configure(text='''Name:''')

        self.LabelPhone = tk.Label(self.Frame1)
        self.LabelPhone.place(relx=0.409, rely=0.138, height=21, width=69)
        self.LabelPhone.configure(activebackground="#f9f9f9")
        self.LabelPhone.configure(text='''Phone:''')

        self.LabelNote = tk.Label(self.Frame1)
        self.LabelNote.place(relx=0.034, rely=0.23, height=21, width=59)
        self.LabelNote.configure(activebackground="#f9f9f9")
        self.LabelNote.configure(text='''Note:''')

        self.LabelGender = tk.Label(self.Frame1)
        self.LabelGender.place(relx=0.017, rely=0.308, height=31, width=69)
        self.LabelGender.configure(activebackground="#f9f9f9")
        self.LabelGender.configure(text='''Gender:''')

        self.LabelDate = tk.Label(self.Frame1)
        self.LabelDate.place(relx=0.403, rely=0.308, height=31, width=69)
        self.LabelDate.configure(activebackground="#f9f9f9")
        self.LabelDate.configure(text='''Date:''')

        self.EntryName = tk.Entry(self.Frame1)
        self.EntryName.place(relx=0.12, rely=0.138,height=23, relwidth=0.284)
        self.EntryName.configure(background="white")
        self.EntryName.configure(cursor="watch")
        self.EntryName.configure(font="TkFixedFont")

        self.EntryPhone = tk.Entry(self.Frame1)
        self.EntryPhone.place(relx=0.53, rely=0.138,height=23, relwidth=0.284)
        self.EntryPhone.configure(background="white")
        self.EntryPhone.configure(cursor="watch")
        self.EntryPhone.configure(font="TkFixedFont")
        self.EntryPhone.configure(selectbackground="#c4c4c4")

        self.EntryNote = tk.Entry(self.Frame1)
        self.EntryNote.place(relx=0.121, rely=0.228,height=23, relwidth=0.694)
        self.EntryNote.configure(background="white")
        self.EntryNote.configure(cursor="watch")
        self.EntryNote.configure(font="TkFixedFont")

        self.EntryDate = tk.Entry(self.Frame1)
        self.EntryDate.place(relx=0.532, rely=0.315,height=23, relwidth=0.284)
        self.EntryDate.configure(background="white")
        self.EntryDate.configure(cursor="watch")
        self.EntryDate.configure(font="TkFixedFont")

        self.var = tk.IntVar()
        # print(self.var)
        self.RadiobuttonMale = tk.Radiobutton(self.Frame1, variable= self.var, value=1)
        self.RadiobuttonMale.place(relx=0.118, rely=0.322, relheight=0.053
                , relwidth=0.116)
        self.RadiobuttonMale.configure(justify='left')
        self.RadiobuttonMale.configure(text='''Male''')
        # self.RadiobuttonMale.configure(variable=ProfileDataCollector_support.selectedButton)

        self.RadiobuttonFemale = tk.Radiobutton(self.Frame1, variable= self.var, value=2)
        self.RadiobuttonFemale.place(relx=0.224, rely=0.32, relheight=0.053
                , relwidth=0.149)
        self.RadiobuttonFemale.configure(activebackground="#f9f9f9")
        self.RadiobuttonFemale.configure(justify='left')
        self.RadiobuttonFemale.configure(text='''Female''')
        # self.RadiobuttonFemale.configure(variable=ProfileDataCollector_support.selectedButton)

        self.LabelAddress = tk.Label(self.Frame1)
        self.LabelAddress.place(relx=0.012, rely=0.391, height=21, width=69)
        self.LabelAddress.configure(text='''Address:''')

        self.EntryAddress = tk.Entry(self.Frame1)
        self.EntryAddress.place(relx=0.125, rely=0.386, height=23
                , relwidth=0.694)
        self.EntryAddress.configure(background="white")
        self.EntryAddress.configure(cursor="watch")
        self.EntryAddress.configure(font="TkFixedFont")
        self.EntryAddress.configure(selectbackground="#c4c4c4")

    @staticmethod
    def popup1(event, *args, **kwargs):
        Popupmenu1 = tk.Menu(root, tearoff=0)
        Popupmenu1.configure(activebackground="#f9f9f9")
        Popupmenu1.post(event.x_root, event.y_root)

    def client_exit(self):
        exit()
        # print("Hellow")



    def add_feature(self):
        name = self.EntryName.get()
        phone = self.EntryPhone.get()
        note = self.EntryNote.get()
        gender_value = self.var.get()
        print(gender_value)
        gender="Male"
        if(gender_value == 2):
            gender = "Female"


        date = self.EntryDate.get()
        address = self.EntryAddress.get()
        has_image = '0'
        if (self.photo_path != None):
            has_image = '1'

        data = {
            'Name': name,
            'Phone': phone,
            'Note': note,
            'Gender': gender,
            'Date': date,
            'Address': address,
            'Image':has_image
        }

        firebase_db_manager = DBManager.FirebaseDBManager()
        results = firebase_db_manager.insert(data)
        print(results)

        if(self.photo_path != None):
            fileManager = FileManager.FileManager()
            fileManager.insert(results['name'], self.photo_path)

        self.clear_records()

    def edit_feature(self):
        ProfileDataCollectorEdit.vp_start_gui()

    def delete_feature(self):
        DeleteWindow.vp_start_gui()

    def add_new_photo(self):
        print("Hello")
        self.photo_path = filedialog.askopenfilename(initialdir="./", title="Pick the Image", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))
        print(self.photo_path)

    def clear_records(self):
        self.EntryAddress.delete(first=0, last=100)
        self.EntryDate.delete(first=0, last=100)
        self.EntryNote.delete(first=0, last=100)
        self.EntryName.delete(first=0, last=100)
        self.EntryPhone.delete(first=0, last=100)
        # self.RadiobuttonMale.selection_clear()
        # self.RadiobuttonFemale.selection_clear()
        self.var.set(0)
        self.photo_path = None

if __name__ == '__main__':
    vp_start_gui()




