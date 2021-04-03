import random

#shuffle string characters
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercaseLetter1=chr(random.randint(65,90)) #Generate a random Uppercase letter
uppercaseLetter2=chr(random.randint(65,90)) #Generate a random Uppercase letter

# generate password using all the characters in random order

password = uppercaseLetter1 + uppercaseLetter2 
password = shuffle(password)

# print out the password

print("Your newly generated password is", password)
