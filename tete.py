from tkinter import *

# ********** Functions **********
def doNothing():
    print("Ok, i won't!")

# ********** TK Initialization **********
root = Tk()
# ********** Main Menu **********
menu = Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New", command=doNothing)
subMenu.add_command(label="Open...", command=doNothing)
subMenu.add_command(label="Save", command=doNothing)
subMenu.add_command(label="Save As...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Page Setup...", command=doNothing)
subMenu.add_command(label="Print...", command=doNothing)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=root.quit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Undo", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Cut", command=doNothing)
editMenu.add_command(label="Copy", command=doNothing)
editMenu.add_command(label="Paste", command=doNothing)
editMenu.add_command(label="Delete", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Find...", command=doNothing)
editMenu.add_command(label="Find Next", command=doNothing)
editMenu.add_command(label="Replace...", command=doNothing)
editMenu.add_command(label="Go To...", command=doNothing)
editMenu.add_separator()
editMenu.add_command(label="Select All", command=doNothing)
editMenu.add_command(label="Time/Date", command=doNothing)

FormatMenu = Menu(menu)
menu.add_cascade(label="Format", menu=FormatMenu)
FormatMenu.add_command(label="Word Wrap", command=doNothing)
FormatMenu.add_command(label="Font...", command=doNothing)

ViewMenu = Menu(menu)
menu.add_cascade(label="View", menu=ViewMenu)
ViewMenu.add_command(label="Status Bar", command=doNothing)

HelpMenu = Menu(menu)
menu.add_cascade(label="Help", menu=HelpMenu)
HelpMenu.add_command(label="View Help", command=doNothing)
HelpMenu.add_separator()
HelpMenu.add_command(label="About Editor", command=doNothing)

AboutMenu = Menu(menu)
menu.add_cascade(label="About", menu=AboutMenu)
AboutMenu.add_command(label="About the Developer", command=doNothing)
AboutMenu.add_separator()
AboutMenu.add_command(label="FK YOALL", command=doNothing)



# ********** Status Bar **********
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN,
anchor=W)
status.pack(side=BOTTOM, fill=X)

# ********** Text Area **********
text = Text(root, height=100, width=200)
text.pack()

# ********** Window Properties **********
root.maxsize(width=800, height=680)
root.minsize(width=666, height=666)
root.title('Text Editor')
root.mainloop()