#! /usr/bin/env python	
#  -*- coding: utf-8 -*-

import sys	

from tkcalendar import DateEntry	

import Controller	
from StorageManager import DBManager
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

from View.Support import Inquiry_support
from tkinter import messagebox	

def vp_start_gui(root_parent):	
    '''Starting point when module is the main routine.'''	
    global val, w, root	
    root = tk.Tk()	
    var = tk.IntVar(root)
    top = Toplevel1 (root, root_parent=root_parent, var=var)	
    Inquiry_support.init(root, top)	
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
    Inquiry_support.init(w, top, *args, **kwargs)	
    return (w, top)	

def destroy_Toplevel1():	
    global w	
    w.destroy()	
    w = None	

class Toplevel1:	
    def __init__(self, top=None, root_parent=None, var=None):	
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
        top.resizable(0, 0)	
        top.title("Inquiry")	
        top.configure(cursor="arrow")
        top.configure(highlightcolor="black")
        root.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.var = var

        self.Labelframe_Inquiry = tk.LabelFrame(top)	
        self.Labelframe_Inquiry.place(relx=0.025, rely=0.016, relheight=0.944	
                , relwidth=0.95)	
        self.Labelframe_Inquiry.configure(relief='groove')	
        self.Labelframe_Inquiry.configure(text='''Inquiry''')	

        self.root_parent = root_parent	
        self.hidden_parent_window()

        self.Button_InuiryProceed = tk.Button(self.Labelframe_Inquiry, command=lambda:self.proceed_inquiry())	
        self.Button_InuiryProceed.place(relx=0.754, rely=0.753, height=31	
                , width=73, bordermode='ignore')	
        self.Button_InuiryProceed.configure(text='''Inquiry''')	

        self.Button_InquiryCancel = tk.Button(self.Labelframe_Inquiry, command=lambda:self.client_exit())	
        self.Button_InquiryCancel.place(relx=0.526, rely=0.753, height=31	
                , width=72, bordermode='ignore')	
        self.Button_InquiryCancel.configure(text='''Back''')	

        self.LabelName = tk.Label(self.Labelframe_Inquiry)	
        self.LabelName.place(relx=0.017, rely=0.138, height=21, width=69)	
        self.LabelName.configure(activebackground="#f9f9f9")	
        self.LabelName.configure(text='''Name:''')	

        self.LabelPhone = tk.Label(self.Labelframe_Inquiry)	
        self.LabelPhone.place(relx=0.409, rely=0.138, height=21, width=69)	
        self.LabelPhone.configure(activebackground="#f9f9f9")	
        self.LabelPhone.configure(text='''Phone:''')	

        self.LabelNote = tk.Label(self.Labelframe_Inquiry)	
        self.LabelNote.place(relx=0.034, rely=0.23, height=21, width=59)	
        self.LabelNote.configure(activebackground="#f9f9f9")	
        self.LabelNote.configure(text='''Note:''')	

        self.LabelGender = tk.Label(self.Labelframe_Inquiry)	
        self.LabelGender.place(relx=0.017, rely=0.308, height=31, width=69)	
        self.LabelGender.configure(activebackground="#f9f9f9")	
        self.LabelGender.configure(text='''Gender:''')	

        self.LabelDate = tk.Label(self.Labelframe_Inquiry)	
        self.LabelDate.place(relx=0.403, rely=0.308, height=31, width=69)	
        self.LabelDate.configure(activebackground="#f9f9f9")	
        self.LabelDate.configure(text='''Date:''')	

        self.EntryName = tk.Entry(self.Labelframe_Inquiry)	
        self.EntryName.place(relx=0.12, rely=0.138, height=23, relwidth=0.284)	
        self.EntryName.configure(background="white")	
        self.EntryName.configure(cursor="arrow")
        self.EntryName.configure(font="TkFixedFont")	

        self.EntryPhone = tk.Entry(self.Labelframe_Inquiry)	
        self.EntryPhone.place(relx=0.53, rely=0.138, height=23, relwidth=0.284)	
        self.EntryPhone.configure(background="white")	
        self.EntryPhone.configure(cursor="arrow")
        self.EntryPhone.configure(font="TkFixedFont")	
        self.EntryPhone.configure(selectbackground="#c4c4c4")	

        self.EntryNote = tk.Entry(self.Labelframe_Inquiry)	
        self.EntryNote.place(relx=0.121, rely=0.228, height=23, relwidth=0.694)	
        self.EntryNote.configure(background="white")	
        self.EntryNote.configure(cursor="arrow")
        self.EntryNote.configure(font="TkFixedFont")

        self.cal = DateEntry(top, width=12, background='darkblue', foreground='white', borderwidth=2)	
        self.cal.pack(padx=10, pady=10)	
        self.cal.place(relx=0.512, rely=0.345, height=23, relwidth=0.284)	


        self.var.set(0)	
        self.RadiobuttonMale = tk.Radiobutton(self.Labelframe_Inquiry, variable=self.var, value=1)	
        self.RadiobuttonMale.place(relx=0.118, rely=0.322, relheight=0.053	
                                   , relwidth=0.116)	
        self.RadiobuttonMale.configure(justify='left')	
        self.RadiobuttonMale.configure(text='''Male''')

        self.RadiobuttonFemale = tk.Radiobutton(self.Labelframe_Inquiry, variable=self.var, value=2)	
        self.RadiobuttonFemale.place(relx=0.224, rely=0.32, relheight=0.053	
                                     , relwidth=0.149)	
        self.RadiobuttonFemale.configure(activebackground="#f9f9f9")	
        self.RadiobuttonFemale.configure(justify='left')	
        self.RadiobuttonFemale.configure(text='''Female''')

        self.LabelAddress = tk.Label(self.Labelframe_Inquiry)	
        self.LabelAddress.place(relx=0.012, rely=0.391, height=21, width=69)	
        self.LabelAddress.configure(text='''Address:''')	

        self.EntryAddress = tk.Entry(self.Labelframe_Inquiry)	
        self.EntryAddress.place(relx=0.125, rely=0.386, height=23	
                                , relwidth=0.694)	
        self.EntryAddress.configure(background="white")	
        self.EntryAddress.configure(cursor="arrow")
        self.EntryAddress.configure(font="TkFixedFont")	
        self.EntryAddress.configure(selectbackground="#c4c4c4")	

    def client_exit(self):	

        root.destroy()
        self.get_back_parent_window()

    def disable_event(self):
        pass

    def proceed_inquiry(self):
        if (InternetConnection.is_connected_to_network()):

            name = self.EntryName.get()	
            phone = self.EntryPhone.get()	
            note = self.EntryNote.get()	
            gender_value = self.var.get()	

            gender = "Male"	
            if (gender_value == 2):	
                gender = "Female"	

            date = self.cal.get_date()	
            address = self.EntryAddress.get()

            if (len(name) != 0 and len(phone) != 0 and len(note) != 0 and len(address) != 0 ):	

                data = {	
                    'Name': name,	
                    'Phone': phone,	
                    'Note': note,	
                    'Gender': gender,	
                    'Date': str(date),
                    'Address': address	

                }	

                inuiry_results = Controller.inquiry_data(data)	

                if (inuiry_results):
                    messagebox.showinfo("Inquiry Results", "Requested profile exists with Name:"+data['Name']+", Phone:"+data['Phone']	
                                        +", Note:"+data['Note']	
                                        +", Gender:"+data['Gender']	
                                        +", Date:"+str(data['Date'])	
                                        +", Address:"+data['Address'])	

                else:
                    messagebox.showinfo("Inquiry Results",	
                                        "Requested profile not exists for the Name:" +data['Name']+", Phone:"+data['Phone']	
                                        +", Note:"+data['Note']	
                                        +", Gender:"+data['Gender']	
                                        +", Date:"+str(data['Date'])	
                                        +", Address:"+data['Address'])	


            else:	
                messagebox.showwarning("Incomplete Details",	
                                       "Please fill all the required fields!")	
        else:	
            messagebox.showwarning("No internet connection.",	
                                   "Connect to the internet to do inquiries!")	

    def hidden_parent_window(self):	
        self.root_parent.withdraw()	

    def get_back_parent_window(self):	

        self.root_parent.update()	
        self.root_parent.deiconify()

if __name__ == '__main__':	
    vp_start_gui()