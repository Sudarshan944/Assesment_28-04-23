#Problem 1

# Cost Estimate
number_book1 = int(input("Number of Introduction to Python Programming books:"))
number_book2 = int(input("Number of Python Libraries Cookbook books:"))
number_book3 = int(input("Number of Data Science in Python books:"))
if number_book1 < 0:
    print("Invalid input please enter positive number")
elif number_book2 < 0:
    print("Invalid input please enter positive number")
elif number_book3 < 0:
    print("Invalid input please enter positive number")
else:
    price1 = 499.0 * number_book1
    price2 = 855.0 * number_book2
    price3 = 645.0 * number_book3
    total = price1 + price2 + price3
    gst = total * 0.12
    delivery_charges = 250
    print("Total            :", total)
    print("GST (12%)        :", gst)
    print("Delivery Charges :", delivery_charges)
    print("--------------------------")
    print("Net Amount       :", (total+gst+delivery_charges))

#Problem 2

string1=input("string1 =").lower() # Take input
list1=[] # Take empty list
for character in string1:
    if character not in list1:
        list1.append(character)
print("uniqueLetters =",",".join(list1)) #Join them with comma between them
