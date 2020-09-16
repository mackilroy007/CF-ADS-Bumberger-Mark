value = int(input("Please enter the amount of money to withdraw:\n"))

#Amount of bills in the ATM
n_hundred = 1
n_fifty = 5
n_twenty = 5
n_ten = 5

if (value > n_hundred*100+n_fifty*50+n_twenty*20+n_ten*10):
    print("Sorry, I don't have enough money")
elif (value % 10 !=0):
    print("Please enter a value divisible by 10")
else :   
    if (value >= 100) :
        if (n_hundred >= int(value/100)) :
            hundred = int(value/100)
            value = value % 100
        else :
            hundred = n_hundred
            value = value-n_hundred*100
        print("%d notes of 100€" %hundred)
            
    if (value >= 50) :
        if (n_fifty >= int(value/50)) :    
            fifty = int(value/50)
            value = value % 50
        else :
            fifty = n_fifty
            value = value-n_fifty*50
        print("%d notes of 50€" %fifty)
        
    if (value >= 20) :
        if (n_twenty >= int(value/20)) :    
            twenty = int(value/20)
            value = value % 20
        else :
            twenty = n_twenty
            value = value-n_twenty*20
        print("%d notes of 20€" %twenty)
    
    if (value >= 10) :
        if (n_ten >= int(value/10)) :    
            ten = int(value/10)
            value = value % 10
        else :
            ten = n_ten
            value = value-n_ten*10        
        print("%d notes of 10€" %ten)