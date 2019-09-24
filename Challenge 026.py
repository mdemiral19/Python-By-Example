'''Challenge 026: Pig Latin takes the first consonant of a word, moves it to the end of the word and adds on an "ay".
If a word begins with a vowel you just addd "way" to the end. For example, pig becomes igpay, banana becomes ananabay,
and aadvark becomes aadvarkway. Create a program that will ask the user to enter a word and change it into Pig Latin. Make
sure the new word is displayed in lower case.'''

word = input('Please enter a word: ')
firstletter = word[0]
wordlength = len(word)
rest = word[1:wordlength]
if firstletter == 'a' or firstletter == 'e' or firstletter == 'i' or firstletter == 'o' or firstletter == 'u':
    newword = word + 'way'
    print(newword.lower())
else:
    newword = rest + firstletter + 'ay'
    print(newword.lower())