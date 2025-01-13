#i wrote this code in pycharm to check along the way for errors in my code

#set variables
pet_type = "snake"
pet_name = "Luna"

#print sentence using an f-string
print(f"I have a {pet_type} and her name is {pet_name}")


#set the variables based on user inputs, including "int" for the numerical inputs
user_name = input("Enter your first name: ")
user_age = int(input("Enter your current age: "))
user_savings = int(input("Enter your yearly savings: "))

#print using f-string
print(f"Hello {user_name}! You are currently {user_age} years old.")
print(f"In 15 years you will be {user_age + 15}.")
print(f"After saving ${user_savings} for 5 years, you will have ${user_savings * 5}.")
print(f"Your average monthly savings is ${user_savings // 12}.")


#set variable equal to number of days in january
january_days = 31

#set variable for seconds in january to the number of days times 24h times 60min times 60sec
january_seconds = 31 * 24 * 60 * 60

#print the result using an f-string
print (f"The number of seconds in January is: {january_seconds}.")


#get input from user and set eggs variable to that numerical value
eggs = int(input("Enter the number of eggs: "))
#set remainder variable using % operator
remainder = eggs % 12

#print results using an f-string
print(f"This makes {eggs//12} dozen eggs with {remainder} left over")
