# fruits = ["apple", "orange"]
# if "apple" in fruits:
#     print("ある")
# else:
#     print("ない")

numbers = [1,2,3,4,5,6]
odd_list = []
even_list = []
for number in numbers:
    if number % 2 == 1:
        odd_list.append(number)
    else:
        even_list.append(number)

print(odd_list)
print(even_list)