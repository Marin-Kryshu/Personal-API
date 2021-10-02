from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.title('Reminders')
root.geometry("500x575")
root.configure(bg='#208C8D')

# Define font
my_font = Font(family="Century Gothic", size=20, weight="bold")

my_frame = Frame(root)
my_frame.pack()

my_scrollbar = Scrollbar(my_frame, orient=VERTICAL)
my_listbox = Listbox(my_frame,
                     width=50,
                     yscrollcommand=my_scrollbar.set,
                     height=10,
                     bg="SystemButtonFace",
                     bd=0,
                     fg='#27AEA4',
                     font=my_font,
                     highlightthickness=0,
                     selectbackground="#208C8D",
                     activestyle="none"
                     )

my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_listbox.pack(pady=15)

label = Label(root, text="Insert New Item")
label.pack(side=TOP, pady=5)

entry = Entry(root, bd=1,fg='#27AEA4', font=("Helvetica", 24), width=26)
entry.pack(side=TOP)

def insertitem():
    insertitem_enter(TRUE)


def insertitem_enter(event):
    global insert_count
    my_listbox.insert(END, '-' + entry.get())
    entry.delete(0, END)


def delete():
    delete_item_press(TRUE)


def delete_item_press(event):
    try:
        my_listbox.delete(ANCHOR)
    except:
        pass


def deleteAll():
    my_listbox.delete(0, END)


def cross_off():
    my_listbox.itemconfig(
        my_listbox.curselection(),
        fg="#dedede")
    my_listbox.selection_clear(0, END)


def delete_crossed():
    count = 0
    while count < my_listbox.size():
        if my_listbox.itemcget(count, "fg") == "#dedede":
            my_listbox.delete(my_listbox.index(count))
        else:
            count += 1


def save_list_shortcut(event):
    save_list()


def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="C:/downloads",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = '{}.dat'.format(file_name)
        count = 0
        while count < my_listbox.size():
            if my_listbox.itemcget(count, "fg") == "#dedede":
                my_listbox.delete(my_listbox.index(count))
            else:
                count += 1
        stuff = my_listbox.get(0, END)
        output_file = open(file_name, "wb")
        pickle.dump(stuff, output_file)


def open_file_shortcut(event):
    open_list()


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="C:/downloads",
        title="Open File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if file_name:
        my_listbox.delete(0, END)
        input_file = open(file_name, "rb")
        stuff = pickle.load(input_file)
        for item in stuff:
            my_listbox.insert(END, item)


def clear_list_shortcut(event):
    clear_list()


def clear_list():
    my_listbox.delete(0, END)


my_menu = Menu(root)
root.config(menu=my_menu)
menu_file = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="File", menu=menu_file)
menu_file.add_command(label="Save List (Ctrl+S)", command=save_list)
menu_file.add_command(label="Open List (Ctrl+O)", command=open_list)
menu_file.add_separator()
menu_file.add_command(label="Clear List (Ctrl+D)", command=clear_list)

button_frame = Frame(root, bg='#208C8D')
button_frame.pack(pady=20)

# All buttons used
delete_button = Button(button_frame, text="Delete", command=delete)
delete_all_button = Button(button_frame, text="Delete All", command=deleteAll)
cross_off_button = Button(button_frame, text="Cross off", command=cross_off)
insert_button = Button(button_frame, text="Insert Item", command=insertitem)

delete_crossed_button = Button(button_frame, text="Delete Crossed", command=delete_crossed)

root.bind('<Return>', insertitem_enter)
root.bind('<BackSpace>', delete_item_press)
root.bind('<Control_L>' + '<o>', open_file_shortcut)
root.bind('<Control_R>' + '<o>', open_file_shortcut)
root.bind('<Control_L>' + '<s>', save_list_shortcut)
root.bind('<Control_R>' + '<s>', save_list_shortcut)
root.bind('<Control_L>' + '<d>', clear_list_shortcut)
root.bind('<Control_R>' + '<d>', clear_list_shortcut)

# Grid buttons
insert_button.grid(row=0, column=0, )
cross_off_button.grid(row=0, column=1, padx=10)
delete_button.grid(row=0, column=2, padx=10)
delete_crossed_button.grid(row=0, column=3, padx=10)

root.mainloop()