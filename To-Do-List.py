#importing tkinter library from python
import tkinter as tk
from tkinter import messagebox

#function defined for the add operation on a list
def add_task():
    task = task_enter.get()

    #checking condition if it is false then it will display the output as error occured
    if task !="":
        task_listbox.insert(tk.END,task)
        task_enter.delete(0,tk.END)


    else:
        messagebox.showwaring("Error occuring in the input section","please enter the valid task")

        #function defined for remove the task from the list app created
def remove_task():

    try:
        selected_task_index = task_listbox.curselection()
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwaring("selecting error has occured please enter a valid task to remove the component from the application")
#soundar variable for the todo list app
soundar = tk.Tk()

#display the title of the app as to--do--list App
soundar.title("To--Do--List App")


task_enter = tk.Entry(soundar,width = 75)
task_enter.pack(pady = 55)

#add button color grading and box creating
add_button = tk.Button(soundar, text="Add task to the list",width= 50,bg='Orange',command = add_task)
add_button.pack(pady = 10)

#remove button color grading and box creating
remove_button =tk.Button(soundar,text="remove task from the list",bg='yellow',width=30,command= remove_task)
remove_button.pack(pady= 15)

#changing the background colour
soundar.configure(bg="turquoise")

task_listbox = tk.Listbox(soundar,height = 15,width =65,selectmode= tk.SINGLE)
task_listbox.pack(pady= 50)

soundar.mainloop()
