def user_data():
    #making empty dictionary
    data={ }
    num=int(input("Enter how many persons you want to add in system= "))
    for i in range(1,(num+1)):
        name=input(f"Enter name{i} = ")                                                      
        password=(input(f"Enter {name} password= "))
        data[name]=password
        i+=1

    def lock_system():
        while True:
            user_name=input("Enter your name= ")
            if user_name in data:
                p=input("Enter your password= ")
                if data[user_name]==p:
                    print("---GATE UNLOCKED---")
                else:
                    print("Wrong password")
            else:
                print("Invalid Name")
    lock_system()
user_data()

            




            
        






    


