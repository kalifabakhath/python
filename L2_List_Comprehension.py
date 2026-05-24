num = [i for i in range(10)]
print(num)

cubes = [i*i*i for i in num]
print(cubes)

odd = [i for i in num if i%2 != 0]
print(odd)

words = ["Python", "Java", "JavaScript", "C"]
word_lengths = [len(word) for word in words]
print(word_lengths)

n= [i for i in range(21) if i%2 == 0 or i==1]
r = [i*2 for i in n if i !=0]
print(r)

i = [[i*j for i in range(1,4)] for j in range(1,4) ]
print(i)

nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
j =[ num for row in nested for num in row if num > 4]

print(j)