from string import*

def encipherCharacter(char, keyChar):
    offset = ord(keyChar) - ord('A')
    charCode = ord(char)
    newCharCode = charCode + offset
    if newCharCode > ord('Z'):
        newCharCode = newCharCode - numberOfLettersInAlphabet
    newChar = chr(newCharCode)
    return newChar

def decipherCharacter(char, keyChar):
    offset = ord(keyChar) - ord('A')
    charCode = ord(char)
    newCharCode = charCode - offset
    if newCharCode < ord('A'):
        newCharCode = newCharCode + numberOfLettersInAlphabet
    newChar = chr(newCharCode)
    return newChar

def filterLettersPass(aString):
    newString = ""
    for ch in aString:
        if ch in ascii_letters:
            newString = newString + ch
    return newString

def encipher(key):
    messageToEncipher = "aaabbbcccdddeeefffggghhhiiijjjkkkk"
    key = filterLettersPass(key)
    key = key.upper()
    upcaseMessageToEncipher = messageToEncipher.upper()

    encipheredMessage = ""
    for index in range(len(upcaseMessageToEncipher)):
        char = upcaseMessageToEncipher[index]
        keyChar = key[index % len(key)]
        if char in ascii_uppercase:
            newChar = encipherCharacter(char, keyChar)
        else:
            newChar = char
        encipheredMessage = encipheredMessage + newChar
    print(encipheredMessage)

def decipher(key):
    messageToDecipher = "RVY GFO ZW! POEF? USM MOSBGYO KKWX TIEADCI PHBPK SZ JRAJMOMZO LVGYHBRK?"
    key = filterLettersPass(key)
    key = key.upper()
    upcaseMessageToDecipher = messageToDecipher.upper()

    decipheredMessage = ""
    for index in range(len(upcaseMessageToDecipher)):
        char = upcaseMessageToDecipher[index]
        keyChar = key[index % len(key)]
        if char in ascii_uppercase:
            newChar = decipherCharacter(char, keyChar)
        else:
            newChar = char
        decipheredMessage = decipheredMessage + newChar
    print(decipheredMessage)



numberOfLettersInAlphabet = 26

# encipher("A A A")
# encipher("ABCDEFGHI")
decipher("THE HARVARD OF THE MIDWEST")
