from tkinter import *
from tkinter import _setit
from tkinter.ttk import Style, Treeview
from tkinter import messagebox
import copy
options = ["Groceries", "Housing", "Clothing", "Transportation expenses", "Insurance", "Health Care", "Debt Payments"]
original_options = options[:]
count=0
length=0
count1=0
op_label=None
def Start_again():
    global op_label
    global count1
    count1=0
    expense_entry.delete(0, 'end')
    e1.delete(0,'end')
    table.delete(*table.get_children())
    if op_label:
        op_label.destroy()
    current_options = option_menu["menu"].children.keys()
    option_menu["menu"].delete(0, "end") 
    selected_option.set('Options')
    for option in original_options:
        if option not in current_options:
            option_menu["menu"].add_command(label=option, command=_setit(selected_option, option))

def calculate_expenses_and_profit():
    global count1
    total_expenses = count1
    income = int(e1.get())
    profit = income - total_expenses
    return total_expenses, profit

def update_profit_label():
    global op_label
    if op_label:
        op_label.destroy()
    total_expenses, profit = calculate_expenses_and_profit()
    op_label = Label(root, text="The final Expense of this month is: " + str(total_expenses) + " and the profit is: " + str(profit), font=("Comic Sans MS", 20, "bold"), bg="#FFFF7F", fg="#000000")
    op_label.pack()
    if profit > 0:
        messagebox.showinfo("Congrats!", "Keep saving")
    else:
        messagebox.showwarning("So Sad", "Losses are not good for health")

def select_option():
    category = selected_option.get()
    expense = expense_entry.get()
    global count1
    global count
    count1=count1+int(expense)
    count=count+1
    if count==len(options)+1:
        messagebox.showerror("Error", "Cannot add Category")
        expense_entry.delete(0, 'end')
    elif expense:
        table.insert('', 'end', values=(category, expense))
        expense_entry.delete(0, 'end')
        options.remove(category)
        option_menu['menu'].delete(0, 'end')
        for option in options:
            option_menu['menu'].add_command(label=option, command=lambda value=option: selected_option.set(value))
    else:
        messagebox.showerror("Error", "Please enter an expense.")

root = Tk()
root.title('Expense Tracker')
root.configure(bg="#FFFF7F")
root.state('zoomed')

border_frame = Frame(root, highlightbackground="black", highlightthickness=2)
border_frame.pack(padx=5, pady=5)
image = PhotoImage(file="icon_photo.png")
label = Label(border_frame, image=image)
label.pack()
border_frame.place(x=0, y=0)
label3=Label(root,text="Enter income per month: ",font=("Comic Sans MS", 20, "bold"), bg="#FFFF7F", fg="#000000")
label3.pack()
e1=Entry(root)
e1.pack()

label1 = Label(root, text="Select category", font=("Comic Sans MS", 26, "bold"), bg="#FFFF7F", fg="#000000")
label1.pack()

# Options
selected_option = StringVar()
selected_option.set("Options")
option_menu = OptionMenu(root, selected_option, *options)
option_menu.config(width=20, height=2, font=("Comic Sans MS", 18, "bold"), fg="#000000")
option_menu.pack()
label2 = Label(root, text="Enter expense for the selected category:", font=("Comic Sans MS", 12, "bold"), bg="#FFFF7F", fg="#000000")
label2.pack()
expense_entry = Entry(root)
expense_entry.pack()
frame = Frame(root,bg="#FFFF7F")
frame.pack(padx=10,pady=10)
my_button = Button(frame, text="Select", command=select_option, font=("Comic Sans MS", 14, "bold"))
my_button.pack(side=LEFT,padx=10, pady=10)
my_submit=Button(frame,text="Submit",command=update_profit_label,font=("Comic Sans MS", 14, "bold"))
my_submit.pack(side=LEFT,padx=10,pady=10)
my_refersh=Button(frame,text="Refresh",command=Start_again,font=('Comic Sans MS',14,"bold"))
my_refersh.pack(side=LEFT,padx=10,pady=10)

table = Treeview(root,columns=('Categories', 'Expenses'), show='headings')
style=Style()
style.theme_use("clam")
table.heading('Categories', text='Categories')
table.heading('Expenses', text='Expenses')
table.pack(side="top", fill="x", expand=True)
root.mainloop()