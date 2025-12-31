master_contact_list = []
file_name = "sample1.txt"

class contact :
    def __init__(self,name = None,email = None,number = None):
        if name == None and email == None and number == None :
            self.name = input("Enter Contact Name : ")
            self.email = input("Enter Contact Email : ")
            self.number = input("Enter Contact Phone Number : ")
            student_entry="{},{},{}\n".format(self.name,self.email,self.number)
            print("Contact added successfully")
            file=open(file_name,"a")
            file.write(student_entry)
            file.close()
        else : 
            self.name = name 
            self.email = email
            self.number = number


    def show(self):
        print("======================================================")
        print("Name : ",self.name)
        print("Email : ",self.email)
        print("Phone Number : ",self.number)
        print("======================================================")

    def update_contact():
        search_term = input("Enter contact name to update : ")
        updated = False

        file=open(file_name, "r")
        data = file.readlines()

        file=open(file_name, "w")
        for contact in data:
            if search_term in contact:
                print("Contact found. Enter new details:")
                name = input("New Name : ")
                email = input("New Email : ")
                number = input("New Phone : ")
                file.write(f"{name},{email},{number}\n")
                get_master_data()
                print(master_contact_list)
                updated = True
                break
            else:
                file.write(contact)

        if updated:
            print("Contact updated successfully")
        else:
            print("Contact not found")

    def delete_contact():
        get_master_data
        print(master_contact_list)
        search_term = input("Enter contact name to delete : ")
        deleted = False

        file=open(file_name, "r")
        data = file.readlines()

        file=open(file_name, "w")
        for line in data:
            if search_term in line:
                deleted = True
            else:
                file.write(line)

        if deleted:
            print("Contact deleted successfully")
        else:
            print("Contact not found")

def show_all_contact():
    file=open(file_name,"r")
    Master_data=file.readlines()
    file.close()
    for i in Master_data :
        show(self)(i)
        

def get_master_data() :
    global master_contact_list
    master_contact_list()
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
    get_master_data()
    search_term = input("Enter Search Term : ")
    for k in master_contact_list :
        if search_term in k : 
            k = k.replace("\n","")
            y = k.split(",")
            print(y)
            c1 = contact(y[0],y[1],y[2])
            c1.show()
            break  
    else :
        print("Contact Not Found")



get_master_data()
print(master_contact_list)
choice1 = True
while choice1 == True :
    choice=int(input("press 1 for add contact\npress 2 for search contact\npress 3 for show_all_contact\npress 4 for update contact\npress 5 for delete contact\nenter a valid choice:"))
    if choice == 1:
        c1 = contact()
        c1.show()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        show_all_contact()
    elif choice == 4:
        contact.update_contact()
    elif choice == 5:
        contact.delete_contact()
    else:
        print("Invalid Choice")
    next_choice = input("Enter (y) or any key to continue and (n) to stop : ")
    if next_choice == "n"or next_choice == "N":
        choice1 = False 