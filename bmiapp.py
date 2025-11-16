import tkinter as tk
from tkinter import messagebox
from tkinter import Toplevel

def save():
    time = i7.get()
    bmiresult = str(bmi_)
    age2 = str(age)

    with open('records.txt','a') as file:
        file.write(time + '\n' + 'Age = ' + age2 + '\n' + 'BMI = ' + bmiresult + '\n' + 'Range = ' + type + '\n' + '--' + '\n')
        messagebox.showinfo('Confirmation','Results stored successfully')
        result.destroy()
        info.destroy()

def bmi():
    h = float(i3.get())
    height = float(h*h)
    weight = float(i5.get())

    global bmi_, type, result    
    
    bmi_ = (weight/height)

    if bmi_ < 18.5:
        type = 'Underweight'
    if  (bmi_ > 18.5 and bmi_ <= 24.9):
        type = 'Healthy Weight'
    if (bmi_ > 25 and bmi_ <= 29.9):
        type = 'Overweight'
    if bmi_ > 30:
        type = 'Obese'

    result = Toplevel()
    result.geometry('250x120')
    result.minsize(250, 120)
    result.maxsize(250, 120)
    result.title('Results')

    r1 = tk.Label(
        result,
        text='Your BMI',
        font=('Arial',20,'bold'),
        width=20
    )
    r1.grid(
        row=1,
        column=1,
        columnspan=2,
        padx=2,
        pady=2
    )

    r2 = tk.Label(
        result,
        text='BMI =',
        font=('Arial',15)
    )
    r2.grid(
        row=2,column=1
    )

    r3 = tk.Label(
        result,
        text=f'{bmi_:.2f}',
        font=('Arial',15)
    )
    r3.grid(
        row=2,
        column=2
    )

    r4 = tk.Label(
        result,
        text='Range =',
        font=('Arial',15)
    )
    r4.grid(
        row=3,
        column=1
    )
    
    r5 = tk.Label(
        result,
        text=type,
        font=('Arial',15)
    )
    r5.grid(
        row=3,
        column=2
    )

    r6 = tk.Button(
        result,
        text='Save',
        command=save,
        width=20
    )
    r6.grid(
        row=4,
        column=1,
        columnspan=2
    )


def infopage():
    global i3, i5, i7, info

    info = Toplevel()
    info.title('User Info')
    info.geometry('280x180')
    info.minsize(280, 180)

    i1 = tk.Label(
        info,
        text='Personal Information',
        font=('Arial',20,'bold'),
        width=20
    )
    i1.grid(
        row=1,
        column=1,
        columnspan=2,
        padx=2,
        pady=2
    )

    i2 = tk.Label(
        info,
        text='Height (m)',
        font=('Arial',15)
    )
    i2.grid(
        row=2,
        column=1
    )

    i3 = tk.Entry(info)
    i3.grid(
        row=2,
        column=2
    )

    i4 = tk.Label(
        info,
        text='Weight (kg)',
        font=('Arial',15)
    )
    i4.grid(
        row=3,
        column=1
    )

    i5 = tk.Entry(info)
    i5.grid(
        row=3,
        column=2
    )

    i6 = tk.Label(
        info,
        text='Date',
        font=('Arial',15)
    )
    i6.grid(
        row=4,
        column=1
    )

    i7 = tk.Entry(info)
    i7.grid(
        row=4,
        column=2
    )

    i8 = tk.Button(
        info,
        text='Submit',
        command=bmi,    
        width=20      
    )
    i8.grid(
        row=5,
        column=1,
        columnspan=2
    )

    i9 = tk.Button(
        info,
        text='Back',
        command=info.destroy,
        width=20
    )
    i9.grid(
        row=6,
        column=1,
        columnspan=2
    )

    agecheck.destroy()

def ageverify():
    global age
    age = int(a2.get())

    if age >= 18:
        infopage()
    elif age < 18:
        messagebox.showinfo('info','Program is for people aged 18 and over')
        agecheck.destroy()
        root.destroy()

def aged():
    global a2, agecheck

    agecheck = Toplevel()
    agecheck.title('Age')
    agecheck.geometry('250x100')
    agecheck.minsize(240, 60)
    agecheck.maxsize(240, 60)

    a1 = tk.Label(
        agecheck,
        text='Age',
        font=('Arial',15)
    )
    a1.grid(
        row=1,
        column=1
    )

    a2 = tk.Entry(
        agecheck,
    )
    a2.grid(
        row=1,
        column=2
    )

    a3 = tk.Button(
        agecheck,
        text='Submit',
        command=ageverify,
        width=20
    )
    a3.grid(
        row=2,
        column=1,
        columnspan=2,
    )

root = tk.Tk()
root.title('BMI Calculator')
root.geometry('245x100')
root.minsize(245, 100)
root.maxsize(245, 100)

r1 = tk.Label(
    root,
    text = 'BMI Calculator',
    font = ('Arial',20),
    width = 20
)
r1.grid(
    row=1,
    column=1,
    columnspan=2,
    padx=0,
    pady=0
)

r2 = tk.Button(
    root,
    text='Measure BMI',
    command=aged,
    width=20
)
r2.grid(
    row=2,
    column=1,
    columnspan=2,
    padx=0,
    pady=0
)

r3 = tk.Button(
    root,
    text='Exit',
    command=root.destroy,
    width=20
)
r3.grid(
    row=3,
    column=1,
    columnspan=2,
    padx=0,
    pady=0
)

root.mainloop()