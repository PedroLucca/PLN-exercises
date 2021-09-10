#Pedro Lucca Monteiro Soares
#Exercícios referentes ao primeiro capítulo do livro: https://www.nltk.org/book/ch02.html
#Questões 4, 5, 8, 9, 17, 18, 19, 23a, 25

import nltk
from nltk.corpus import state_union
from nltk.corpus import wordnet as wn
#nltk.download()
from nltk.book import *
#from nltk.tokenize import word_tokenize

#Questao 4
def questao_4():
    print(state_union.raw().count('men')) # Frequencia de "men": 4656
    print(state_union.raw().count('women')) # Frequencia de "women": 141
    
#Questao 5
def questao_5():
    print(wn.synset('tree.n.01').member_meronyms()) # []
    print(wn.synset('tree.n.01').part_meronyms()) # [Synset('burl.n.02'), Synset('crown.n.07'), Synset('limb.n.02'), Synset('stump.n.01'), Synset('trunk.n.01')]
    print(wn.synset('tree.n.01').substance_meronyms()) # [Synset('heartwood.n.01'), Synset('sapwood.n.01')]
    print(wn.synset('tree.n.01').member_holonyms()) # [Synset('forest.n.01')]
    print(wn.synset('tree.n.01').part_holonyms()) # []
    print(wn.synset('tree.n.01').substance_holonyms()) # []
    print('-')
    print(wn.synset('mint.n.04').member_meronyms()) # []
    print(wn.synset('mint.n.04').part_meronyms()) # []
    print(wn.synset('mint.n.04').substance_meronyms()) # []
    print(wn.synset('mint.n.04').member_holonyms()) # []
    print(wn.synset('mint.n.04').part_holonyms()) # [Synset('mint.n.02')]
    print(wn.synset('mint.n.04').substance_holonyms()) # [Synset('mint.n.05')]

#Questao 8
def questao_8():
    names = nltk.corpus.names
    #for fileid in names.fileids():
        #for name in names.words(fileid):
    cfd = nltk.ConditionalFreqDist((fileid, name[-1]) for fileid in names.fileids() for name in names.words(fileid))
    cfd.plot()
    #Para homens: n
    #Para mulheres: a
    
#Questao 9
#def questao_9():
    #names = nltk.corpus.names
    #for fileid in names.fileids():
        #for name in names.words(fileid):
    #cfd = nltk.ConditionalFreqDist((fileid, name[-1]) for fileid in names.fileids() for name in names.words(fileid))
    #cfd.plot()
    #Para homens: n
    #Para mulheres: a

#Questao 17
def questao_17():
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text2 if w.lower() not in stopwords]
    fdist1 = FreqDist(content)
    print(fdist1.most_common(50))
    #[(',', 9397), ('.', 3975), ('"', 1506), (';', 1419), ("'", 883), ('."', 721), ('Elinor', 684), ('could', 568), ('Marianne', 566), ('Mrs', 530), ('would', 507), ('--', 461), ('said', 397), (',"', 396), ('-', 366), ('every', 361), ('one', 304), ('!', 289), ('much', 287), ('sister', 282), ('must', 279), ('Edward', 262), ('mother', 258), ('Dashwood', 252), ('time', 237), ('know', 230), ('Jennings', 230), ('might', 215), ('Willoughby', 215), ('?"', 213), ('think', 209), ('Miss', 208), ('though', 204), ('well', 191), ('thing', 185), ('Lucy', 185), ('never', 184), ('soon', 180), ('Mr', 178), ('see', 173), ('Colonel', 173), ('without', 171), ('nothing', 170), ('ever', 169), ('may', 169), ('good', 166), ('.--', 166), ('John', 163), ('first', 160), ('?', 160)]

def questao_18():
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text1 if w.lower() not in stopwords]
    list = bigrams(content)
    fdist1 = FreqDist(list)
    print(fdist1.most_common(50))
    #[(('.', '"'), 557), ((',', ','), 497), (('.', ','), 359), ((',', "'"), 304), ((';', ','), 271), (('."', '"'), 246), ((',', '"'), 182), (('whale', ','), 181), ((',', 'one'), 177), ((',', 'though'), 175), (('.', "'"), 165), ((',', 'like'), 158), (('?"', '"'), 146), ((',', 'would'), 145), ((',', 'sir'), 136), ((',"', 'said'), 135), ((';', "'"), 129), (('Sperm', 'Whale'), 118), ((',', 'Ahab'), 117), (('whale', '-'), 115), ((',', 'yet'), 110), (('Ahab', ','), 109), ((',', 'ye'), 107), (('sea', ','), 106), (('"', "'"), 106), (('man', ','), 104), (('say', ','), 104), (('ship', ','), 91), (('ye', ','), 91), (('.', 'CHAPTER'), 89), ((',', 'old'), 89), ((',', 'say'), 88), ((',', 
    #'seemed'), 88), (('head', ','), 87), ((',', 'still'), 86), ((',', 'must'), 84), (('Moby', 'Dick'), 83), ((',', 'whale'), 83), ((';', 'though'), 83), (('boat', ','), 82), (('whale', "'"), 82), (('Stubb', ','), 82), (('said', ','), 81), (('!', "'"), 81), (('ship', "'"), 81), (('old', 'man'), 80), ((',', 'Queequeg'), 79), (('Queequeg', ','), 78), (('time', ','), 77), (('."', '--'), 76)]


questao_18()