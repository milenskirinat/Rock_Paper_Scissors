import random
from turtle import pos

user_action = input("Сделай выбор - камень, ножницы, бумага?")
possible_action = ["камень", "ножницы", "бумага"]
computer_action = random.choice(possible_action)

print("Вы выбрали " + user_action, "\nКомпьютер выбрал " + computer_action)

if user_action == computer_action:
	print("Оба играка выбрали", + user_action,":Ничья!")
elif user_action == possible_action[0] and computer_action == possible_action[1]:
	print("Камень бьет ножницы\nВы победитель, поздравляю!")
elif user_action == possible_action[0] and computer_action == possible_action[2]:
	print("Бумага бьет камень\nПобедил компьютер, хорошая была каточка!")
elif user_action == possible_action[1] and computer_action == possible_action[0]:
	print("Камень бьет ножницы\nПобедил компьютер, повезет в следующий раз бро!")
elif user_action == possible_action[2] and computer_action == possible_action[0]:
	print("Бумага бьет камент\nВы победитель, поздравляю!")
elif user_action == possible_action[1] and computer_action == possible_action[2]:
	print("Ножницы рассекают бумагу\nВы победитель, красаучик!")
elif user_action == possible_action[2] and computer_action == possible_action[1]:
	print("Ножницы рассекают бумагу\nНе фартануло тебе, не фартануло!")