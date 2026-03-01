from tkinter import *
import mysql.connector as connector

# SQL Connection
conn = connector.connect(
    host='localhost',
    username='root',
    password='',
    database='students'
)
cursor = conn.cursor()
print("Connected Successfully!")

# ================= FUNCTIONS =================

def Insert_Data():
    cursor.execute(f"INSERT INTO `students`(`first_name`, `last_name`, `age`, `gender`, `class`, `phone_no`, `parent_name`, `parent_phone`) VALUES ('{E1.get()}','{E2.get()}','{E3.get()}','{E4.get()}','{E5.get()}','{E6.get()}','{E7.get()}','{E8.get()}')")
    conn.commit()
    Result.config(text="Data Inserted Successfully!", fg="green")
    Reset_Data()
    Display_Data()


def Reset_Data():
    E1.delete(0, END)
    E2.delete(0, END)
    E3.delete(0, END)
    E4.delete(0, END)
    E5.delete(0, END)
    E6.delete(0, END)
    E7.delete(0, END)
    E8.delete(0, END)
    Result.config(text="")

def delete_Data():
    cursor.execute(f"DELETE FROM `students` WHERE id = '{E9.get()}'")
    conn.commit()
    Result.config(text="Selected Data Deleted Sucessfully..!")
    Display_Data()

def Data_update():
    cursor.execute(f"UPDATE `students` SET `first_name`='{E1.get()}',`last_name`='{E2.get()}',`age`='{E3.get()}',`gender`='{E4.get()}',`class`='{E5.get()}',`phone_no`='{E6.get()}',`parent_name`='{E7.get()}',`parent_phone`='{E8.get()}' WHERE id ='{E9.get()}'")
    conn.commit()
    Result.config(text="Data Updated Successfully!",fg="blue")
    Display_Data()

def Display_Data():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    output = ""
    for row in records:
        output += f"{row}\n"

    Result.config(text=output)


# ================= UI =================

win = Tk()
win.geometry("650x450")
win.title("Student Form")
win.resizable(False,False)

Label(win, text="Student Form", font=("Arial", 20, "bold")).grid(row=0, column=1, columnspan=4)

Label(win, text="First Name").grid(row=1, column=0)
E1 = Entry(win)
E1.grid(row=1, column=1,pady=10,padx=10)

Label(win, text="Last Name").grid(row=1, column=2)
E2 = Entry(win)
E2.grid(row=1, column=3,pady=10,padx=10)

Label(win, text="Age").grid(row=2, column=0)
E3 = Entry(win)
E3.grid(row=2, column=1,pady=10,padx=10)

Label(win, text="Gender").grid(row=2, column=2)
E4 = Entry(win)
E4.grid(row=2, column=3,pady=10,padx=10)

Label(win, text="Class").grid(row=3, column=0)
E5 = Entry(win)
E5.grid(row=3, column=1,pady=10,padx=10)

Label(win, text="Phone").grid(row=3, column=2)
E6 = Entry(win)
E6.grid(row=3, column=3,pady=10,padx=10)

Label(win, text="Parent Name").grid(row=4, column=0)
E7 = Entry(win)
E7.grid(row=4, column=1,pady=10,padx=10)

Label(win, text="Parent Phone").grid(row=4, column=2)
E8 = Entry(win)
E8.grid(row=4, column=3,pady=10,padx=10)

Label(win, text="ID").grid(row=5, column=0)
E9 = Entry(win)
E9.grid(row=5, column=1)

# Buttons
Button(win, text="Insert", bg="green", fg="white", command=Insert_Data).grid(row=6, column=0,pady=10,padx=10)
Button(win, text="Display", command=Display_Data).grid(row=6, column=1,pady=10,padx=10)
Button(win, text="Update", command=Data_update).grid(row=6,column=3,padx=10,pady=10)
Button(win, text="Reset", command=Reset_Data).grid(row=6, column=2,pady=10,padx=10)
Button(win, text="Delete", command=delete_Data).grid(row=6, column=4, padx=10, pady=10)

Result = Label(win, text="", width=80, height=10, bg="white",fg="black", font=("Arial",9,"bold"))
Result.grid(row=7, column=0, columnspan=4,pady=10,padx=10)

win.mainloop()