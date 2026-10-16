day = int(input('enter day in number : '))
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")
    case _:
        print(' didn"t understand pleas enter the number from one to seven proprly')
month = int(input('enter the month in  number: '))
day = int( input(' enter the day in number: '))
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")