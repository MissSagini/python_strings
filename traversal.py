word = 'banana'
index = 0

# while index < len(word):
#     char = word[index]
#     print(f'Index {index} contains: {char}')
#     index +1

for char in word:
    if char == 'a':
        index = index + 1
    print(index)
# for char in word:
#     print(char)
print('n' in word) # returns a boolean

email = 'saginicynthia2@gmail.com'
print('@gmail' in email)

fruit = 'Pineapple'
if fruit < 'banana':
    print('Pineapple comes first')

fruit = 'Pineapple'
if word < 'Pineapple':
    print('banana comes first')


