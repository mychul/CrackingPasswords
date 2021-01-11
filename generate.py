from itertools import product
from string import ascii_lowercase

f = open("Possible_output.txt","a")

# for x in range(1,3): #cycles through 1-6 not including 7, x represents size of the string generated
#     generated = ""
#     for y in alpha: #y represents the current letter to generate with
#         generated += y
#         if len(generated)==int(x):
#             f.write(generated + "\n")
#             generated = ""
for x in range(1,7):
    generated=(''.join(i) for i in product(ascii_lowercase, repeat = x))
    for y in generated:
        f.write(y)
        f.write("\n")
f.close()
        
