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
    # neseted loop
for x in range(4):
    for y in range(3):
        print(f'( {x}, {y})')
# for loop
total=0
prices=[10,20,40,60]
for price in prices:
    total += price
print(f'total price: {total}')
number = [5,2,5,2,2]
for i in number:
    print('x'*i)
numberes=[30,20,6,8,9,10]
max=numberes[1]
for number in numberes:
    if number>max:
        max=number
print(f"the maximum number is  {max} ")
