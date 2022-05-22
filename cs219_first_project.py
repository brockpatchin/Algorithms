from random import choice


def insult_this_fool(name, age):
	adjectives = ["wet", "big", "false", "foul", "greasy", "infectious", "kindless", "lecherous", "smelly", "vociferous", "diabolical", "non-unique", "lacking-any-brain-cells"]
	nouns = ["turnip", "dog", "bed-presser", "biscuit", "boar-pig", "bull's-pizzle", "carbuncle", "coward", "death-token", "eel-skin", "fustilarian", "harlot", "hog", "horseback-breaker"]

	adjective = choice(adjectives)
	noun = choice(nouns)

	print(name + " is a " + adjective + " " + noun + ".")


print("Hi, What is your name?")
name = input()

print("Hi " + name + ", how old are you?")
age = input()

insult_this_fool(name, age)


