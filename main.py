from PyDictionary import PyDictionary
import os

dictionary=PyDictionary()


def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    cls()
    word = input("What word do you want to learn about? > ")
    if word == "":
        print("Type a word.")
    else:
        print (dictionary.meaning(word))
        print (dictionary.synonym(word))
        print (dictionary.antonym(word))
    voltar = input("Want to restart? y/n > ")
    if voltar == "y":
        main()
    else:
        quit()

if __name__ == '__main__':
	main()
