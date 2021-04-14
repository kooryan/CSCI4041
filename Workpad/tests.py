string1 = "hello"
string2 = "bye"

print(string1[0] > string2[0])

print(ord('z') - ord('a'))

for numbers in range(ord('a'), ord('z') + 1):
   # print(string2[0])
    print(numbers - 97)
    # print(chr(numbers))

flat_list = []
t = [['Apple'], ['Banana'], [], [], [], [], ['Grapes', 'Grapples'], [], [], [], [], [], [], [], [], ['Peach'], [], [], ['Strawberry'], [], [], [], [], [], []]
for sublist in t:
    for item in sublist:
        flat_list.append(item)

print(2 > 2)