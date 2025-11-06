fruits =  ["apple", "banana" , "orange", "grape", "kiwi"]
#print each fruit
for fruit in fruits:
    print(fruit)

for fruit in fruits:
    if len(fruit)>5:
        print("long fruit:", fruit)

count = 0
for fruit in fruits:
    if fruit.startswith("a"): 
        count += 1
print("number of fruits starting with 'a':", count)

new_fruit = input("Enter the name of a new fruit to add:")
fruits.append(new_fruit)
print("Updated fruit list:", fruits)