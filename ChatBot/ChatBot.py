# chatbot.py
import datetime

# Етап 1
bot_name = "DICT_Bot"
birth_year = datetime.datetime.now().year

# Виведення привітання
print(f"Hello! My name is {bot_name}.")
print(f"I was created in {birth_year}.")

# Етап 2
# Питання користувача та збереження введеного імені
user_name = input("Please, remind me your name.\n> ")

# Виведення вітання з іменем користувача
print(f"What a great name you have, {user_name}!")


# Етап 3
# Вгадування віку користувача
print("Let me guess your age.")
remainder3 = int(input("Enter remainder of dividing your age by 3.\n> "))
remainder5 = int(input("Enter remainder of dividing your age by 5.\n> "))
remainder7 = int(input("Enter remainder of dividing your age by 7.\n> "))

# Визначення віку за формулою
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

# Виведення результату
print(f"Your age is {your_age}; that's a good time to start programming!")


# Етап 4
# Підрахунок від 0 до введеного числа
user_number = int(input("Now I will prove to you that I can count to any number you want.\n> "))
for i in range(user_number + 1):
    print(f"{i}!")
print("Completed, have a nice day!")

# Етап 5
# Тестування програмування
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# Перевірка відповіді користувача
correct_answer = "2"
user_answer = input("> ")

while user_answer != correct_answer:
    print("Please, try again.")
    user_answer = input("> ")

# Виведення результату
print("Congratulations, have a nice day!")

