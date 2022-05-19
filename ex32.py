the_count = [1, 2, 3, 4, 5]
fruits = ['aples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
boje = ['crvena', 'plava', 'zuta']
# this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

for koja in boje:
    print(f"Boja je: {koja}")

for i in change:
    print(f"I got {i}")

elements = []
brojevi = []
for i in range(0,6):
    print(f"Adding {i} tot the list.")
    elements.append(i)

for ja in range(10,20):
    brojevi.append(ja)

for ja in brojevi:
    print(f"Broj je: {ja}")

for i in elements:
    print(f"Element was: {i}")
