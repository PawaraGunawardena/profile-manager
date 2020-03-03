import os
import time
from tkinter import *

from PIL import Image, ImageTk

from StorageManager import DBManager

import main

class PhotoImageViewer:

    def __init__(self, top=None, name=None):

        top.destroy()
        root = Tk()

        root.geometry("600x450+364+221")
        root.minsize(1, 1)
        root.maxsize(1265, 994)
        root.resizable(1, 1)
        root.title("Image Viewer")
        root.configure(cursor="watch")

        self.last_img_object_list = []
        self.ButtonNext = Button(root, command=lambda: self.load_next_image(root))
        self.ButtonNext.place(relx=0.833, rely=0.889, height=31, width=59)
        self.ButtonNext.configure(text='''Next''')

        self.ButtonPrevious = Button(root, command=lambda:self.load_prev_image(root))
        self.ButtonPrevious.place(relx=0.667, rely=0.889, height=31, width=84)
        self.ButtonPrevious.configure(text='''Previous''')

        self.ButtonBack = Button(root, command=lambda: self.go_back(root))
        self.ButtonBack.place(relx=0.501, rely=0.889, height=31, width=84)
        self.ButtonBack.configure(text='''Back''')

        sqliteManager = DBManager.SQLiteDBManager()
        self.all_names = sqliteManager.getAllNames()
        self.current_name = name
        self.current_index = self.all_names.index(self.current_name)

        self.load_current_image(self.current_name, root)

        root.mainloop()

    def go_back(self, root):
        main.restart(root)


    def load_next_image(self, root):
        self.img.destroy()
        self.current_index +=1
        if(self.current_index >= len(self.all_names)):
            self.current_index = 0

        self.current_name = self.all_names[self.current_index]
        self.load_current_image(self.current_name, root)

    def load_prev_image(self, root):
        self.img.destroy()
        self.current_index -= 1
        if (self.current_index <0 ):
            self.current_index = len(self.all_names)-1

        self.current_name = self.all_names[self.current_index]
        self.load_current_image(self.current_name, root)

    def open_resized_image(self, image_path):
        try:
            saved_image = Image.open(image_path)
            imwidth =570  # the new width you want

            # the next three lines of codes are used to keep the aspect ration of the image
            wpersent = (imwidth / float(saved_image.size[0]))
            hsize = int(float(saved_image.size[1]) * float(
                wpersent))

            if(hsize > 390):
                hsize = 390

                wpersent2 = (hsize / float(saved_image.size[1]))
                imwidth = int(float(saved_image.size[0]) * float(
                    wpersent2))

            saved_image = ImageTk.PhotoImage(saved_image.resize((
                imwidth, hsize),
                Image.ANTIALIAS)
            )

            return saved_image, True
        except:
            return None, False

    def load_current_image(self, name, root):
        sqliteManager = DBManager.SQLiteDBManager()
        id_dict, exist = sqliteManager.getSpecificDataFromName(name)

        if (exist == 1):
            image_path = "images/" + id_dict['ID'] + "/image.jpg"
            saved_image, opened = self.open_resized_image(image_path)
            self.last_img_object_list.append(saved_image)

            self.img = Label(root, image=self.last_img_object_list[-1])
            # self.img.place(relx=0.101, rely=0.2)
            self.img.place(relx=0.41, rely=0.023, height=21, width=79)
            self.img.image = self.last_img_object_list[-1]
            self.img.pack()



