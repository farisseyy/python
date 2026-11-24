names_inp=input("enter a list of names separated by spaces:")
names = names_inp.split()
count_a=''.join(names).lower().count('a')
print("total occurrence of 'a':",count_a)
