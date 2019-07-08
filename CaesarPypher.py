alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ''

print("\nWelcome to Project Caesar Cipher! This is one of the oldest cryptography methods \nthat has been known to be used by Julius Caesar himself during battle with his generals. \nYou can now encrypt or decrypt a message using this encryption method.")
option = input("\nPlease select an option: \ne. Encrypt\nd. Decrypt\nk. Find encryption rotation\nq. Quit the program\nOption: ")
while option not in ["e", "d", "q", "r"]:
	option = input("\nInvalid selection.\nPlease select an option:\ne. Encrypt\nd. Decrypt\nr. Find encryption rotation\nq. Quit the program.\nOption: ")
if option is "e":
  message = input('Please enter a message to encrypt: ').lower()

  rotation = input('Enter a rotation (1-26): ')
  rotation = int(rotation)
  
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + rotation) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character

  print('Your encrypted message is: ', newMessage, "\nThank you for using Caesar Cipher!")
elif option is "d":
  message = input('Please enter a message to decrypt: ').lower()

  rotation = input('Enter a rotation (1-26): ')
  rotation = int(rotation)

  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position - rotation) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character

  print('Your decrypted message is: ', newMessage, "\nThank you for using Caesar Cipher!")
elif option is "r":
  decrypted = input("Enter the decrypted message: ").lower()
  encrypted = input("Enter the encrypted message: ").lower()

  for character in decrypted:
    if character in alphabet:
      positionDecrypted = alphabet.find(character)
  for character in encrypted:
    if character in alphabet:
      positionEncrypted = alphabet.find(character)
  rotation = (positionEncrypted - positionDecrypted) % 26
  print("Your encryption rotation is", rotation, "\nThank you for using Caesar Cipher!")
  exit()
elif option is "q":
  exit("Thank you for using Caesar Cipher!")