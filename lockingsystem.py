def lock_system():
    user_data={ }
    num=int(input("Enter how many persons you want to add in system= "))
    for i in range(1,(num+1)):
        name=input(f"Enter name{i} = ")
        password=(input(f"Enter {name} password= "))
        user_data[name]=password
    print(user_data)
    
lock_system()



    


