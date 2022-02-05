from importlib.machinery import WindowsRegistryFinder
import random

def msg_abertura():
        print('*********************************')
        print('***Welcome to The Hangman Game***')
        print('*********************************')

def secret_word():
        words = []
        with open('words.txt', 'r', encoding="utf-8") as arqv:
            for linha in arqv:
                linha = linha.strip()
                words.append(linha)

        numero = random.randrange(0, len(words))
        secret_word = words[numero].upper()
        return secret_word
    
def letras_certas_com(palavra):
        return['_' for letra in palavra]
    
def pede_chute():
       chute = input("Qual Letra?? ")
       chute = chute.strip().upper()
       return chute

def chute_correto(chute,letras_certas,secret_word):
        posicao = 0
        for letra in secret_word:
            if(chute.upper() == letra.upper()):
                letras_certas[posicao] = letra
            posicao += 1
    
def imprime_mensagem_vencedor():
         print("Congratulations! You Won!! ")
         print("       ___________      ")
         print("      '._==_==_=_.'     ")
         print("      .-\\:      /-.    ")
         print("     | (|:.     |) |    ")
         print("      '-|:.     |-'     ")
         print("        \\::.    /      ")
         print("         '::. .'        ")
         print("           ) (          ")
         print("         _.' '._        ")
         print("        '-------'       ")
    
def imprime_mensagem_perdedor(secret_word):
         print("Damn, you were hanged!")
         print("The word is {}".format(secret_word))
         print("    _______________         ")
         print("   /               \       ")
         print("  /                 \      ")
         print("//                   \/\  ")
         print("\|   XXXX     XXXX   | /   ")
         print(" |   XXXX     XXXX   |/     ")
         print(" |   XXX       XXX   |      ")
         print(" |                   |      ")
         print(" \__      XXX      __/     ")
         print("   |\     XXX     /|       ")
         print("   | |           | |        ")
         print("   | I I I I I I I |        ")
         print("   |  I I I I I I  |        ")
         print("   \_             _/       ")
         print("     \_         _/         ")
         print("       \_______/           ")


   
def desenha_forca(wrong):
        print("  _______     ")
        print(" |/      |    ")

        if(wrong==1):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
        
        if(wrong==2):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        if(wrong==3):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        if(wrong==4):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")
        
        if(wrong==5):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        if(wrong==6):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")
        
        if(wrong==7):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")
        
        print(" |            ")
        print("_|___         ")
        print()

def jogar():

    msg_abertura()
    secre_word = secret_word()
    letras_certas = letras_certas_com(secre_word)
    acertou = False
    enforcou = False
    wrong = 0
    letras_em_falta = len(letras_certas)

    print(letras_certas)

    while(not acertou and not enforcou):
        chute = pede_chute()

        if(chute in secre_word):
            chute_correto(chute,letras_certas,secre_word)
            letras_em_falta = str(letras_certas.count('_'))
            if (letras_em_falta == "0"):
                 print("Congratulation!!You found all the letters of the word '{}'".format(secre_word.upper()))
        else:
            wrong +=1
            print(letras_certas)
            print("Still missing to hit {} letters".format(letras_em_falta))
            print("You still have {} tries".format(7-wrong))
            desenha_forca(wrong)

        if wrong == 7:
            enforcou = True
            
        acertou = "_" not in letras_certas

        print(letras_certas)
    
    if (acertou):
        imprime_mensagem_vencedor()
    
    else:
        imprime_mensagem_perdedor(secre_word)
    
    print("Game Over")

jogar()