print("\t\t\t\t      ~~CANDY MANAGEMENT SYSTEM~~")
print("--"*50)
candy_dic = {}
customer_dic = {}
sale_dic = {}
def candy_add():
     print("\n**************ADD PRODUCT RECORD**************")
     a_confirmation = "y"
     option = True
     while a_confirmation =="y" or a_confirmation =="Y":
         while True:
             try:
                 ID = eval(input ("\nEnter the product ID: "))
                 break
             except:
                print("Wrong input.You have to enter digits only")
         if option ==False:
             if ID in candy_dic.keys():
                   print("ID already exist.Try another one")
             else:
                 while True:
                     name=input( "\nEnter name of the product: ")
                     if name.isalpha() or (" " in name) ==True:
                         break
                     else:
                         print("Wrong input.You have to enter Alphabets only")
                         
                 while True:
                     try: 
                         quantity=eval(input("\nEnter the quantity of product: ")) 
                         break 
                     except: 
                         print("Wrong input.You have to enter digits only") 
                 while True: 
                     try:
                         price=eval(input("\nEnter the price of product: ")) 
                         break 
                     except: 
                         print("Wrong input.You have to enter digits only") 
                 while True: 
                     a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ")  
                     if a_confirmation.isalpha() or (" " in a_confirmation) ==True: 
                         break 
                     else: 
                         print("Wrong input.You have to enter Alphabets only") 
                     
                 candy_dic[ID]=[name,quantity,price] 
         else: 
             while True: 
                 name=input( "\nEnter name of the product: ") 
                 if name.isalpha() or (" " in name) ==True:  
                     break 
                 else: 
                     print("Wrong input.You have to enter Alphabets only") 
             while True: 
                 try:
                     quantity=eval(input("\nEnter the quantity of product: ")) 
                     break 
                 except:
                     print("Wrong input.You have to enter digits only") 
             while True: 
                 try: 
                     price=eval(input("\nEnter the price of product: ")) 
                     break 
                 except:
                     print("Wrong input.You have to enter digits only") 
             while True: 
                 a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ") 
                 if a_confirmation.isalpha() or (" " in a_confirmation) ==True: 
                     break 
                 else:
                     print("Wrong input.You have to enter Alphabets only") 
                    
             candy_dic[ID]=[name,quantity,price] 
         option =False 
         
def candy_view(): 
    print("\n**************VIEW PRODUCT RECORD**************") 
    print("\t\t\nCANDY_ID\t\tCANDY_NAME\t\tCANDY_QUANTITY\t\tCANDY_PRICE") 
    for ID in candy_dic.keys(): 
        index = candy_dic[ID] 
        print("\n\n  ",ID, "\t\t\t " ,index[0], "\t\t     " ,index[1], "\t\t    " ,index[2])
             
def candy_search(): 
     print("\n**************SEARCH PRODUCT RECORD**************") 
     s_confirmation = "y" 
     while s_confirmation =="y" or s_confirmation =="Y": 
         while True: 
             try: 
                 ID= eval(input ("\nEnter the product ID to SEARCH: ")) 
                 break
             except: 
                print("Wrong input.You have to enter digits only") 
         print("\nCANDY_ID\tCANDY_NAME\tCANDY_QUANTITY\tCANDY_PRICE") 
         if ID in candy_dic.keys(): 
             search=candy_dic[ID]  
             print(ID,"\t\t" ,search[0], "\t\t" ,search[1], "\t\t" ,search[2])                    
         else:
             print("Invalid ID") 
             print("candy not found try another ID") 
         while True: 
                 s_confirmation = input("\nEnter y to continue or any alphabet to end searching process: ") 
                 if s_confirmation.isalpha() or (" " in s_confirmation) ==True: 
                     break 
                 else:
                     print("Wrong input.You have to enter Alphabets only") 
                     
def candy_edit(): 
    print("\n**************EDIT PRODUCT RECORD**************") 
    e_confirmation = "y" 
    while e_confirmation =="y" or e_confirmation =="Y":
         while True: 
             try: 
                 ID= eval(input ("\nEnter the product ID to Edit: ")) 
                 break 
             except: 
                print("Wrong input.You have to enter digits only") 
                
         if ID in candy_dic.keys():
            while True: 
                    try: 
                        edit=eval(input("\n1) To edit name:\n\n2) To edit quantity:\n\n3) To edit price:\n\n4) To edit the whole product record:\n\nEnter your choice:"))
                        break 
                    except: 
                          print("Wrong input.You have to enter digits only") 
        
            if edit ==1: 
             while True: 
                 name=input( "\nEnter name of the product: ") 
                 if name.isalpha() or (" " in name) ==True: 
                     break
                 else: 
                     print("Wrong input.You have to enter Alphabets only") 
             candy_dic[ID][0] = name
             print("Name Edited") 
            elif edit ==2: 
                while True: 
                    try: 
                        quantity=eval(input("\nEnter the quantity of product: ")) 
                        break
                    except: 
                     print("Wrong input.You have to enter digits only") 
                candy_dic[ID][1] = quantity
                print("Quantity Edited") 
            elif edit ==3: 
                while True:
                    try: 
                        price=eval(input("\nEnter the price of product: ")) 
                        break 
                    except:
                        print("Wrong input.You have to enter digits only") 
                candy_dic[ID][2] = price
                print("Price Edited") 
            elif edit ==4: 
                while True: 
                    name=input( "\nEnter name of the product: ") 
                    if name.isalpha() or (" " in name) ==True: 
                        break
                    else: 
                        print("Wrong input.You have to enter Alphabets only") 
                while True: 
                    try: 
                        quantity=eval(input("\nEnter the quantity of product: ")) 
                        break 
                    except: 
                        print("Wrong input.You have to enter digits only") 
                while True:
                    try: 
                        price=eval(input("\nEnter the price of product: ")) 
                        break 
                    except: 
                        print("Wrong input.You have to enter digits only") 
                candy_dic[ID]=[name,quantity,price] 
         else: 
            print("Invalid ID") 
            print("candy not found try another ID") 
         while True: 
             e_confirmation = input("\nEnter y to continue or any alphabet to end editing process: ") 
             if e_confirmation.isalpha() or (" " in e_confirmation) ==True: 
                 break 
             else: 
                 print("Wrong input.You have to enter Alphabets only") 

def candy_delete(): 
    print("\n**************DELETE PRODUCT RECORD**************") 
    d_confirmation = "y" 
    while d_confirmation =="y" or d_confirmation =="Y": 
         while True: 
             try: 
                 ID= eval(input ("\nEnter the product ID to delete: ")) 
                 break 
             except: 
                print("Wrong input.You have to enter digits only")
         if ID in candy_dic.keys():
             del candy_dic[ID]
             print("Record Deleted")
         else: 
             print("Invalid ID") 
             print("candy not found try another ID") 
         while True: 
                 d_confirmation = input("\nEnter y to continue or any alphabet to end deleting process: ") 
                 if d_confirmation.isalpha() or (" " in d_confirmation) ==True: 
                     break
                 else: 
                     print("Wrong input.You have to enter Alphabets only") 
             
             
def candy_menu() : 
    print("\n**************WELCOME TO CANDY MENU**************") 
    candy_confirmation = "y" 
    while candy_confirmation =="y" or candy_confirmation =="Y": 
         while True: 
             try:
                 num = eval(input("\n1) To add candy product:\n\n2) To view candy product:\n\n3) To search candy product:\n\n4) To edit candy product:\n\n5) To delete candy product:\n\nEnter a number from the given  indexes:"))
                 break 
             except: 
                 print("Wrong input.You have to enter digits only") 
         delete =True
         if len(candy_dic)>=1:
             delete =False
         if num == 1 : 
             candy_add()
         elif num == 2 : 
             if delete ==False:
                 candy_view()
             else:
                print("Add record First")
                
         elif num == 3 : 
            if delete ==False:
                candy_search()
            else: 
                print("Add record First")
                
         elif num == 4 : 
            if delete ==False:
                candy_edit()
            else:
                print("Add record First")
                
         elif num == 5 : 
            if delete ==False:
                candy_delete()
            else: 
                print("Add record First")
                
         else: 
            print("Invalid input.Try again") 
         while True:
             candy_confirmation = input("\nEnter y to BACK to candy Menu or any Alphabet to exit this process:") 
             if candy_confirmation.isalpha() or (" " in candy_confirmation) ==True: 
                 break 
             else: 
                 print("Wrong input.You have to enter Alphabets only") 
            

def customer_add():
     print("\n**************ADD CUSTOMER RECORD**************") 
     a_confirmation = "y" 
     option = True
     while a_confirmation =="y" or a_confirmation =="Y":
         while True: 
             try: 
                 ID = eval(input ("\nEnter the Customer's ID: ")) 
                 break 
             except: 
                 print("Wrong input.You have to enter digits only") 
         if option ==False:
             if ID in customer_dic.keys():
                 print("ID already exist.Try another one") 
             else: 
                 while True: 
                     name = input( "\nEnter the customer's name: ")
                     if name.isalpha() or (" " in name) ==True:
                         break 
                     else:
                         print("Wrong input.You have to enter Alphabets only") 
                 while True:
                     try: 
                         Age = eval(input("\nEnter the customer's age: "))
                         break 
                     except: 
                         print("Wrong input.You have to enter digits only") 
                 while True: 
                     try:
                         contact = eval(input("\nEnter the customer's contact: "))
                         break 
                     except:
                         print("Wrong input.You have to enter digits only") 
                 while True: 
                     a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ") 
                     if a_confirmation.isalpha() or (" " in a_confirmation) ==True: 
                         break 
                     else: 
                         print("Wrong input.You have to enter Alphabets only")
                 customer_dic[ID]=[name,Age,contact]
         else: 
             while True: 
                     name = input( "\nEnter the customer's name: ")
                     if name.isalpha() or (" " in name) ==True:
                         break 
                     else:
                         print("Wrong input.You have to enter Alphabets only") 
             while True: 
                 try: 
                     Age = eval(input("\nEnter the customer's age: "))
                     break
                 except: 
                     print("Wrong input.You have to enter digits only") 
                 
             while True: 
                 try: 
                     contact = eval(input("\nEnter the customer's contact: "))
                     break 
                 except: 
                     print("Wrong input.You have to enter digits only") 
             while True:
                     a_confirmation = input("\nEnter y to continue or any alphabet to end adding process: ") 
                     if a_confirmation.isalpha() or (" " in a_confirmation) ==True: 
                         break 
                     else: 
                         print("Wrong input.You have to enter Alphabets only") 
             customer_dic[ID]=[name,Age,contact]
         option =False

def customer_view():
    print("\n**************VIEW CUSTOMER RECORD**************") 
    print("\t\t\nCUSTOMER_ID\t\tCUSTOMER_NAME\t\tCUSTOMER_AGE\t\tCUSTOMER_CONTACT") 
    for ID in customer_dic.keys(): 
        index = customer_dic[ID]
        print("\n\n   ",ID, "\t\t\t   " ,index[0], "\t\t    " ,index[1], "\t\t     " ,index[2])

def customer_search(): 
     print("\n**************SEARCH CUSTOMER RECORD**************") 
     s_confirmation = "y" 
     while s_confirmation =="y" or s_confirmation =="Y":
         while True: 
             try:
                 ID= eval(input ("\nEnter the Customer's ID to SEARCH: ")) 
                 break 
             except: 
                 print("Wrong input.You have to enter digits only") 
     print("\nCUSTOMER_ID\tCUSTOMER_NAME\tCUSTOMER_AGE\tCUSTOMER_CONTACT") 
     if ID in customer_dic.keys():
         search=customer_dic[ID] 
         print(ID,"\t\t" ,search[0], "\t\t" ,search[1], "\t\t" ,search[2])                   
     else: 
         print("Invalid ID") 
         print("customer not found try another ID") 
     while True: 
         s_confirmation = input("\nEnter y to continue or any alphabet to end searching process: ") 
         if s_confirmation.isalpha() or (" " in s_confirmation) ==True: 
             break
         else: 
             print("Wrong input.You have to enter Alphabets only") 

def customer_edit(): 
    print("\n**************EDIT CUSTOMER RECORD**************") 
    e_confirmation = "y"   
    while e_confirmation =="y" or e_confirmation =="Y":    
        while True:    
            try:  
                ID = eval(input ("\nEnter the Customer's ID: "))
                break 
            except: 
                print("Wrong input.You have to enter digits only") 
                
        if ID in customer_dic.keys(): 
                while True:    
                    try:  
                        edit=eval(input("\n1) To edit name:\n\n2) To edit Age:\n\n3) To edit contact:\n\n4) To edit the whole customer record:\n\nEnter your choice:"))
                        break 
                    except: 
                        print("Wrong input.You have to enter digits only") 
                if edit ==1:
                    while True:    
                        name = input( "Enter the customer's name: ") 
                        if name.isalpha() or (" " in name) ==True:
                            break 
                        else:  
                            print("Wrong input.You have to enter Alphabets only") 
                    customer_dic[ID][0] = name
                    print("Name Edited")  
                elif edit ==2:
                    while True:    
                        try:  
                            Age = eval(input("Enter the customer's age: "))
                            break 
                        except: 
                            print("Wrong input.You have to enter digits only") 
                    customer_dic[ID][1] = Age  
                    print("Age Edited")
                elif edit ==3:
                    while True:    
                        try:  
                            contact=eval(input("\nEnter the customer's contact: "))  
                            break 
                        except: 
                            print("Wrong input.You have to enter digits only") 
                    customer_dic[ID][2] = contact
                    print("contact Edited")  
                elif edit ==4:
                    while True:    
                        name = input( "Enter the customer's name: ")  
                        if name.isalpha() or (" " in name) ==True:  
                            break 
                        else:  
                            print("Wrong input.You have to enter Alphabets only") 
                    while True:    
                        try:  
                            Age = eval(input("Enter the customer's age: ")) 
                            break 
                        except: 
                            print("Wrong input.You have to enter digits only") 
                    while True:    
                        try:  
                            contact = eval(input("Enter the customer's contact: "))  
                            break 
                        except: 
                            print("Wrong input.You have to enter digits only") 
                    while True:    
                        update = input("\nEnter y to continue or any alphabet to end editing process: ") 
                        if update.isalpha() or (" " in update) ==True: 
                            break
                        else: 
                            print("Wrong input.You have to enter Alphabets only") 
                    customer_dic[ID]=[name,Age,contact]
        else: 
            print("Invalid ID") 
            print("customer not found try another ID") 
        while True:
            e_confirmation = input("\nEnter y to continue or any alphabet to end editing process: ") 
            if e_confirmation.isalpha() or (" " in e_confirmation) ==True: 
                break 
            else: 
                print("Wrong input.You have to enter Alphabets only") 

def customer_delete(): 
    print("\n**************DELETE CUSTOMER RECORD**************") 
    d_confirmation = "y"  
    while d_confirmation =="y" or d_confirmation =="Y":
         while True: 
             try: 
                 ID = eval(input ("\nEnter the Customer's ID: ")) 
                 break 
             except: 
                 print("Wrong input.You have to enter digits only") 
         if ID in customer_dic.keys(): 
             del customer_dic[ID]
         else:
             print("Invalid ID") 
             print("customer not found try another ID") 
         while True: 
                 d_confirmation = input("\nEnter y to continue or any alphabet to end deleting process: ") 
                 if d_confirmation.isalpha() or (" " in d_confirmation) ==True:
                     break 
                 else: 
                     print("Wrong input.You have to enter Alphabets only") 
             
def customer_menu() : 
    print("\n**************WELCOME TO CUSTOMER MENU**************")
    customer_confirmation = "y" 
    delete =True
    while customer_confirmation =="y" or customer_confirmation =="Y":
        while True: 
            try: 
                num = eval(input("\n\n1) To add Customer's Record:\n\n2) To view Customer's Record :\n\n3) To search Customer's Record:\n\n4) To edit Customer's Record:\n\n5) To delete Customer's Record:\n\nEnter a number from the given  indexes:"))
                break 
            except: 
                print("Wrong input.You have to enter digits only") 
        delete =True
        if len (customer_dic)>=1: 
            delete =False
        if num == 1 :
            customer_add() 
            delete =False
        elif num == 2 : 
            if delete ==False:
                customer_view() 
            else:
                print("Add record First")
        elif num == 3 : 
            if delete ==False:
                customer_search() 
            else: 
                print("Add record First")
        elif num == 4 : 
            if delete ==False:
                customer_edit() 
            else: 
                print("Add record First")
        elif num == 5 : 
            if delete ==False:
                customer_delete() 
            else: 
                print("Add record First")
        else:
            print("Invalid input.Try again") 
        while True: 
            customer_confirmation = input("\nEnter y to BACK to customer Menu or any Alphabet to exit this process:") 
            if customer_confirmation.isalpha() or (" " in customer_confirmation) ==True:
                break 
            else: 
                print("Wrong input.You have to enter Alphabets only") 
                       

def sale_add(): 
    print("\n**************ADD SALE RECORD**************") 
    Order_confirmation ="y" 
    while Order_confirmation =="y" or Order_confirmation =="Y": 
        while True: 
            while True: 
                try: 
                    order_ID = eval(input ("\nEnter your Unique product ID to add sale: ")) 
                    break 
                except: 
                    print("Wrong input.You have to enter digits only")
            if order_ID in candy_dic.keys(): 
                order= candy_dic[order_ID]
                break 
            else: 
                print("Invalid ID") 
                print("candy not found try another ID") 
        while True:
            while True:
                try: 
                    Unique_ID = eval(input("Enter your Unique customer's ID to place order: ")) 
                    break
                except: 
                    print("Wrong input.You have to enter digits only") 
            if Unique_ID in customer_dic.keys():
                order1= customer_dic[Unique_ID]
                break 
            else: 
                print("Invalid ID") 
                print("customer not found try another ID") 
        while True: 
            try: 
                Quantity = eval(input("Enter the Quantity of candy to order: ")) 
                break 
            except: 
                print("Wrong input.You have to enter digits only") 
        
        if order_ID in candy_dic.keys():
            
            order= candy_dic[order_ID]
            
            
            if Unique_ID in customer_dic.keys(): 
                
                
                order_price= Quantity * order[2]
                sale_dic.update({1:[order_price]})
            else: 
                print("Invalid ID") 
                print("customer not found try another ID") 
        else: 
            print("Invalid ID") 
            print("candy not found try another ID") 
        while True: 
                Order_confirmation=input("Enter y to Re_enter or any Alphabet to end Order: ") 
                if Order_confirmation.isalpha() or (" " in Order_confirmation) ==True: 
                    break 
                else: 
                    print("Wrong input.You have to enter Alphabets only") 

def sale_view(): 
    print("\n**************VIEW SALE RECORD**************") 
    print("\nThe price of your order is",sale_dic[1])
    while True: 
        order_bill=input("\nEnter y to print BILL or N to not print the bill :  ")
        if order_bill.isalpha() or (" " in order_bill) == True:
            break 
        print("You have to enter Alphabats here. Try again :  ") 
    if order_bill=="yes" or "Yes": 
        while True: 
            name = input("\nPlease enter customer's name here: ") 
            if name.isalpha() or (" " in name) == True:
                break 
            print("Wrong input.You have to enter Alphabats only") 
        while True:
            gender = input("\nPlease enter customer's gender here: ") 
            if name.isalpha() or (" " in name) == True: 
                break 
            print("Wrong input.You have to enter Alphabats only") 
        while True: 
            try: 
                contact= eval(input("\nEnter customer's contact number here: ")) 
                break
            except: 
                print("Wrong input.You have to enter digits only") 
        print("----------------Order Bill------------------------")
        u="""  *******Thanks For******
*********Visting Us******"""
        print(u)
        print("Name \t\t  Contact number \t\t Gender \t\t Total Amount")
        print(name,"\t\t",contact,"\t\t\t ",gender,"\t\t\t   ",sale_dic[1]) 
        print(" ")
        f="""                        (Complaint or Home Deivery)
                For any complaint or Free home delivery contact us::
                            Contact 000111222333
                            
                            email address abc@def.com"""
        print(f)
        print("---------------------------------------------------------------------------------------------------------")

def sale_menu():  
    print("\n**************WELCOME TO SALE MENU**************") 
    sale_confirmation = "y" 
    delete =True
    while sale_confirmation =="y" or sale_confirmation =="Y": 
        while True: 
            try: 
                choice = eval(input("\n1) To add sale:\n\n2) To view sale:\n\nEnter your choice:")) 
                break 
            except: 
                print("Wrong input.You have to enter digits only") 
        
        if choice ==1: 
            sale_add() 
            delete =False
        elif choice ==2: 
            if len(sale_dic)>=1: 
                sale_view() 
            else:
                print("Place order first.")
        else: 
            print("Invalid Input.Try again") 
            
        while True: 
            sale_confirmation = input("\nEnter y to BACK to SALE Menu or any Alphabet to exit this process:") 
            if sale_confirmation.isalpha() or (" " in sale_confirmation) ==True: 
                break 
            else: 
                print("Wrong input.You have to enter Alphabets only") 
def control_menu():
    print("\n**************WELCOME TO CONTROL MENU**************") 
    delete =False 
    
    choise=7
    while choise!=4:
        while True:
           try: 
               choise=eval(input("\n 1) To Access candy menu:\n\n 2) To Access customer menu:\n\n 3) To Access sale menu:\n\n 4) For exit:\n\nEnter number here : "))
               break 
           except:
               print("Wrong input.You have to enter digits only")
        if choise==1:
           candy_menu()
        elif choise==2:
           customer_menu()
        elif choise==3:
           sale_menu()
        elif choise==4:
            print("PROGRAM TERMINATED") 
            print("Project by:\nIntahal Tallat(FA21-BCS-032)")
            print("Presented to:\nSIR UMER IQBAL\nCS DEPARTMENT")
        else:
            print("Invalid input.Try again")
control_menu()