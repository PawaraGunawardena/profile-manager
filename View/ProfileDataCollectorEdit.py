#! /usr/bin/env python	
#  -*- coding: utf-8 -*-

import sys	
from tkinter import messagebox	

import InternetConnection	

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

from View.Support import ProfileDataCollectorEdit_support
import Controller	

def vp_start_gui(root_parent):	
    '''Starting point when module is the main routine.'''	
    global val, w, root	
    root = tk.Tk()	

    top = Toplevel1(root, root_parent=root_parent)	

    ProfileDataCollectorEdit_support.init(root, top)	
    root.resizable(0, 0)	

    root.mainloop()	

w = None	
def create_Toplevel1(rt, *args, **kwargs):	
    '''Starting point when module is imported by another module.	
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''	
    global w, w_win, root	
    #rt = root	
    root = rt	
    w = tk.Toplevel (root)	
    top = Toplevel1 (w)	
    ProfileDataCollectorEdit_support.init(w, top, *args, **kwargs)	
    return (w, top)	

def destroy_Toplevel1():	
    global w	
    w.destroy()	
    w = None	

class Toplevel1:	
    def __init__(self, top=None, root_parent=None):	
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
        top.title("Edit")	
        top.configure(cursor="arrow")
        top.configure(highlightcolor="black")	
        root.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.root_parent = root_parent	
        self.hidden_parent_window()	

        self.Labelframe_OldInfo = tk.LabelFrame(top)	
        self.Labelframe_OldInfo.place(relx=0.017, rely=0.022, relheight=0.167	
                , relwidth=0.967)	
        self.Labelframe_OldInfo.configure(relief='groove')	
        self.Labelframe_OldInfo.configure(text='''Old Information''')	

        self.EntryOldName = tk.Entry(self.Labelframe_OldInfo)	
        self.EntryOldName.place(relx=0.172, rely=0.4, height=23, relwidth=0.286	
                , bordermode='ignore')	
        self.EntryOldName.configure(background="white")	
        self.EntryOldName.configure(cursor="arrow")
        self.EntryOldName.configure(font="TkFixedFont")	
        self.EntryOldName.configure(selectbackground="#c4c4c4")	

        self.LabelOldName = tk.Label(self.Labelframe_OldInfo)	
        self.LabelOldName.place(relx=0.017, rely=0.4, height=21, width=79	
                , bordermode='ignore')	
        self.LabelOldName.configure(activebackground="#f9f9f9")	
        self.LabelOldName.configure(text='''Old Name''')

        self.Labelframe_NewInfo = tk.LabelFrame(top)	
        self.Labelframe_NewInfo.place(relx=0.017, rely=0.244, relheight=0.744	
                , relwidth=0.967)	
        self.Labelframe_NewInfo.configure(relief='groove')	
        self.Labelframe_NewInfo.configure(text='''New Information''')	

        self.Label_NewName = tk.Label(self.Labelframe_NewInfo)	
        self.Label_NewName.place(relx=0.052, rely=0.149, height=21, width=99	
                , bordermode='ignore')	
        self.Label_NewName.configure(text='''New Name:''')	

        self.Label_NewPhone = tk.Label(self.Labelframe_NewInfo)	
        self.Label_NewPhone.place(relx=0.052, rely=0.269, height=21, width=89	
                , bordermode='ignore')	
        self.Label_NewPhone.configure(cursor="arrow")
        self.Label_NewPhone.configure(text='''New Phone:''')	

        self.Label_NewNote = tk.Label(self.Labelframe_NewInfo)	
        self.Label_NewNote.place(relx=0.069, rely=0.385, height=21, width=79	
                , bordermode='ignore')	
        self.Label_NewNote.configure(cursor="arrow")
        self.Label_NewNote.configure(text='''New Note:''')	

        self.Label_NewGender = tk.Label(self.Labelframe_NewInfo)	
        self.Label_NewGender.place(relx=0.034, rely=0.493, height=21, width=109	
                , bordermode='ignore')	
        self.Label_NewGender.configure(text='''New Gender:''')	

        self.Label_NewAddress = tk.Label(self.Labelframe_NewInfo)	
        self.Label_NewAddress.place(relx=0.034, rely=0.597, height=21, width=109	
                , bordermode='ignore')	
        self.Label_NewAddress.configure(activebackground="#f9f9f9")	
        self.Label_NewAddress.configure(text='''New Address:''')	

        self.Entry_NewName = tk.Entry(self.Labelframe_NewInfo)	
        self.Entry_NewName.place(relx=0.241, rely=0.149, height=23	
                , relwidth=0.303, bordermode='ignore')	
        self.Entry_NewName.configure(background="white")	
        self.Entry_NewName.configure(cursor="arrow")
        self.Entry_NewName.configure(font="TkFixedFont")	

        self.Entry_NewPhone = tk.Entry(self.Labelframe_NewInfo)	
        self.Entry_NewPhone.place(relx=0.241, rely=0.269, height=23	
                , relwidth=0.303, bordermode='ignore')	
        self.Entry_NewPhone.configure(background="white")	
        self.Entry_NewPhone.configure(cursor="arrow")
        self.Entry_NewPhone.configure(font="TkFixedFont")	
        self.Entry_NewPhone.configure(selectbackground="#c4c4c4")	

        self.Entry_NewNote = tk.Entry(self.Labelframe_NewInfo)	
        self.Entry_NewNote.place(relx=0.241, rely=0.376, height=23	
                , relwidth=0.303, bordermode='ignore')	
        self.Entry_NewNote.configure(background="white")	
        self.Entry_NewNote.configure(cursor="arrow")
        self.Entry_NewNote.configure(font="TkFixedFont")	
        self.Entry_NewNote.configure(selectbackground="#c4c4c4")	


        self.var = tk.IntVar(root)

        self.RadiobuttonMale = tk.Radiobutton(self.Labelframe_NewInfo, variable=self.var, value=1)
        self.RadiobuttonMale.place(relx=0.241, rely=0.486, relheight=0.053
                                   , relwidth=0.116)
        self.RadiobuttonMale.configure(justify='left')
        self.RadiobuttonMale.configure(text='''Male''')

        self.RadiobuttonFemale = tk.Radiobutton(self.Labelframe_NewInfo, variable=self.var, value=2)
        self.RadiobuttonFemale.place(relx=0.347, rely=0.484, relheight=0.053
                                     , relwidth=0.149)
        self.RadiobuttonFemale.configure(activebackground="#f9f9f9")
        self.RadiobuttonFemale.configure(justify='left')
        self.RadiobuttonFemale.configure(text='''Female''')

        self.Entry_NewAddress = tk.Entry(self.Labelframe_NewInfo)
        self.Entry_NewAddress.place(relx=0.241, rely=0.594, height=23	
                , relwidth=0.303, bordermode='ignore')	
        self.Entry_NewAddress.configure(background="white")	
        self.Entry_NewAddress.configure(cursor="arrow")
        self.Entry_NewAddress.configure(font="TkFixedFont")	
        self.Entry_NewAddress.configure(selectbackground="#c4c4c4")	

        self.Button_SaveUpdate = tk.Button(self.Labelframe_NewInfo, command=lambda:self.find_by_name())	
        self.Button_SaveUpdate.place(relx=0.759, rely=0.776, height=31, width=111	
                , bordermode='ignore')	
        self.Button_SaveUpdate.configure(text='''Save Update''')	

        self.Button_EditCancel = tk.Button(self.Labelframe_NewInfo, command=lambda:self.client_exit())	
        self.Button_EditCancel.place(relx=0.552, rely=0.776, height=31, width=71	
                , bordermode='ignore')	
        self.Button_EditCancel.configure(activebackground="#f9f9f9")	
        self.Button_EditCancel.configure(text='''Cancel''')	

    @staticmethod	
    def popup1(event, *args, **kwargs):	
        Popupmenu1 = tk.Menu(root, tearoff=0)	
        Popupmenu1.configure(activebackground="#f9f9f9")	
        Popupmenu1.post(event.x_root, event.y_root)	

    def disable_event(self):
        pass

    def find_by_name(self):	

        if(InternetConnection.is_connected_to_network()):
            old_name = self.EntryOldName.get()
            name = self.Entry_NewName.get()	
            phone = self.Entry_NewPhone.get()	
            note = self.Entry_NewNote.get()

            gender_value = self.var.get()

            gender = "Male"
            if (gender_value == 2):
                gender = "Female"

            address = self.Entry_NewAddress.get()

            if (len(name) != 0 and len(phone) != 0 and len(note) != 0 and len(address) != 0 and len(gender) != 0):	
                data = {	
                    'Name': name,	
                    'Phone': phone,	
                    'Note': note,	
                    'Gender': gender,	
                    'Address': address	
                }	

                # Controller.find_object_id_by_name(old_name, data)	
                Controller.update_feature_by_name(old_name, data)	
                root.destroy()	
                self.get_back_parent_window()
            else:	
                messagebox.showwarning("Incomplete Details",	
                                       "Please fill all the required fields!")	
        else:	
            messagebox.showwarning("No internet connection.", "Connect to the internet to complete the requested edit!")	

    def client_exit(self):
        root.destroy()
        self.get_back_parent_window()

    def hidden_parent_window(self):	
        self.root_parent.withdraw()	

    def get_back_parent_window(self):	
        self.root_parent.update()	
        self.root_parent.deiconify()	

if __name__ == '__main__':	
    vp_start_gui()