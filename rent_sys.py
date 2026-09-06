## Writing a code to manage rent sys - Priyanshu Purohit
##inputs we need 
##rent, food , electicity, 
## charge per head
## person in flat
rent = int(input("enter your flat rent = "))
food = int(input("food amount = "))
electricity = int(input("enter electricity bill amount = "))
charge_per_unit =int(input("charge per unit of electricity = "))
person =int( input("no. of person in room = "))


total_bill = electricity * charge_per_unit

output = (food + rent + total_bill) // person

print("each person will pay =",output)

 