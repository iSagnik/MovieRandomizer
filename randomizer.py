import random
import csv
from io import StringIO
import re
from random import seed
from tkinter import Tk, Label, Button, BOTH, Frame, filedialog
from os import sys
import os
import argparse
def getRowCount(reader):
    theRow = ''
    rowCount = 0
    for row in reader:
        theRow = row
        if any(c.isalpha() for c in theRow):
            rowCount += 1
        else:
            break
    return rowCount


def getColCount(reader):
    theCol = 0
    for row in reader:
        theCol = len(row) - 1
    return theCol


movieArray = ["Comedy", "Thriller", "Action", "Rom-Com", "Drama", "Critically Acclaimed",
              "MindFuck", "Fantasy/Sci Fi", "Animated", "Mystery", "Biopic", "B-Romantic/drama", "BollyFeels", "B-Action/Thriller", "B-Biopics", "B-Critically Acclaimed", "B-Comedy"]


def getFile(fileName2):
    f = open(fileName2, 'r')
    datafiletemp = f.read()
    f.close()
    reader = csv.reader(StringIO(datafiletemp))
    return reader


def getMovie(num, option):
    reader = getFile(fileName)
    movie = ''
    if option == 2:
        i = 0
        for row in enumerate(reader):
            if i == num:
                while movie == '':
                    movie = random.choice(row[1])
                break
            i += 1
    elif option == 1:
        content = []
        skip = 0
        for row in reader:
            if skip != 0:
                content.append(row[num])
            skip += 1
        while movie == '':
            movie = random.choice(content)
    return movie


'''
def selectMovie(col, movie):
    reader = getFile(fileName)
    with open(fileName, 'w') as fw:
        cw = csv.writer(fw)
        for row in reader:
            if row[col] != movie:
                cw.writerow(row)
            elif row[col] == movie:
                #print('reached')
                row[col] = ''
                cw.writerow(row)
            elif not any(c.isalpha() for c in row):
                break
    exit()
'''


def getList():
    i = 1
    txt = ''
    for genre in movieArray:
        txt = txt + f'{i}. {genre}\n'
        i += 1
    return txt


class Backend:

    # def __init__(self):
    #    self = self
    # self.main(filter)

    def main(self, filter, genre):
        '''
        print("Welcome to the Movie Randomizer")
        print("Choose Option: ")
        print("1. Filter by Genre")
        print("2. Entire list")
        print("3. Exit")
        #filter = (int)(input("Enter 1, 2, or 3:  "))
        '''
        reader = getFile(fileName)
        if filter == 2:
            #seed(random.randint(1, 100))
            rowNum = random.randint(0, getRowCount(reader))
            movie = getMovie(rowNum, filter)
            i = 0
            colNum = 0
            reader2 = getFile(fileName)
            for row in reader2:
                if i == rowNum:
                    colNum = row.index(movie)
                    break
                i += 1
            text = "\n" + movieArray[colNum] + "  |  " + movie
            print(text)

            '''
            confirm = (int)(
                input("1. Accept and Delete the movie from file  \n(Any Key) Exit  "))
            if confirm == 1:
                selectMovie(colNum, movie)
            else:
                exit()
            '''
            return text

        elif filter == 1:
            print("Genre List\n")
            print(getList())
            print(genre)
            #genre = (int)(input("\nEnter Genre: "))
            genreStr = movieArray[genre]
            #seed(random.randint(1, 100))
            #movieList = list(next(reader))
            #print(movieList)
            #colNum = movieList.index(genreStr)
            #print("\n", genreStr, "  |  ", getMovie(colNum, filter))
            text = "\n" + genreStr + "  |  " + getMovie(genre, filter)
            print(text)
            return text

        elif filter == 3:
            exit()
            '''
            confirm = (int)(
                input("1. Accept and Delete the movie from file, then Exit\n(Any Key) Exit"))
            if confirm == 1:
                selectMovie(colNum, movie)
            else:
                exit()
            '''


def gui():
    root = Tk()
    root.geometry("500x800")
    #pylint: disable=unused-argument
    _app = Window(root)
    root.mainloop()
    root.destroy()


class Window(Frame):
    def __init__(self, master=None):

        # parameters that you want to send through the Frame class.
        Frame.__init__(self, master)

        # reference to the master widget, which is the tk window
        self.master = master

        # with that, we want to then run init_window, which doesn't yet exist
        self.init_window()

    def init_window(self):
        self.master.title("Movie Randomizer")
        self.configure(bg='white')
        self.pack(fill=BOTH, expand=1)
        labels = []
        buttons = []
        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)
        self.label = Label(
            self, bg="white",font=("Helvetica 16 "), text="Welcome to the Movie Randomizer\nChoose an Option:\n", )
        self.label.pack()
        self.ByGenre = Button(self, font=("Helvetica 10 "), borderwidth = 0, width=14,
                           height=2,bg = "black",fg = "white",text="Filter By Genre",
                              command=lambda: self.genre(labels, buttons))
        self.ByGenre.pack()
        self.ByGenre = Button(self, font=("Helvetica 10"), borderwidth = 0,width=14,
                           height=2,bg = "black",fg = "white", text="Entire list",
                              command=lambda: self.fulllist(labels, buttons))
        self.ByGenre.pack()
        self.close_button = Button(self, font=("Helvetica 10 "), borderwidth = 0,width=14,
                           height=2,bg = "black",fg = "white", text="Close", command=lambda: sys.exit())
        self.close_button.pack()
        #self.label = Label(self, bg="white", text="\n")
        self.label.pack()

    def fulllist(self, labels, buttons):
        for label in labels:
            label.destroy()
        for buttonQ in buttons:
            buttonQ.destroy()
        b = Backend()
        line = Label(self, bg="white",
                     text="\n\n_____________________________________")
        text = Label(self, bg="white",font=("Helvetica 12 "), text=b.main(2, 0))
        labels.append(line)
        labels.append(text)
        line.pack()
        text.pack()

    def genre(self, labels, buttons):
        for buttonQ in buttons:
            buttonQ.destroy()
        for label in labels:
            label.destroy()
        b = Backend()
        lbl = Label(self, bg="white", text="Genre List:\n")
        lbl.pack()
        labels.append(lbl)
        ByGenre0 = Button(
            self, bg = "white", text=movieArray[0],width=18, command=lambda: callMain(self, labels, 0))
        ByGenre0.pack()
        ByGenre1 = Button(
            self, bg = "white", text=movieArray[1],width=18, command=lambda: callMain(self, labels, 1))
        ByGenre1.pack()
        ByGenre2 = Button(
            self, bg = "white", text=movieArray[2], width=18,command=lambda: callMain(self, labels, 2))
        ByGenre2.pack()
        ByGenre3 = Button(
            self, bg = "white", text=movieArray[3],width=18, command=lambda: callMain(self, labels, 3))
        ByGenre3.pack()
        ByGenre4 = Button(
            self, bg = "white", text=movieArray[4],width=18, command=lambda: callMain(self, labels, 4))
        ByGenre4.pack()
        ByGenre5 = Button(
            self, bg = "white", text=movieArray[5],width=18, command=lambda: callMain(self, labels, 5))
        ByGenre5.pack()
        ByGenre6 = Button(
            self, bg = "white", text=movieArray[6],width=18, command=lambda: callMain(self, labels, 6))
        ByGenre6.pack()
        ByGenre7 = Button(
            self, bg = "white", text=movieArray[7], width=18,command=lambda: callMain(self, labels, 7))
        ByGenre7.pack()
        ByGenre8 = Button(
            self, bg = "white", text=movieArray[8],width=18, command=lambda: callMain(self, labels, 8))
        ByGenre8.pack()
        ByGenre9 = Button(
            self, bg = "white", text=movieArray[9], width=18,command=lambda: callMain(self, labels, 9))
        ByGenre9.pack()
        ByGenre10 = Button(
            self, bg = "white", text=movieArray[10],width=18, command=lambda: callMain(self, labels, 10))
        ByGenre10.pack()
        ByGenre11 = Button(
            self, bg = "white", text=movieArray[11],width=18, command=lambda: callMain(self, labels, 11))
        ByGenre11.pack()
        ByGenre12 = Button(
            self, bg = "white", text=movieArray[12],width=18, command=lambda: callMain(self, labels, 12))
        ByGenre12.pack()
        ByGenre13 = Button(
            self, bg = "white", text=movieArray[13],width=18, command=lambda: callMain(self, labels, 13))
        ByGenre13.pack()
        ByGenre14 = Button(
            self, bg = "white", text=movieArray[14], width=18,command=lambda: callMain(self, labels, 14))
        ByGenre14.pack()
        ByGenre15 = Button(
            self, bg = "white", text=movieArray[15], width=18,command=lambda: callMain(self, labels, 15))
        ByGenre15.pack()
        ByGenre16 = Button(
            self, bg = "white", text=movieArray[16], width=18,command=lambda: callMain(self, labels, 16))
        ByGenre16.pack()
        buttons.append(ByGenre0)
        buttons.append(ByGenre1)
        buttons.append(ByGenre2)
        buttons.append(ByGenre3)
        buttons.append(ByGenre4)
        buttons.append(ByGenre5)
        buttons.append(ByGenre6)
        buttons.append(ByGenre7)
        buttons.append(ByGenre8)
        buttons.append(ByGenre9)
        buttons.append(ByGenre10)
        buttons.append(ByGenre11)
        buttons.append(ByGenre12)
        buttons.append(ByGenre13)
        buttons.append(ByGenre14)
        buttons.append(ByGenre15)
        buttons.append(ByGenre16)

        def callMain(self, labelsGen, i):
            for label in labels:
                label.destroy()
            text = Label(self, bg="white", font=("Helvetica 12 "),text=b.main(1, i))
            line = Label(self, bg="white",
                         text="\n_____________________________________")
            labels.append(text)
            labels.append(line)
            line.pack()
            text.pack()
'''
class CommandLine:
    def __init__(self):
        parser = argparse.ArgumentParser(description = "Description for my parser")
        parser.add_argument("-f", "--file", help = "Example: CSV argument [ -F ./movies.csv ]", required = False, default = "")
        argument = parser.parse_args()
        status = False
        if argument.file:
            fileName = argument.file
            filename = os.path.abspath(fileName)
            if os.path.exists(filename):
                print("File Name: {0}".format(fileName))
                status = True
            else:
                raise FileNotFoundError
        if not status:
            fileName = getFileName()
            print("File Name: {0}".format(fileName) )
'''

def getFileName():
    root = Tk()
    root.filename = filedialog.askopenfilename(
        initialdir="/", title="Select file", filetypes=(("csv files", "*.csv"), ("all files", "*.*")))
    filename1 = root.filename
    if filename1 == '':
        sys.exit()
    else:
        root.destroy()
    
    return filename1
fileName = ''

if __name__ == "__main__":
    #app = CommandLine()
    fileName = getFileName()
    gui()
