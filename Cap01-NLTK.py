#Pedro Lucca Monteiro Soares
#Exercícios referentes ao primeiro capítulo do livro: https://www.nltk.org/book/ch01.html
#Questões 4, 6, 7, 9, 10, 15, 19, 22, 24, 25, 26, 27, 28 e 29

import nltk
#nltk.download()
from nltk.book import *
from nltk.tokenize import word_tokenize

#Questao 4
def questao_4():
    print(len(text2)) #Número de palavras = 141576

#Questao 6
def questao_6():
    print(text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"]))
    #As primeiras duas personagens tem mais relevância no história do livro

#Questao 7
def questao_7():
    print("--\n")
    print(text5.collocations())
    #wanna chat; PART JOIN; MODE #14-19teens; JOIN PART; PART PART;
    #cute.-ass MP3; MP3 player; JOIN JOIN; times .. .; ACTION watches; guys
    #wanna; song lasts; last night; ACTION sits; -...)...- S.M.R.; Lime
    #Player; Player 12%; dont know; lez gurls; long time

#Questao 9
def questao_9():
    my_string = "Just a string for the exercise"
    #Letra a:
    my_string# Essa forma não printa nada
    print(my_string) #Essa forma printa no terminal
    #Letra b:
    print(my_string * 3)
    print((my_string + ' ') * 3) #Forma de corrigir
    #Just a string for the exercise
    #Just a string for the exerciseJust a string for the exerciseJust a string for the exercise
    #Just a string for the exercise Just a string for the exercise Just a string for the exercise

#questão 10
def questao_10():
    my_sent = ["teste", "exercicio", "nltk"]
    #Letra a
    an = ' '.join(my_sent)#Separa as palavras com um espaço vazio
    print(an)
    #Letra b
    an.split()#Tambem separa as palavras com um espaço vazio
    print(an)
    # Resultado "teste exercicio nltk"

#questão 15
def questao_15():
    x = [word for word in text5 if word.startswith("b")]
    x = sorted(x)
    print(x)
    #Resultado
    #['b', 'b', 'b', 'b', 'b', 'b', 'b-day', 'b/c', 'b4', 'b4', 'babay', 'babble', 'babblein', 'babe', 'babe', 'babe', 'babe', 'babe', 'babe', 'babe', 'babe', 'babe', 'babe', 'babe', 'babes', 'babes', 'babes', 'babi', 'babi', 'babies', 'babies', 'babiess', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 'baby', 
    #'baby', 'babycakeses', 'bachelorette', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'back', 'backatchya', 'backfrontsidewaysandallaroundtheworld', 'backroom', 'backup', 'bacl', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bad', 'bag', 'bag', 'bag', 'bagel', 'bagels', 'bahahahaa',

#questão 19
def questao_19():
    pass
    # sorted(set(w.lower() for w in text1))
    # sorted(w.lower() for w in set(text1))
    #A função set presente na primeira linha retira elementos dupliados antes de colocar em ordem alfabetica

#questão 22 e 24
def questao_22_e_24():
    fl = sorted([word for word in text5 if len(word) == 4])
    fdist = nltk.FreqDist(fl)
    print("22", fdist.most_common(15))#[('JOIN', 1021), ('PART', 1016), ('that', 274), ('what', 183), ('here', 181), ('....', 170), ('have', 164), ('like', 156), ('with', 152), ('chat', 142), ('your', 137), ('good', 130), ('just', 125), ('lmao', 107), ('know', 103)]
    #24 Letra a
    ise_words = [word for word in text6 if word.endswith("ise")] 
    print("a", ise_words) #['wise', 'wise', 'apologise', 'surprise', 'surprise', 'surprise', 'noise', 'surprise']
    #24 Letra b
    z_words = [word for word in text6 if 'z' in word.lower()]
    print("b", z_words)#['zone', 'amazes', 'Fetchez', 'Fetchez', 'ZOOT', 'ZOOT', 'ZOOT', 'ZOOT', 'Zoot', 'ZOOT', 'ZOOT', 'ZOOT', 'ZOOT', 'Zoot', 'Zoot', 'ZOOT', 'ZOOT', 'ZOOT', 'ZOOT', 'ZOOT', 'ZOOT', 'Zoot', 'Zoot', 'Zoot', 'Zoot', 'Zoot', 'Zoot', 'AMAZING', 'zoop', 'zoo', 'zhiv', 'frozen', 'zoosh']
    #24 Letra c
    pt_words = [word for word in text6 if 'pt' in word.lower()]
    print("c", pt_words)#['empty', 'aptly', 'Thpppppt', 'Thppt', 'Thppt', 'empty', 'Thppppt', 'temptress', 'temptation', 'ptoo', 'Chapter', 'excepting', 'Thpppt']
    #24 Letra d
    l_words = [word for word in text6 if word[1:].islower() and word[0].isupper()]
    print("d", l_words)#['Whoa', 'Halt', 'Who', 'It', 'Arthur', 'Uther', 'Pendragon', 'Camelot', 'King', 'Britons', 'Saxons', 'England', 'Pull', 'Patsy', 'We', 'Camelot', 'What', 'Ridden', 'Yes', 'You', 'What', 'You', 'So', 'We', 'Mercea', 'Where', 'We', 'Found', 'In', 'Mercea', 'The', 'What', 'Well', 'The', 'Are', 'Not', 'They', 'What', 'It', 'It', 'It', 'Well', 'Will', 'Arthur', 'Court', 'Camelot', 'Listen', 'In', 'Please', 'Am', 'It', 'African', 'Oh', 'African', 'European', 'That', 'Oh', 'Will', 'Camelot', 'But', 'African', 'Oh', 'So', 'Wait', 'Supposing', 'No', 'Well', 'They', 'What', 'Well', 'Bring', 'Bring',...]

#questão 25
def questao_25():
    sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']

    #Letra a
    print([word for word in sent if word.startswith("sh")])#['she', 'shells', 'shore']
    #Letra b
    print([word for word in sent if len(word) > 4]) #['sells', 'shells', 'shore']

#questão 26
def questao_26():
    pass
    #sum(len(w) for w in text1)
    #Calcula em a soma do numeros de letras em text1
    #Sim basta dividir pelo tamanho de text1

#questão 27
def questao_27():
    def vocab_size(text): 
        return len(set(text))

#questão 28
def questao_28():
    def percent(word, text):
        wcount = text.count(word)
        size = len(text)
        return (wcount/size)*100

#questão 29
def questao_29():
    print(set(text2) < set(text1))
    # Faz a comparação da quantidade de palavras diferentes  em text1 e text2 
    # retornando true caso text2 tenha mais palavras diferente
    #Serve para verificar a diversidade gramatical de um texto.




questao_25()