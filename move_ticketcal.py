base_price = 15
name=input('enter your name: '.title)
print(name)
age = int(input('enter your age: '))
seat_type = input("choise your seat type : " .title)
seat_type=seat_type.title
if seat_type=="Gold":
    service_charges=3
elif seat_type=='Premium':
    service_charges=5
elif seat_type=="normal":
    service_charges=1
else:
    print("invalid selection \n plese selecet agian 'normal', Premium ,or Gold")

show_time = input('choise your show time evening or weekend')

if age > 17:
    print('User is eligible to book a ticket')

if age >= 21:
    print('User is eligible for Evening shows')
else:
    print('User is not eligible for Evening shows')

is_member = False
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print('User qualifies for membership discount')
else:
    print('User does not qualify for membership discount')
print('Discount:', discount)

extra_charges = 0
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied')
else:
    print('No extra charges will be applied')
print('Extra charges:', extra_charges)

if age >= 21 or age >= 18 and (show_time != 'Evening' or is_member):
    print('Ticket booking condition satisfied')

    service_charges = 0
    if seat_type == 'Premium':
        service_charges = 5
    elif seat_type == 'Gold':
        service_charges = 3
    else:
        service_charges = 1
    print('Service charges:', service_charges)
    final_price=base_price + extra_charges +  service_charges - discount

    print("Final price of ticket:",final_price)
    print(f"thsnks for coming{name}")
else:
    print('Ticket booking failed due to restrictions')