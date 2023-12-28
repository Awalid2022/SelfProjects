import tkinter as tk
import time
import os

#-----------------------------------------------------------------------------------------------------------------

import cx_Oracle
import os

os.system("cls")

# Define Connection data
username = 'system'
password = 'admin123'
tns_entry = 'XEPDB1'

dsn = cx_Oracle.makedsn('localhost', '1522', service_name=tns_entry)

#----------------------------------------------------------------------------------------------------------------

#Defining Functions:
# *elemenst defines that the variable of elements is a tuple that takes multiple arguments
def forgetelements(*elements):
    for element in elements:
        element.forget()

def CloseApp(root):
    root.destroy()

def Sign_up():
    root2 = tk.Tk()
    root2.title("Sign up page")
    
    root_width = 400
    root_height = 170

    root2.geometry(f"{root_width}x{root_height}")
    
    label = tk.Label(root2,text="Enter First Name : ")
    label.pack(side='top',anchor='nw')

    First_entry = tk.Entry(root2,width=60)
    First_entry.pack(side='top',anchor='nw')
    
    label = tk.Label(root2,text="Enter Second Name : ")
    label.pack(side='top',anchor='nw')

    Second_entry = tk.Entry(root2,width=60)
    Second_entry.pack(side='top',anchor='nw')
    
    
    label = tk.Label(root2,text="Enter your Email : \n")
    label.pack(side='top',anchor='nw')

    email_entry = tk.Entry(root2,width=60)
    email_entry.pack(side='top',anchor='nw')
    
    button_signup = tk.Button(root2,text="Sign-up",width=20,command= lambda: Add_UsertoDatabase(First_entry.get(),Second_entry.get(),email_entry.get(),root2))
    button_signup.pack(side="left",anchor='nw')
    
    root2.mainloop()

def Add_UsertoDatabase(x,y,z,root):
    
    if len(str(x).strip()) != 0 and len(str(y).strip()) != 0 and len(str(z).strip()) != 0 :
        try:
            connection = cx_Oracle.connect(username, password, dsn)
            cursor = connection.cursor()

            print('Connected Successfully to the database\n')

            values = f"('{x}','{y}','{z}')"

            query = f"INSERT INTO datatable (COLUMN1,COLUMN2,COLUMN3) VALUES {values}"

            #Execute SQL Statement:
            cursor.execute(query)

            #Commit all changes to database to be stored:   
            connection.commit()

        except cx_Oracle.Error as e:
            print(f"Error while connecting to the database, Error Message: {e}")

        finally:
            # Close cursor and connection if they are defined
            cursor.close()
            connection.close()
            
            Complete_label = tk.Label(root,text="Sign - up has been completed!!",background='green')
            Complete_label.pack(side='right' , anchor='se')   
            
            #root.after(2000,forgetelements(warning_label))
            root.after(2000,lambda: CloseApp(root))
            

    else:
        warning_label = tk.Label(root,text="Please Fill all fields of data !!",background='red')
        warning_label.pack(side='right' , anchor='se')   
    
        root.after(2000,lambda: forgetelements(warning_label))
                 
def GetData_From_Database():
    try:
        connection = cx_Oracle.connect(username, password, dsn)
        cursor = connection.cursor()

        print('Connected Successfully to the database\n')
    
        #Execute SQL Statement:
        cursor.execute('''select column1,column3 from datatable
                   where column3 like '%@%' ''')
    
        #Fetch the response of the executed sql query:
        response = cursor.fetchall()
    
        Firstname_list = []
        Email_list = []
    
        #Printing each row of Response:
        for row in response:
            print(row)
            datarow = str(row).strip("()").split(",")
            Firstname_list.append(datarow[0])
            Email_list.append(datarow[1])
    
        #Commit all changes to database to be stored:   
        connection.commit()

    except cx_Oracle.Error as e:
        print(f"Error while connecting to the database, Error Message: {e}")

    finally:
    # Close cursor and connection if they are defined
        cursor.close()
        connection.close()

    return [Firstname_list,Email_list]

def Sign_in(email,root):
    Names,Emails = GetData_From_Database()
    
    User_emails = [str(e).replace("'","").strip() for e in Emails]
    
    if email in User_emails:
        
        print("User exsists")
        
        index = User_emails.index(f"{email}")
        Name = str(Names[index]).replace("'","")
    
        root.after(1000)
        CloseApp(root)
        
        welcome = tk.Tk()
        welcome.title("Logged in Sucessfully !!")
        
        welcome_screen_width = 230
        welcome_screen_hight = 70
        
        welcome.geometry(f"{welcome_screen_width}x{welcome_screen_hight}")
        
        label = tk.Label(welcome,text=f"\nWelcome {Name} Back \nYour Email Exsists in the system !!\n",font=("Times New Roman",12),background="Yellow")
        label.pack(side='top',anchor="center")
        
        welcome.after(1800, lambda: CloseApp(welcome))

    else:
        root.title("Email Doesnt Exsist in Database !!")
        
        root.after(2000)
        root.title("Welcome to Our Program")
        
#----------------------------------------------------------------------------------------------------------------------------------------------
    
# Create Welcome Screen For App
root = tk.Tk()
root.title("Welcome to Our Program")

Names,Emails = GetData_From_Database()

root_width = 400
root_height = 70

root.geometry(f"{root_width}x{root_height}")

#Create Email Sign in Field:

label = tk.Label(root,text="Enter you email : ")
label.pack(side='top',anchor='nw')

email_entry = tk.Entry(root,width=70)
email_entry.pack(side='top',anchor='nw')

button = tk.Button(root,text="Log-in",width=20,command=lambda: Sign_in(email_entry.get(),root))
button.pack(side="left",anchor='nw')

emptylabel = tk.Label(root,width=15)
emptylabel.pack(side='left',anchor='nw')

button = tk.Button(root,text="Sign-up",width=20,command=Sign_up)
button.pack(side="left",anchor='nw')

root.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------
# def on_button_click():

#     label1.forget()
#     label2.forget()
#     label3.forget()
#     entry1.forget()
#     entry2.forget()
#     entry3.forget()
    
#     #Message text
#     label4 = tk.Label(root,text="Hello, " + entry1.get() +" " +  entry2.get()+", \n Hope you are Doing Fine Today!!",font=("helvetica",14))    
#     label4.place(x=350,y=20,anchor='ne')
    
#     root.after(3000,CloseApp)

# #Create Main window
# root = tk.Tk()
# root.title("Simple GUI Window")

# #Adjust window size {Width*Hight}
# root_width = 400
# root_height = 200

# root.geometry(f"{root_width}x{root_height}")

# #Create a label:
# label1 = tk.Label(root,text='Enter First Name')
# label1.pack(side='top',anchor="nw")

# #Create an Entry widget (Input Field)
# entry1 = tk.Entry(root,background='white',width=30)
# entry1.pack(side="top",anchor='nw')

# #Create another label:
# label2 = tk.Label(root,text='\nEnter Second Name',)
# label2.pack(side='top',anchor="nw")

# #Create an Entry widget (Input Field)
# entry2 = tk.Entry(root,background='white',width=30)
# entry2.pack(side="top",anchor='nw')


# #Create another label:
# label3 = tk.Label(root,text='\nEnter your email',)
# label3.pack(side='top',anchor="nw")

# #Create an Entry widget (Input Field)
# entry3 = tk.Entry(root,background='white',width=30)
# entry3.pack(side="top",anchor='nw')

# #Create a button
# Button = tk.Button(root,text='\nSubmit',command=on_button_click,width=100)
# Button.pack(side='right',anchor='se')

# #Bind enter to button click
# root.bind('<Return>', lambda event=None: Button.invoke())

# #Start GUI app
# root.mainloop()