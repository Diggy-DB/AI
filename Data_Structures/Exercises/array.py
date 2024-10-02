# Exercise 1
exp = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print(exp[1]-exp[0])
# Time Complexity = O(1)

# 2. Find out your total expense in first quarter (first three months) of the year.
s = 0
for i in range(3):
    s += exp[i]
print(s)
# Time complexity = O(1)

# 3. Find out if you spent exactly 2000 dollars in any month
chk = False
for i in exp:
    if(i==2000):
        chk = True
        break
print(chk)
# Time complexity = O(n)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
exp.append(1980)
print(exp)
# Time complexity = O(1)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
exp[0+3]-=200
print(exp)
# Time complexity = O(1)



# Exercise 2
heros = ['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heros))
# Time complexity = O(1)

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)
# Time complexity = O(1)

# 3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)
# Time complexity = O(n)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)
# Time complexity = O(1)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)
# Time complexity = O(n^2)



# Exercise 3
mx = int(input('Enter the max number: '))
i=1
while(i<mx):
    print(i)
    i+=2
# Time complexity = O(n)
