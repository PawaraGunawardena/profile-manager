#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.1
#  in conjunction with Tcl version 8.6
#    Feb 21, 2020 07:41:34 PM +0530  platform: Linux

import sys
from tkinter import messagebox

import Controller
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

import DeleteWindow_support

def vp_start_gui(root_parent):
    '''Starting point when module is the main routine.'''
    global val, w, root

    root = tk.Tk()
    top = Toplevel1 (root, root_parent=root_parent)
    DeleteWindow_support.init(root, top)
    root.resizable(0, 0)

    # root.grab_set()
    # root.wait_window(root)
    # root.takefocus = True
    # root.focus_set()

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
    # top.grab_set()
    # root.grab_set()
    # w.grab_set()
    DeleteWindow_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None, root_parent= None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        self.root_parent = root_parent
        self.hidden_parent_window()
        # top.geometry("533x95+337+201")
        # top.minsize(1, 1)
        # top.maxsize(2545, 994)
        # top.resizable(1, 1)
        # top.title("New Toplevel")
        # top.configure(cursor="watch")
        # # top.grab_set()

        top.geometry("600x450+348+350")
        top.minsize(1, 1)
        top.maxsize(2545, 994)
        top.resizable(1, 1)
        top.title("Delete")
        top.configure(cursor="watch")
        top.configure(highlightcolor="black")

        self.Labelframe_DeleteFeature = tk.LabelFrame(top)
        self.Labelframe_DeleteFeature.place(relx=0.023, rely=0.021
                , relheight=0.895, relwidth=0.957)
        self.Labelframe_DeleteFeature.configure(relief='groove')
        self.Labelframe_DeleteFeature.configure(text='''Delete Feature''')

        self.Label_FeatureName = tk.Label(self.Labelframe_DeleteFeature)
        self.Label_FeatureName.place(relx=0.137, rely=0.235, height=21, width=59
                , bordermode='ignore')
        self.Label_FeatureName.configure(cursor="watch")
        self.Label_FeatureName.configure(text='''Name:''')

        self.Entry1 = tk.Entry(self.Labelframe_DeleteFeature)
        self.Entry1.place(relx=0.294, rely=0.235, height=23, relwidth=0.424
                , bordermode='ignore')
        self.Entry1.configure(background="white")
        self.Entry1.configure(cursor="watch")
        self.Entry1.configure(font="TkFixedFont")

        self.Button_DeleteCancel = tk.Button(self.Labelframe_DeleteFeature, command=lambda:self.client_exit())
        self.Button_DeleteCancel.place(relx=0.661, rely=0.576, height=31
                , width=71, bordermode='ignore')
        self.Button_DeleteCancel.configure(text='''Cancel''')

        self.Button_DeleteConfirm = tk.Button(self.Labelframe_DeleteFeature, command=lambda:self.delete_confirm())
        self.Button_DeleteConfirm.place(relx=0.841, rely=0.576, height=31
                , width=71, bordermode='ignore')
        self.Button_DeleteConfirm.configure(text='''Delete''')

    def delete_confirm(self):
        if (InternetConnection.is_connected_to_network()):

            if (len(self.Entry1.get()) != 0 ):

                Controller.delete_feature_by_name(self.Entry1.get())
                root.destroy()
                self.get_back_parent_window()
            else:
                messagebox.showwarning("Incomplete Details",
                                       "Please fill the name field!")
        else:
            messagebox.showwarning("No internet connection.", "Connect to the internet to complete the requested data deletion!")

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





