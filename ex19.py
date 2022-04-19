def cheese_and_crackers_bombone(cheese_count, boxes_of_crackers, bombone):
    print(f"You have {cheese_count} cheeses!")
    print(f"You hvae {boxes_of_crackers} boxes of crackers!")
    print(f"You have {bombone} bombona")
    print("Man thats enough for a party!")
    print("Get a blanket.\n")


print("We can just give the function numbers direclty:")
cheese_and_crackers_bombone(20, 30, 200)

print("OR, we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50
amound_of_bombone = 200

cheese_and_crackers_bombone(amount_of_cheese, amount_of_crackers, amound_of_bombone)

print("we can even do math inside too:")
cheese_and_crackers_bombone(10 + 20, 5 + 6, 190 + 10)

print("And we can combine the two, variables and math")
cheese_and_crackers_bombone(amount_of_cheese + 100, amount_of_crackers + 1000, amound_of_bombone + 36)