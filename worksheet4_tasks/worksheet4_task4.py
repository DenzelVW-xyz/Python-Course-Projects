selection = input(f"Please pick a stand: (wa, wc, m): ").lower().strip()

if selection == "wa":
    num_of_adults = int(input("Please enter the number of adults: "))
    num_of_children = int(input("Please enter the number of children: "))
    num_of_pensioners = int(input("Please enter the number of pensioners: "))
    
    child_total = (num_of_children * 12)
    adult_total = (num_of_adults * 25)
    pensioner_total = (num_of_pensioners * 18)
    total = (child_total + adult_total + pensioner_total)
    print(f"Your total is €{total}")

elif selection == "wc":
    num_of_adults = int(input("Please enter the number of adults: "))
    num_of_children = int(input("Please enter the number of children: "))
    num_of_pensioners = int(input("Please enter the number of pensioners: "))
    
    child_total = (num_of_children * 10)
    adult_total = (num_of_adults * 20)
    pensioner_total = (num_of_pensioners * 15)
    total = (child_total + adult_total + pensioner_total)
    print(f"Your total is €{total}")
        
elif selection == "m":
    num_of_adults = int(input("Please enter the number of adults: "))
    num_of_children = int(input("Please enter the number of children: "))
    num_of_pensioners = int(input("Please enter the number of pensioners: "))
    
    child_total = (num_of_children * 5)
    adult_total = (num_of_adults * 12)
    pensioner_total = (num_of_pensioners * 10)
    total = (child_total + adult_total + pensioner_total)
    print(f"Your total is €{total}")

else:
    print("Invalid Stand Chosen.")