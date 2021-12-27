import difflib
import webbrowser, os
from tkinter import *
from tkinter import filedialog, messagebox
import logging
from typing import Union
# from toolz.curried import compose

# text1 = open("test1.c", encoding='UTF-8').readlines()
# text2 = open("test2.c", encoding='UTF-8').readlines()

# filename = input("비교할 첫 번째 파일을 입력하세요. ")
# text1 = open(filename, encoding='UTF-8').readlines()
# filename = input("비교할 두 번째 파일을 입력하세요. ")
# text2 = open(filename, encoding='UTF-8').readlines()

path = "D:\\work\\02_vnv\\05. 수산\\01. TC\\00_코드\\NTC8-1Q_REV05_181011\\NTC8-1Q_REV05_181011\\Source\\Analog.c"


class diffReport():

    def __init__(self):
        self.root = Tk()

        self.root.title("diff-report")
        self.root.geometry("430x130")

        blank = Label(self.root, text="  ")
        blank.grid(column=0, row=0)

        titlelabel = Label(self.root, text="Select two files or two folders to compare.")
        titlelabel.grid(column=1, row=0)

        self.input_file1 = Entry(self.root, width=40)
        self.input_file1.insert(0, "1st file or folder")
        self.input_file1.grid(column=1, row=1)

        self.input_file2 = Entry(self.root, width=40)
        self.input_file2.insert(0, "2nd file or folder")
        self.input_file2.grid(column=1, row=2)

        self.input_file1_button = Button(self.root, text='Open', overrelief="solid", width=15, command=self.openDir1, repeatdelay=1000, repeatinterval=100)
        self.input_file1_button.grid(column=2, row=1)

        self.input_file2_button = Button(self.root, text='Open', overrelief="solid", width=15, command=self.openDir2, repeatdelay=1000, repeatinterval=100)
        self.input_file2_button.grid(column=2, row=2)

        comp_button = Button(self.root, text='Compare', overrelief="solid", width=15, command=self.compFile, repeatdelay=1000, repeatinterval=100)
        comp_button.grid(column=1, row=3)

        self.root.mainloop()

    def openDir1(self):
        self.root.filename1 = filedialog.askopenfilename(initialdir = "C:/",title = "choose your file or directory",filetypes = (("all files","*.*"),("all files","*.*")))
        self.input_file1.delete(0, 'end')
        self.input_file1.insert(0, str(self.root.filename1))

    def openDir2(self):
        self.root.filename2 = filedialog.askopenfilename(initialdir = "C:/",title = "choose your file or directory",filetypes = (("all files","*.*"),("all files","*.*")))
        self.input_file2.delete(0, 'end')
        self.input_file2.insert(0, str(self.root.filename2))

    def detect_encoding(self, target_file :str) -> str:
        encodings = ['utf-8', 'euc-kr', 'ansi']
        for e in encodings:
            try: 
                from codecs import open
                fh = open(target_file, 'r', encoding=e)
                fh.readlines()
                fh.seek(0)
                print("opening the file with encoding: %s" % e)
                return e
            except UnicodeDecodeError:
                print("got unicode error with %s, trying different encoding" % e)
                continue
        print("CSV file encoding must be 'utf-8' or 'euc-kr")
        exit()

    def compFile(self):
        e = self.detect_encoding(self.root.filename1)
        text1 = open(self.root.filename1, 'r', encoding=e).readlines()
        e = self.detect_encoding(self.root.filename2)
        text2 = open(self.root.filename2, 'r', encoding=e).readlines()

        d = difflib.HtmlDiff()
        difference = d.make_file(text1, text2, diffonly=True, fromdesc="Before code", todesc="After code")
        with open("diff.html", "w") as f:
            for line in difference.splitlines():
                print (line, file=f)
        
        messagebox.showinfo("Result", "Compare!")

        filename = 'file:///'+os.getcwd()+'/' + 'diff.html'
        webbrowser.open_new_tab(filename)


if __name__ == '__main__':
    gui = diffReport()
