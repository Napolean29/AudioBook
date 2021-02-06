# importing tkinter and tkinter.ttk
# and all their functions and classes


import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install',
                           package])

install('pyttsx3')
install('PyPDF2')
from tkinter import *
from tkinter.ttk import *
import pyttsx3
import PyPDF2

# importing askopenfile function
# from class filedialog
from tkinter.filedialog import askopenfile

def sel():
   selection = "You selected the option " + str(var.get())
   label.config(text = selection)

root = Tk()
root.geometry('200x200')
root.title("Select pdf file")

l1 = Label(root,
         text="From:").grid(row=0)
l2 = Label(root,
         text="To:").grid(row=1)
l3 = Label(root,
         text="Rate:").grid(row=2)

var = IntVar()
R1 = Radiobutton(root, text="Male Voice", variable=var, value=1, command=sel)
R1.grid(row=3,column=1)


R2 = Radiobutton(root, text="Female voice", variable=var, value=2, command=sel)
R2.grid(row=4,column=1)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

Button(root, text='quit', command=root.quit).grid(row=5, column=0, sticky=W, pady=4)
def open_file():
    root.filename = askopenfile(title="Select A File", filetypes=(("PDF files", "*.pdf"),("all files", "*.*")))
    print(root.filename.name)
    file = root.filename.name
    book = open(file, 'rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages

    speaker = pyttsx3.init()
    """RATE"""
    rate = speaker.getProperty('rate')  # getting details of current speaking rate
    speaker.setProperty('rate', int(e3.get()))  # printing current voice rate
    """VOLUME"""
    volume = speaker.getProperty('volume')  # getting to know current volume level (min=0 and max=1)

    speaker.setProperty('volume',
                        0.8)  # setting up volume level  between 0 and 1                     #printing current volume level
    """VOICE"""
    voices = speaker.getProperty('voices')  # getting details of current voice
    if var.get() == 1:
        speaker.setProperty('voice', voices[0].id)  # changing index, changes voices. o for male
    if var.get() == 2:
        speaker.setProperty('voice', voices[1].id)
    print(int(e1.get()), int(e2.get()))  # changing index, changes voices. 1 for female
    if int(e1.get()) > int(e2.get()):
        exit()
    for num in range(int(e1.get()), int(e2.get())):
        page = pdfReader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
Button(root, text ='Open', command = lambda:open_file()).grid(row=6, column=0, sticky=W, pady=4)

label = Label(root)



#root.mainloop()


# This function will be used to open
# file in read mode and only Python files
# will be opened
# btn = Button(root, text ='Open', command = lambda:open_file())
# btn.pack(side = TOP, pady = 10)

mainloop()
