from PyDictionary import PyDictionary
import os
import time

dictionary=PyDictionary()

verde = '\033[1;32m'
reset = '\033[0;0m'
vermelho = '\033[1;31m'
bullet = '\u2022 '

def cls():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def main():
    cls()
    arte_ascii = '''                                                                          
██████  ██  ██████ ████████ ██  ██████  ███    ██  █████  ██████  ██    ██ 
██   ██ ██ ██         ██    ██ ██    ██ ████   ██ ██   ██ ██   ██  ██  ██  
██   ██ ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████ ██████    ████   
██   ██ ██ ██         ██    ██ ██    ██ ██  ██ ██ ██   ██ ██   ██    ██    
██████  ██  ██████    ██    ██  ██████  ██   ████ ██   ██ ██   ██    ██                                                                                                                                                                                   
'''
    print(verde+arte_ascii)
    word = input(bullet+verde+"What word do you want to learn about? > ")
    if word == "":
        print(bullet+vermelho+"Type a word."+reset)
    else:
        print(bullet+verde+"Meanings: "+reset)
        print (dictionary.meaning(word))
        print(bullet+verde+"Synonyms: "+reset)
        print (dictionary.synonym(word))
        print(bullet+verde+"Antonyms: "+reset)
        print (dictionary.antonym(word))
    voltar = input(bullet+verde+"Want to restart? y/n > ")
    if voltar == "y":
        main()
    elif voltar == "n":
        print(bullet+verde+"Thanks for using my simple program!"
                            " Credits to Pepes and PyDictionary")
        time.sleep(5)
        quit()
    else:
        quit()

if __name__ == '__main__':
	main()
