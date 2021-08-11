word = input()
 
result = ''
for char in word:
    result = result + str(ord(char)-ord('A') + 1) + ' '
result = result[:-1]
 
print(result)