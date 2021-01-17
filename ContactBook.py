

def contact_book():
	rows, cols = int(input("Please enter initial number of contacts: ")), 4

	phone_book = []
	print(phone_book)
	for i in range(rows):
		print("\nEntering contact %d details " % (i+1))

		print("....................................................................")
		temp = []
		for j in range(cols):

			if j == 0:
				temp.append(str(input("Enter name*: ")))

			if j == 1:
				temp.append(int(input("Enter number*: ")))

			if j == 2:
				temp.append(str(input("Enter e-mail address: ")))

			if j == 3:
				temp.append(str(input("Enter address: ")))

		phone_book.append(temp)

	print(phone_book)
	return phone_book


def menu():

	print("********************************************************************")
	print("\t\t\tMenu")
	print("********************************************************************")
	print("\tYou can now perform the following operations on this phonebook\n")
	print("1. Add a new contact")
	print("2. Remove an existing contact")
	print("3. Search for a contact")
	print("4. Display all contacts")
	print("5. Edit contact")
	print("6. Exit phonebook")

	choice = int(input("Please enter your choice: "))

	return choice


def add(pb):

	dip = []
	for i in range(len(pb[0])):
		if i == 0:
			dip.append(str(input("Enter name: ")))
		if i == 1:
			dip.append(int(input("Enter number: ")))
		if i == 2:
			dip.append(str(input("Enter e-mail address: ")))
		if i == 3:
			dip.append(str(input("Enter address: ")))
	pb.append(dip)

	return pb


def remove(pb):
	query = str(input("Please enter the name of the contact you wish to remove: "))

	temp = 0

	for i in range(len(pb)):
		if query == pb[i][0]:
			temp += 1
			print(pb.pop(i))
			print("This query has now been removed")
			return pb
	if temp == 0:
		print("Sorry, you have entered an invalid query.")

		return pb


def search(pb):
    choice = 1
    temp = []
    check = -1

    if choice == 1:
        query = str(
            input("Please enter the name of the contact you wish to search: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])

    if check == -1:
        return -1
    else:
        display_all(temp)
        return check

def display_all(pb):
	if not pb:
		print("List is empty: []")
	else:
		for i in range(len(pb)):
			print(pb[i])


def edit(pb):
	print("You are here to search")
	d = search(pb)

	choice = int(input("Enter criteria you want to edit\n\n\n1. Name\n2. Number\n3. Email-id\n4. Address"))
	
	if choice == 1:
		print(pb[d][0])
		name = str(input("Enter name"))
		pb[d][0] = name
		
	elif choice == 2:
		print(pb[d][1])
		no = int(input("Enter the number"))
		pb[d][1] = no
	
	elif choice == 3:
		print(pb[d][2])
		em = str(input("Enter the email"))
		pb[d][2] = em
	
	elif choice == 4:
		print(pb[d][3])
		ad = str(input("Enter the address"))
		pb[d][3] = ad
	
	else:
		print("Invalid edit criteria")
		1
		return -1
    
  


def endnote(): 

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 
	print("Arav's Contact Diary closing.......") 	
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 




print("\t\t\tArav's Contact Diary") 
print("...................................") 
print("...................................") 

ch = 1
pb = contact_book() 
while ch in (1, 2, 3, 4,5): 
	ch = menu() 
	if ch == 1: 
		pb = add(pb) 
	elif ch == 2: 
		pb = remove(pb) 
	elif ch == 3: 
		 d = search(pb) 
		 if d == -1:
			 print("The contact does not exist. ") 
	elif ch == 4: 
		display_all(pb) 
	elif ch == 5: 
		edit(pb) 
	else: 
		endnote() 
