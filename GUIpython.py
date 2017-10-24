from tkinter import *
from URLlinksEXTRACTOR import extractfunctionForGui
from Stack import Stack

root = Tk()
root.minsize(width=900, height=500)
root.grid_columnconfigure(0,weight=0)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_rowconfigure(0,weight=0)
root.grid_rowconfigure(1,weight=1)

labelTitle = Label(root, text= 'HTML LINK EXTRACTOR', fg="red")
labelTitle.grid(row=0, column=1)

content = StringVar()
entry = Entry(root, width=50, textvariable=content)
entry.grid(row=1, column = 1)
back = Stack()

def extractUrl():
    if entry.get():
        back.push(entry.get())
        if back.size() > 1:
            button2.config(state='normal')
        links = extractfunctionForGui(entry.get())
        listbox.delete(0,END)
        for i in links:
            listbox.insert(END, links[i])

def goBack():
    back.pop()
    if back.size() <= 1:
        button2.config(state='disabled')
    print('back.peek():',back.peek())
    links = extractfunctionForGui(back.peek())
    listbox.delete(0, END)
    for i in links:
        listbox.insert(END, links[i])

button1 = Button(root, text='Extract Links', command=extractUrl)
button1.grid(row=1, column=0)
button2 = Button(root, text='Back', command=goBack)
button2.grid(row=2,column=0)

def onselect(evt):
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    print('Selected: %d %s' % (index,value))
    content.set(value)

listbox = Listbox(root, name='listbox', width=100, height=50)
listbox.grid(row=3, column= 1)
listbox.bind('<<ListboxSelect>>', onselect)

root.mainloop()