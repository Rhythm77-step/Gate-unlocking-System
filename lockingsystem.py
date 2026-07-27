def lock_system():
    #making empty dictionary
    user_data={ }
    num=int(input("Enter how many persons you want to add in system= "))
    for i in range(1,(num+1)):
        name=input(f"Enter name{i} = ")
        name_list=[]
        name_list.append(name)                                                      
        password=(input(f"Enter {name} password= "))
        pass_list=[]
        pass_list.append(password)
        user_data[name]=password
        user_name=input("Enter your name= ")
        if user_name in name_list:
            user_pass=input("Enter your password= ")
            if user_data[name]==password:
                print("---Gate Unlocked---")
            else:
                print("Wrong Password")
        else:
            print("Invalid Name")
lock_system()
            



            
        






    


