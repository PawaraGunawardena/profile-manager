#! /usr/bin/env python	
#  -*- coding: utf-8 -*-	

import multiprocessing as mp
import os
import sys	
import threading	
import time	
from threading import Thread	

import arrow as arrow	
from tkcalendar import DateEntry	

import Controller	
from StorageManager import FileManager
from View import Inquiry
import InternetConnection
from View.PhotoImageViewer import PhotoImageViewer

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

from View.Support import ProfileDataCollector_support
from StorageManager import DBManager
from View import ProfileDataCollectorEdit
from View import DeleteWindow
from tkinter import filedialog	
import tkinter	
from tkinter import messagebox	

from PIL import Image	
Image.LOAD_TRUNCATED_IMAGES = True	

def updateTreeView(topelevel):	
    while True:	
        # time.sleep(1000)	
        topelevel.update_treeview()	

def vp_start_gui():	
    '''Starting point when module is the main routine.'''	
    global val, w, root	
    root = tk.Tk()	
    ProfileDataCollector_support.set_Tk_var()	
    top = Toplevel1 (root)
    ProfileDataCollector_support.init(root, top)	

    root.resizable(0, 0)	
    root.mainloop()	

    return top	

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
    def __init__(self, top=None, interval=30):	
        '''This class configures and populates the toplevel window.	
           top is the toplevel containing window.'''	
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'	
        _fgcolor = '#000000'  # X11 color: 'black'	
        _compcolor = '#d9d9d9' # X11 color: 'gray85'	
        _ana1color = '#d9d9d9' # X11 color: 'gray85'	
        _ana2color = '#ececec' # Closest X11 color: 'gray92'	

        self.style = ttk.Style()	
        if sys.platform == "win32":	
            self.style.theme_use('winnative')	
        self.style.configure('.', background=_bgcolor)	
        self.style.configure('.', foreground=_fgcolor)	
        self.style.configure('.', font="TkDefaultFont")	
        self.style.map('.', background=	
        [('selected', _compcolor), ('active', _ana2color)])	

        self.top = top	
        top.geometry("600x450+348+350")	
        top.minsize(1, 1)	
        top.maxsize(2545, 994)	
        top.resizable(1, 1)	
        top.title("Feature")	
        top.configure(cursor="arrow")	
        top.configure(highlightcolor="black")	
        root.protocol("WM_DELETE_WINDOW", self.disable_event)

        self.photo_path = None	

        self.Frame1 = tk.Frame(top)	
        self.Frame1.place(relx=0.013, rely=0.016, relheight=0.967	
                , relwidth=0.975)	
        self.Frame1.configure(relief='groove')	
        self.Frame1.configure(borderwidth="2")	
        self.Frame1.configure(relief="groove")	
        self.Frame1.configure(cursor="arrow")	

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
        self.ButtonNewPhoto.configure(cursor="arrow")	
        self.ButtonNewPhoto.configure(text='''New Photo''')	

        self.LabelPhotoCount = tk.Label(self.Frame2)	
        self.LabelPhotoCount.place(relx=0.576, rely=0.493, height=11, width=29)	
        self.LabelPhotoCount.configure(text='''0''')	

        self.ButtonInquiry = tk.Button(self.Frame2, command=lambda:self.inquiry_feature())	
        self.ButtonInquiry.place(relx=0.082, rely=0.746, height=21, width=71)	
        self.ButtonInquiry.configure(activebackground="#f9f9f9")	
        self.ButtonInquiry.configure(text='''Inquiry''')	

        self.ButtonExit = tk.Button(self.Frame2, command=lambda:self.client_exit())	
        self.ButtonExit.place(relx=0.082, rely=0.868, height=21, width=71)	
        self.ButtonExit.configure(activebackground="#f9f9f9")
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
        self.EntryName.configure(cursor="arrow")	
        self.EntryName.configure(font="TkFixedFont")	

        self.EntryPhone = tk.Entry(self.Frame1)	
        self.EntryPhone.place(relx=0.53, rely=0.138,height=23, relwidth=0.284)	
        self.EntryPhone.configure(background="white")	
        self.EntryPhone.configure(cursor="arrow")	
        self.EntryPhone.configure(font="TkFixedFont")	
        self.EntryPhone.configure(selectbackground="#c4c4c4")	

        self.EntryNote = tk.Entry(self.Frame1)	
        self.EntryNote.place(relx=0.121, rely=0.228,height=23, relwidth=0.694)	
        self.EntryNote.configure(background="white")	
        self.EntryNote.configure(cursor="arrow")	
        self.EntryNote.configure(font="TkFixedFont")

        self.cal = DateEntry(top, width=12, background='darkblue', foreground='white', borderwidth=2)	
        self.cal.pack(padx=10, pady=10)	
        self.cal.place(relx=0.517, rely=0.325,height=23, relwidth=0.284)	

        self.var = tk.IntVar()	

        self.RadiobuttonMale = tk.Radiobutton(self.Frame1, variable= self.var, value=1)	
        self.RadiobuttonMale.place(relx=0.118, rely=0.322, relheight=0.053	
                , relwidth=0.116)	
        self.RadiobuttonMale.configure(justify='left')	
        self.RadiobuttonMale.configure(text='''Male''')	

        self.RadiobuttonFemale = tk.Radiobutton(self.Frame1, variable= self.var, value=2)	
        self.RadiobuttonFemale.place(relx=0.224, rely=0.32, relheight=0.053	
                , relwidth=0.149)	
        self.RadiobuttonFemale.configure(activebackground="#f9f9f9")	
        self.RadiobuttonFemale.configure(justify='left')	
        self.RadiobuttonFemale.configure(text='''Female''')	

        self.LabelAddress = tk.Label(self.Frame1)	
        self.LabelAddress.place(relx=0.012, rely=0.391, height=21, width=69)	
        self.LabelAddress.configure(text='''Address:''')	

        self.EntryAddress = tk.Entry(self.Frame1)	
        self.EntryAddress.place(relx=0.125, rely=0.386, height=23	
                , relwidth=0.694)	
        self.EntryAddress.configure(background="white")	
        self.EntryAddress.configure(cursor="arrow")	
        self.EntryAddress.configure(font="TkFixedFont")	
        self.EntryAddress.configure(selectbackground="#c4c4c4")	

        self.style.configure('Treeview', font="TkDefaultFont", rowheight=40)	
        self.Scrolledtreeview1 = ScrolledTreeView(self.Frame1)	
        self.Scrolledtreeview1.place(relx=0.029, rely=0.54, relheight=0.416	
                                     , relwidth=0.94)	
        self.Scrolledtreeview1.configure(columns=("Name", "Phone", "Gender", "Date", "Address", "Feature", "Photo"))	

        # build_treeview_support starting.	
        self.Scrolledtreeview1.heading("#0", text="Image")	
        self.Scrolledtreeview1.heading("#0", anchor="center")	
        self.Scrolledtreeview1.column("#0", width="100")	
        self.Scrolledtreeview1.column("#0", minwidth="100")	
        self.Scrolledtreeview1.column("#0", stretch="1")	
        self.Scrolledtreeview1.column("#0", anchor="w")	

        self.Scrolledtreeview1.heading("Name", text="Name")	
        self.Scrolledtreeview1.heading("Name", anchor="center")	
        self.Scrolledtreeview1.column("Name", width="100")	
        self.Scrolledtreeview1.column("Name", minwidth="100")	
        self.Scrolledtreeview1.column("Name", stretch="1")	
        self.Scrolledtreeview1.column("Name", anchor="w")	

        self.Scrolledtreeview1.heading("Phone", text="Phone")	
        self.Scrolledtreeview1.heading("Phone", anchor="center")	
        self.Scrolledtreeview1.column("Phone", width="100")	
        self.Scrolledtreeview1.column("Phone", minwidth="100")	
        self.Scrolledtreeview1.column("Phone", stretch="1")	
        self.Scrolledtreeview1.column("Phone", anchor="w")	

        self.Scrolledtreeview1.heading("Gender", text="Gender")	
        self.Scrolledtreeview1.heading("Gender", anchor="center")	
        self.Scrolledtreeview1.column("Gender", width="100")	
        self.Scrolledtreeview1.column("Gender", minwidth="100")	
        self.Scrolledtreeview1.column("Gender", stretch="1")	
        self.Scrolledtreeview1.column("Gender", anchor="w")	

        self.Scrolledtreeview1.heading("Date", text="Date")	
        self.Scrolledtreeview1.heading("Date", anchor="center")	
        self.Scrolledtreeview1.column("Date", width="100")	
        self.Scrolledtreeview1.column("Date", minwidth="100")	
        self.Scrolledtreeview1.column("Date", stretch="1")	
        self.Scrolledtreeview1.column("Date", anchor="w")	

        self.Scrolledtreeview1.heading("Address", text="Address")	
        self.Scrolledtreeview1.heading("Address", anchor="center")	
        self.Scrolledtreeview1.column("Address", width="100")	
        self.Scrolledtreeview1.column("Address", minwidth="100")	
        self.Scrolledtreeview1.column("Address", stretch="1")	
        self.Scrolledtreeview1.column("Address", anchor="w")	

        self.Scrolledtreeview1.heading("Feature", text="Feature")	
        self.Scrolledtreeview1.heading("Feature", anchor="center")	
        self.Scrolledtreeview1.column("Feature", width="100")	
        self.Scrolledtreeview1.column("Feature", minwidth="100")	
        self.Scrolledtreeview1.column("Feature", stretch="1")	
        self.Scrolledtreeview1.column("Feature", anchor="w")	


        self.Scrolledtreeview1.bind('<ButtonRelease-1>', self.select_table_value)

        if (not InternetConnection.is_connected_to_network()):	
            messagebox.showwarning("Warning", "No internest connection.")	

        self.set_label_no_of_images()
        self.interval = interval	
        thread = threading.Thread(target=self.run, args=())	
        thread.daemon = True	
        thread.start()	

    @staticmethod	
    def popup1(event, *args, **kwargs):	
        Popupmenu1 = tk.Menu(root, tearoff=0)	
        Popupmenu1.configure(activebackground="#f9f9f9")	
        Popupmenu1.post(event.x_root, event.y_root)	

    def client_exit(self):
        os._exit(0)

    def disable_event(self):
        pass

    def add_feature(self):	
        if (InternetConnection.is_connected_to_network()):	
            name = self.EntryName.get()	
            phone = self.EntryPhone.get()	
            note = self.EntryNote.get()	
            gender_value = self.var.get()	

            gender="Male"	
            if(gender_value == 2):	
                gender = "Female"	

            date = self.cal.get_date()	
            address = self.EntryAddress.get()	
            has_image = '0'	
            if (self.photo_path != None):	
                has_image = '1'	

            if(len(name)!=0 and len(phone) !=0 and len(note) !=0 and len(address) !=0 and gender_value != 0):	

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

                if(self.photo_path != None):
                    fileManager = FileManager.FileManager()	
                    fileManager.insert(results['name'], self.photo_path)	

                self.clear_records()	
                time.sleep(3)	
                self.update_treeview()	
            else:	
                messagebox.showwarning("Incomplete Details",	
                                       "Please fill all the fields!")	

        else:	
            messagebox.showwarning("No internet connection.", "Connect to the internet to complete the requested data insertion!")	

    def edit_feature(self):	
        ProfileDataCollectorEdit.vp_start_gui(self.top)	

    def delete_feature(self):	
        DeleteWindow.vp_start_gui(self.top)	
        self.update_treeview()	

    def inquiry_feature(self):	
        Inquiry.vp_start_gui(self.top)	

    def add_new_photo(self):	

        self.photo_path = filedialog.askopenfilename(initialdir="./", title="Pick the Image", filetypes=(("jpg files", "*.jpg"), ("all files", "*.*")))	
        if (len(self.photo_path)==0):
            self.photo_path = None

    def clear_records(self):	
        self.EntryAddress.delete(first=0, last=100)	
        self.cal.set_date(arrow.now().format('M/D/YY'))	
        self.EntryNote.delete(first=0, last=100)	
        self.EntryName.delete(first=0, last=100)	
        self.EntryPhone.delete(first=0, last=100)	

        self.var.set(0)	
        self.photo_path = None	

        self.update_treeview()	

    def select_table_value(self, x):
        try:	
            test_str_value = self.Scrolledtreeview1.item(self.Scrolledtreeview1.selection())	


            item = self.Scrolledtreeview1.selection()[0]	

            name = self.Scrolledtreeview1.item(item)['values'][0]

            # Controller.get_selected_image(str(name))
            #
            # ImageViewer.vp_start_gui(str(name))
            # self.update_treeview()
            photoImageViewer = PhotoImageViewer(self.top, name)
        except IndexError:	
            print("")	

    def update_treeview(self):	
        dbManager = DBManager.SQLiteDBManager()	
        self.Scrolledtreeview1.delete(*self.Scrolledtreeview1.get_children())	
        dbManager.fill_treeview(self.Scrolledtreeview1)

    def run(self):	
        while True:	
            try:
                dbManager = DBManager.SQLiteDBManager()
                self.Scrolledtreeview1.delete(*self.Scrolledtreeview1.get_children())
                dbManager.fill_treeview(self.Scrolledtreeview1)

                self.set_label_no_of_images()
                time.sleep(self.interval)
            except:
                print("")

    def set_label_no_of_images(self):	
        count = Controller.get_no_of_images()	
        self.LabelPhotoCount['text'] = count

# The following code is added to facilitate the Scrolled widgets you specified.	
class AutoScroll(object):	
    '''Configure the scrollbars for a widget.'''	
    def __init__(self, master):	
        #  Rozen. Added the try-except clauses so that this class	
        #  could be used for scrolled entry widget for which vertical	
        #  scrolling is not supported. 5/7/14.	
        try:	
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)	
        except:	
            pass	
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)	
        try:	
            self.configure(yscrollcommand=self._autoscroll(vsb))	
        except:	
            pass	
        self.configure(xscrollcommand=self._autoscroll(hsb))	
        self.grid(column=0, row=0, sticky='nsew')	
        try:	
            vsb.grid(column=1, row=0, sticky='ns')	
        except:	
            pass	
        hsb.grid(column=0, row=1, sticky='ew')	
        master.grid_columnconfigure(0, weight=1)	
        master.grid_rowconfigure(0, weight=1)	
        # Copy geometry methods of master  (taken from ScrolledText.py)	
        if py3:	
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        else:	
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys()  + tk.Place.__dict__.keys()
        for meth in methods:	
            if meth[0] != '_' and meth not in ('config', 'configure'):	
                setattr(self, meth, getattr(master, meth))	

    @staticmethod	
    def _autoscroll(sbar):	
        '''Hide and show scrollbar as needed.'''	
        def wrapped(first, last):	
            first, last = float(first), float(last)	
            if first <= 0 and last >= 1:	
                sbar.grid_remove()	
            else:	
                sbar.grid()	
            sbar.set(first, last)	
        return wrapped	

    def __str__(self):	
        return str(self.master)	

def _create_container(func):	
    '''Creates a ttk Frame with a given master, and use this new frame to	
    place the scrollbars and the widget.'''	
    def wrapped(cls, master, **kw):	
        container = ttk.Frame(master)	
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))	
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))	
        return func(cls, container, **kw)	
    return wrapped	

class ScrolledTreeView(AutoScroll, ttk.Treeview):	
    '''A standard ttk Treeview widget with scrollbars that will	
    automatically show/hide as needed.'''	
    @_create_container	
    def __init__(self, master, **kw):	
        ttk.Treeview.__init__(self, master, **kw)	
        AutoScroll.__init__(self, master)	

import platform	

def _bound_to_mousewheel(event, widget):	
    child = widget.winfo_children()[0]	
    if platform.system() == 'Windows' or platform.system() == 'Darwin':	
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))	
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))	
    else:	
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))	
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))	
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))	
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))	

def _unbound_to_mousewheel(event, widget):	
    if platform.system() == 'Windows' or platform.system() == 'Darwin':	
        widget.unbind_all('<MouseWheel>')	
        widget.unbind_all('<Shift-MouseWheel>')	
    else:	
        widget.unbind_all('<Button-4>')	
        widget.unbind_all('<Button-5>')	
        widget.unbind_all('<Shift-Button-4>')	
        widget.unbind_all('<Shift-Button-5>')	

def _on_mousewheel(event, widget):	
    if platform.system() == 'Windows':	
        widget.yview_scroll(-1*int(event.delta/120),'units')	
    elif platform.system() == 'Darwin':	
        widget.yview_scroll(-1*int(event.delta),'units')	
    else:	
        if event.num == 4:	
            widget.yview_scroll(-1, 'units')	
        elif event.num == 5:	
            widget.yview_scroll(1, 'units')	

def _on_shiftmouse(event, widget):	
    if platform.system() == 'Windows':	
        widget.xview_scroll(-1*int(event.delta/120), 'units')	
    elif platform.system() == 'Darwin':	
        widget.xview_scroll(-1*int(event.delta), 'units')	
    else:	
        if event.num == 4:	
            widget.xview_scroll(-1, 'units')	
        elif event.num == 5:	
            widget.xview_scroll(1, 'units')	


if __name__ == '__main__':	
    vp_start_gui()