secret_number1=5
secret_number2=9
gusse_limet=3
gusse_count=0
while gusse_limet > gusse_count:
    gusse=int(input("gusse : "))
    gusse_count +=1
    if gusse==secret_number1 or gusse==secret_number2:
        print("congra you won!")
        break
else:
    print(' sorrt you faild \n pleas trry agian ')