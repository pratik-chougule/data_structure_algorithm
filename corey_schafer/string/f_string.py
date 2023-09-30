first_name = "Pratik"
last_name = 'chougule'

sentence = "my name is {} {}".format(first_name, last_name)
print(sentence)

sentence2 = f'My name is {first_name.upper()} {last_name.upper()}'

print(sentence2)

person = {'name':'Pratik', 'age':28}

sentence3 = "My name is {} and i am {} years old".format(person['name'], person['age'])
print(sentence3)

sentence4 = f"My name is {person['name']} and i am {person['age']} years old"

print(sentence4)