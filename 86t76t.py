from tkinter import *
root = Tk()
root.title("Inheritance")
root.geometry("600x600")

label_name = Label(root, text="User Name : ")
label_name.place(relx=0.3,rely=0.2, anchor=CENTER)
entry_name = Entry(root)
entry_name.place(relx=0.6,rely=0.2, anchor=CENTER)
label_email = Label(root, text="Email id : ")
label_email.place(relx=0.3,rely=0.3, anchor=CENTER)
entry_email = Entry(root)
entry_email.place(relx=0.6,rely=0.3, anchor=CENTER)
label = Label(root)

dictt = {}
class Users(): 
    def addUser(key, value): 
        global dictt
        dictt[key]=value
        label['text'] = dictt
        

class GetUsers(Users): 
    def getUser(self):
        usr = entry_name.get()
        em = entry_email.get()
        print(usr, em)
        Users.addUser(usr, em)

#Create a object of GetUsers class        
user = GetUsers()
btn = Button(root, text="Add user details", command=user.getUser)
btn.place(relx=0.5,rely=0.4, anchor=CENTER)
label.place(relx=0.5,rely=0.5, anchor=CENTER)
root.mainloop()