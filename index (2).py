class contact :
    def __init__(self):
        self.name = input("Enter Contact Name : ")
        self.email = input("Enter Contact Email : ")
        self.number = input("Enter Contact Phone Number : ")
        student_entry="{},{},{}\n".format(self.name,self.email,self.number)
        print("Contact added successfully")
        file=open("sample1.txt","a")
        file.write(student_entry)
        file.close()


    def show(self):
        print("======================================================")
        print("Name : ",selflf.name)
        print("Email : ",self.email)
        print("Phone Number : ",self.number)
        print("======================================================")

    def update_contact():
        file=open("sample1.txt","r")
        Master_data=file.readlines()
        file.close()
         search_student = input("Enter Search Term :")
         for i in Master_data:
            print


    def delete_contact():
        pass

def show_all_contact():
    pass

def search_contact():
        pass


choice1 = True
while choice1 == True :
    choice=int(input("press 1 for add contact\npress 2 for search contact\npress 3 for show contact\npress 4 for update contact\npress 5 for delete contact\nenter a valid choice:"))
    if choice == 1:
        c1 = contact()
        #c1.show()
    elif choice == 2:
        search_contact()
    elif choice == 3:
        show_all_contact()
    elif choice == 4:
        update_contact()
    elif choice == 5:
        delete_contact()
    else:
        print("Invalid Choice")
    next_choice = input("Enter (y) or any key to continue and (n) to stop : ")
    if next_choice == "n"or next_choice == "N":
        choice1 = False 