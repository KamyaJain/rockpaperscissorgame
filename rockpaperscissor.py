#rock,paper,scissor game
from random import randint
choice=['r','p','s']
comp=choice[randint(0,2)]
while (True) :
	user = input("kamya : ").casefold()
	print("computer :",comp)
	if (user=='r') and (comp=='r'):
		print("Match draw")
	elif (user=='r') and (comp=='p'):
		print("Computer won the game")
	elif (user=='r') and (comp=='s'):
		print("Kamya won the game")

	elif (user=='s') and (comp=='s'):
		print("Match draw")
	elif (user=='s') and (comp=='r'):
		print("Computer won the game")
	elif (user=='s') and (comp=='p'):
		print("Kamya won the game")					

	elif (user=='p') and (comp=='p'):
		print("Match draw")	
	elif (user=='p') and (comp=='r'):
		print("Kamya won the game")
	elif(user=='p')	and (comp=='s'):
		print("Computer won the game")	

	else:	
		print("please enter valid input (r,s,p)")
	
	print('\n')
	again = input("want to play more? (yes/no)")
	print('\n')

	if (again=='yes') :
		continue
	else:
		print("Bye. See ya!")
		break