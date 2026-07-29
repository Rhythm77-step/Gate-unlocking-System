def user_data():
    #making empty dictionary
    data={ }
    num=int(input("Enter how many persons you want to add in system= "))
    for i in range(1,(num+1)):
        i=1 
        name=input(f"Enter name{i} = ")                                                      
        password=(input(f"Enter {name} password= "))
        data[name]=password
        i+=1
"""        
def lock_system():        
    name_list=list(data.keys())    
    user_name=input("Enter your name= ")
    if 

    
        user_pass=input("Enter your password= ")
    else:
        print("Invalid User name")
    if data[user_name]==user_pass:
      print("---Gate Unlocked---")
    else:
        print("Wrong Password")
lock_system()
"""
            




            
        






    


