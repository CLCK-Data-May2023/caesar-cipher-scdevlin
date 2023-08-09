shift = input("Please enter the number of places to shift:")
sentence = input("Please enter a sentence:")
sentence = sentence.lower()

abc = "abcdefghijklmnopqrstuvwxyz"
shifted_abc = abc * 2
if shift.isdecimal() and int(shift) <= 25:
	for letter in sentence:
		if letter in abc:
			encrypted_sentence += shifted_abc[abc.find(letter) + int(shift)]
		else:
			encrypted_sentence += letter
        print("The encrypted sentence is:", encrypted_sentence)
        
else:
	print("You need to enter a number between 0 and 25!")
