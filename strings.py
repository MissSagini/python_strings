word = 'banana'
number = '45'
print(type(number))
print(word[4])
# print (word[2.5]) # errpr because index needs to be an interger
# print(word[12]) # cant get this as the last index is 5
print(len(word)) # this corrects the above chal. tells you the length of the word. 

last_index = len(word) - 1
print(last_index)
print(word[last_index])

# Slicing creates a substring
# [starting: stoppoint]

message = "Welcome to Python Programming"
print(len(message))
print(message[0:10])
print(message[6:10])
print(message[:10]) # start from zero
print(message[5:]) # start from the defined index to end
print(message[:]) # creates a copy of the string

number = '0725439354'
print(number[0::2])
# if you want to do from the last to first char, we use reverse 
print(number[::-1])
# message[1] = 'i' # strings are immutable. cant be changed
language = 'Pithon'
corrected = language[0] + 'y' + language[2]
print(corrected)
