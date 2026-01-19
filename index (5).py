master_contact_list = []
file_name = "sample1.txt"

class contact :
    def __init__(self,name = None,email = None,number = None):
        if name == None and email == None and number == None :
            self.name = input("Enter Contact Name : ")
            self.email = input("Enter Contact Email : ")
            self.number = input("Enter Contact Phone Number : ")
            contact_entry="{},{},{}\n".format(self.name,self.email,self.number)
            master_contact_list.append(contact_entry)
            print("Contact added successfully")
        else : 
            self.name = name 
            self.email = email
            self.number = number


    def show (self):
        print("======================================================")
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Phone Number : ",self.number)
        print("======================================================")

    def update_contact(self):
        current_entry ="{},{},{}\n".format(self.name,self.email,self.number)
        update_item = int(input("Enter 1 for Name\nEnter 2 for Email\nEnter 3 for Contact\nEnter Value : "))
        if update_item == 1 :
            self.name = input("Enter New Name : ")
        elif update_item == 2 :
            self.email = input("Enter New Email : ")
        elif update_item == 3 : 
            self.number = input("Enter New Contact No. : ")
        else : 
            print("Invalid Choice")

        master_contact_list.remove(current_entry)
        contact_entry="{},{},{}\n".format(self.name,self.email,self.number)
        master_contact_list.append(contact_entry)
        print("Contact Updated successfully")

    def delete_contact(self):
        current_entry ="{},{},{}\n".format(self.name,self.email,self.number)
        master_contact_list.remove(current_entry)
        print("Contact Deleted successfully")

                        
def show_all_contact():
    global master_contact_list
    for i in master_contact_list:
        c1 = entrytocontact(i)
        c1.show()
        

def entrytocontact(x) :
    x = x.replace("\n","")
    y = x.split(",")
    c2 = contact(y[0],y[1],y[2])
    return c2

def get_master_data() :
    global master_contact_list
    master_contact_list=[]
    file=open(file_name,"r")
    master_data=file.readlines()
    file.close()
    master_contact_list = master_data

def post_master_data():
    global master_contact_list
    file = open(file_name,"w")
    for i in master_contact_list :
        file.write(i)
    file.close()

def search_contact():
    search_term = input("Enter Search Term : ")
    for k in master_contact_list :
        if search_term in k : 
            current_contact = entrytocontact(k)
            current_contact.show()
            return current_contact
            break  
    else :
        print("Contact Not Found")


get_master_data()
#print(master_contact_list)
choice1 = True
while choice1 == True :
    choice=int(input(
        "Press 1 for Add Contact\n"
        "Press 2 for Search Contact\n"
        "Press 3 for Show All Contact\n"
        "Press 4 for Update Contact\n"
        "Press 5 for Delete Contact\n"
        "Enter a valid choice :")
    )
    
    if choice == 1:
        c1 = contact()
        c1.show()
    elif choice == 2:
        x = search_contact()
    elif choice == 3:
        show_all_contact()
    elif choice == 4:
        current_contact = search_contact()
        current_contact.update_contact()
    elif choice == 5:
        current_contact = search_contact()
        current_contact.delete_contact()
    else:
        print("Invalid Choice")
    next_choice = input("Enter (y) or any key to continue and (n) to stop : ")
    if next_choice == "n"or next_choice == "N":
        choice1 = False
post_master_data()