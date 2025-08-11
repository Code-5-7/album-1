# #Create a program that generates a list of squares of numbers from 1 to 10.
#
# #for value in range(1,11):
#     #print(value * value)
# # f = open("age.txt","w")
# # f.close()
# # f = open("age.txt","r")
# # print(f.read())
# # f.close()
# # f = open("age.txt","a")
# # f.write("Martin")
# # f.close()
# # f = open("age.txt")
# # # print(f.read())
#
# Create a program that finds the maximum number in a list.

# lift = [2, 3, 4, 5, 6, 7, 8, 93,12,156]
# lift.append(100)
# # lift.pop()
# number = lift.pop()
# print(number)
# print(lift)
# number = lift[-1]
# print(number)
# max_nimber = max(lift)
# print(max_nimber)


# #Program to reverse a string
# text = input("enter a string to reverse: ")
# reversed_text = text[::-1]
# print(reversed_text)
#



# Write a program that checks if a string is a palindrome.
# while True:
#     text = input("Enter a word or 'quit' to quit: ").lower()  # Convert to lowercase immediately
#     if text == "quit":  # Compare with string "quit", not variable quit
#         break
#     reverse_text = text[::-1]
#     if text == reverse_text:
#         print(f"'{text}' is a palindrome")
#     else:
#         print(f"'{text}' is not a palindrome")

# Implement a simple to-do list application that allows adding and removing tasks.
#
#
#
# Create a program that simulates a basic bank account with deposit and withdrawal functions.
def calc():
    balance = 100000  # Starting balance
    while True:
        print("\nMake a choice:")
        print('1. Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Quit')

        choice = input("Choose: 1, 2, 3, 4: ")

        if choice == '4':
            print("Goodbye!")
            break
        elif choice == '1':
            print(f"Current Balance: {balance}")
        elif choice == '2':
            x = int(input('Enter Deposit: '))
            balance += x
            print(f"Deposit: {x} New Balance is {balance}")
        elif choice == '3':
            y = int(input('Enter Withdraw: '))
            if y > balance:
                print("Insufficient funds!")
            else:
                balance -= y
                print(f"Withdraw: {y} New Balance is {balance}")
        else:
            print("Invalid choice! Please try again.")


calc()




