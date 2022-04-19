from sys import argv
script, user_name = argv
prompt = 'Odgovor: '

print(f"Hello {user_name}")
print("I would like to ask you some questions if u dont mind.")
print("Have you ever heard about Zork and Adventure games?")
heard = input(prompt)
print("Awesome! And in which store i can buy em?")
store = input(prompt)
print(f"So you {heard} about the games and that i can find them in {store} store")
