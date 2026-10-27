pasword="sol1212"
attempts=3
while attempts>0:
    attempts=attempts-1
    user_pass=input('pleas enter the pasword: ')
    if pasword != user_pass and attempts>0:
        print("try agian")
    elif attempts<0:
        break    

    elif user_pass==pasword :
        print("you can acsess")
        break
        
        
          