# number = 120
# flim= 1.890
# print(number + flim)
storage = 1
flim = 1.2
flim = int(flim)
print(flim)
length = 34
width = 68 
area = (length + length) * (width + width)
print(area)
# Store your name in a variable and print it.

# Print the first and last character of a string.

# Reverse a string using slicing.

# Count how many characters are in a sentence.

# Convert a sentence to uppercase and lowercase
name = "fola"
print(name)
food = "nosrep trams dna tnegilletni yrev a era uoy neht siht daer nac uoy fi"
first_character = food[0]
last_character = food[-1]
print(first_character + last_character)
reverse = food[::-1]
print(reverse)
reverse = "".join(reversed(food))
print(reverse)
print(len(food))
uppercase_sentence = food.upper()
lowercase_sentence = uppercase_sentence.lower()
print(uppercase_sentence)
print(lowercase_sentence)
# Create two variables and compare them using ==, >, <.

# Write a program that checks if a number is greater than 10 and prints True or False.

# Check if a word equals "python"
numero_1 = 19.999999
numero_2 = 20
if numero_1 == numero_2:
    print("equal")
elif numero_1 > numero_2:
    print(f"{numero_1} is greater than {numero_2}")
elif numero_1 < numero_2:
   print(f"{numero_1} is less than {numero_2}")    
# Create two variables and compare them using ==, >, <.
# Write a program that checks if a number is greater than 10 and prints True or False.
# Check if a word equals "python"
if numero_1 > 10:
    print("true")
elif numero_1 < 10:
    print("false")
snake = "python"
if snake == "python":
    print("AHH ITS A PYTHON")
favorite_foods = ["rice","pizza","cake","corn","popcorn"]
print(favorite_foods)
print(favorite_foods[-1])
print(favorite_foods[0])
favorite_foods.append("bubblegum")
favorite_foods.remove("corn")
print(favorite_foods)
listo_of_numeros = [1,2,3,4,5,6,7,8,9,10]
sum_of_even_numero = 0
numero_sum_2 = 0
# for number in listo_of_numeros:
#     if number % 2 == 0:
#         sum_of_even_numero += number
# print(sum_of_even_numero)
# for number in listo_of_numeros:
#     if number % 2 == 1:
#         numero_sum_2 += number
# print(numero_sum_2)
length_of_list = len(listo_of_numeros)
index = 0
sum_up = 0
while index < length_of_list:
    sum_up += listo_of_numeros[index]
    index += 1
print(sum_up)
dictionary = {'name':"fola","age":10}
print(dictionary)
print(dictionary["name"])
print(dictionary.get("weevil", "kat"))
dictionary.update(name = 5)
dictionary.update({"bird":"pelican","cereal":"cinnamon toast crunch"})
print(dictionary)
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.pop("cereal"))
for key, value in dictionary.items():
    print(f"the key is {key}, and the value is {value}")