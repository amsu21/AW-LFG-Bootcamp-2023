nos_list = [3, 1, 4, 2, 5]

even_count, odd_count = 0, 0

for numbers in nos_list:
    if numbers % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("The even numbers in the list are: ", even_count)
print("The odd numbers in the list are: ", odd_count)