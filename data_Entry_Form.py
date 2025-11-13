from tkinter import *
from tkinter import ttk

root = Tk()

def enter_data():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    titl = title_combobox.get()
    age = age_spinbox.get()
    nationality = nationality_combobox.get()
    study_course = course_spinbox.get()
    semester = semester_spinbox.get()
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)


    print(titl, first_name,last_name,age,nationality,study_course,semester)
    try:
        with open('data.txt','w') as f:
            f.write(
                f' First Name:{titl} {first_name}\n Last Namw: {last_name}\n Age: {age}\n Nationality: {nationality}\n Completed Course: {study_course}\n Semester: {semester}\n---------------------'
            )
            f.close()
    except Exception as e:
        print(e)

# in

f1 = LabelFrame(root,text="User information")
f1.pack(padx=15,pady=15)
f2 = LabelFrame(root,text="Course information")
f2.pack()
f3 = LabelFrame(root,text="Term & Condition",width=500)
f3.pack()

first_name_label = Label(f1,text="First Name")
first_name_label.grid(row=1, column=1,padx=4,pady=4)
first_name_entry = Entry(f1)
first_name_entry.grid(row=2,column=1,padx=4,pady=4)
last_name_label = Label(f1,text="Last Name")
last_name_label.grid(row=1,column=2,padx=4,pady=4)
last_name_entry = Entry(f1)
last_name_entry.grid(row=2,column=2,padx=4,pady=4)
title_label  = Label(f1,text="Title")
title_label.grid(row=1,column=3,padx=4,pady=4)
title_combobox = ttk.Combobox(f1,values=["","Mr.","Ms.","Dr."])
title_combobox.grid(row=2,column=3,padx=4,pady=4)
age_label = Label(f1,text="Age")
age_label.grid(row=3,column=1,padx=4,pady=4)
age_spinbox = Spinbox(f1,from_=18,to=100)
age_spinbox.grid(row=4,column=1,padx=4,pady=4)
nationality_label = Label(f1,text="Nationality")
nationality_label.grid(row=3,column=2,padx=4,pady=4)
nationality_combobox = ttk.Combobox(f1,values=["Pakistan","America","India"])
nationality_combobox.grid(row=4,column=2,padx=4,pady=4)


# Frame 2

l1 = Label(f2,text="Registration Status")
l1.grid(row=1,column=1,padx=4,pady=4)
checkbox = Checkbutton(f2,text="Curently Registered")
checkbox.grid(row=2,column=1,padx=4,pady=4)

l2 = Label(f2,text="#Completed Course")
l2.grid(row=1,column=2,padx=4,pady=4)
course_spinbox = Spinbox(f2,from_="1",to="50")
course_spinbox.grid(row=2,column=2,padx=4,pady=4)
l3 = Label(f2,text="#Semesters")
l3.grid(row=1,column=3,padx=4,pady=4)
semester_spinbox = Spinbox(f2,from_="1",to="8")
semester_spinbox.grid(row=2,column=3,padx=4,pady=4)

# fram 3
term_checkbox = Checkbutton(f3,text="I accept the term and conditions.")
term_checkbox.grid(row=1,column=1,padx=120,pady=4)

# Button

data_enter_button = Button(root,text="Enter data",width=63,command=enter_data)
data_enter_button.pack(pady=10)


root.mainloop()