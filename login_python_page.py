from tkinter import * 


root = Tk()
root.geometry("500x250")

def getvals():
    print("Accpeted!")
#Heading
Label(root,text="Python Registration Form" , font="ar 15 bold").grid(row=0,column=3)

#field Name
name = Label(root,text = "Name")
email = Label(root,text = "Email")
password = Label(root,text = "Password")
gender = Label(root,text = "Gender")
address = Label(root,text = "Address")

#Packing Fields
name.grid(row=1,column=2)
email.grid(row=2,column=2)
password.grid(row=3,column=2)
gender.grid(row=4,column=2)
address.grid(row=5,column=2)

# Variables for Storing data
namevalue = 'StringVar'
emailvalues = 'StringVar'
passwordvalue = 'StringVar'
gendervalues = 'StringVar'
addressvalue = 'Stringvar'
checkvalue = IntVar

# Creating Entry Fields
nameentry = Entry(root,textvariable=namevalue)
emailentry = Entry(root,textvariable=emailvalues)
passwordentry = Entry(root,textvariable=passwordvalue)
genderentry = Entry(root,textvariable=gendervalues)
addressentry = Entry(root,textvariable=addressvalue)

# packing Entry Fields
nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
passwordentry.grid(row=3,column=3)
genderentry.grid(row=4,column=3)
addressentry.grid(row=5,column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="remember me?" , variable=checkvalue)
checkbtn.grid(row=6, column=3)

#submit button
Button(text="Submit", command=getvals).grid(row=7,column=3)

root.mainloop()