value = int(input("Please enter the amount of money to withdraw:\n"))

if (value % 10 !=0) :
    print("please enter a value divisible by 10")
else:    
    if (value >= 100) :
        hundred = int(value/100)
        value = value % 100
        print("%d notes of 100€" %hundred)
        
    if (value >= 50) :
        fifty = int(value/50)
        value = value % 50
        print("%d notes of 50€" %fifty)
    
    if (value >= 20) :
        twenty = int(value/20)
        value = value % 20
        print("%d notes of 20€" %twenty)
    
    if (value >= 10) :
        ten = int(value/10)
        print("%d notes of 10€" %ten)