s = input("Enter a String: ")
result = dict()
upper = 0
lower = 0
special = 0
digit = 0
for i in s:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
    else:
        special +=1
result.update({"uppercase": upper,"lowercase": lower,"special_character": special,"numbers":digit})
print(result)
