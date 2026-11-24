str1 = input("Enter a string: ")

if len(str1) < 3:
    print(str1)

elif str1.endswith("ing"):
    print(str1 + "ly")

else:
    print(str1 + "ing")

