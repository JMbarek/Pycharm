import operator
import random
from collections import defaultdict
import itertools

abc = [chr(a+97) for a in range(26)]
umlaute =['ä','ü','ö','ß']
germanAlphabet = abc + umlaute

###############################################
###Verify if a Word is existing in the german dictionary
def getWordFromDictByLength(length, word):
    newList = list()
    with open('Dictionnary.txt') as f:
        for line in f:
            if len(line) == length+1:
                newList.append(str(line).lower().replace("\n", ""))
    for i in newList:
        if i == word:
            return word
############################################################

################### Open a file
f = open('text.txt', 'r')
verschtext = f.read()

#############################delete all unknown caracters
unencyptedText1=""
for i in verschtext.lower():
    if (i in germanAlphabet or i == " "):
        unencyptedText1 +=i
############################delete all unknown words
unencyptedText=""
for word in unencyptedText1.split():
    if (getWordFromDictByLength(len(word), word)== word):
        unencyptedText += word.lower()+" ";
#########################################################

k = germanAlphabet[:]
print(k)
random.shuffle(k)
WB = dict(zip(germanAlphabet,k))
print(WB)
lowerUnencyptedText= unencyptedText.lower().replace("  "," ").replace("\n"," ")
print(lowerUnencyptedText)


#####################################################################
# hier wird ein verschlüsselte Text erzeugt ##########################
#####################################################################
encrytedText=''
for c in lowerUnencyptedText:
    if (c !=' '): encrytedText = encrytedText + WB[c]
    else: encrytedText = encrytedText + ' '

print(encrytedText)
#####################################################################

germanLetterFrequency = ["e","n","i","r","s","t","a","h","d","u","l","c","g","m","o","b","w","f","k","z","v","p","ü","ä","ß","ö","j","y","x","q"]

################################################################
# rechnen Wie viel mal tritt ein Character  im verschlüsselten Text auf ?
inTextFrequency =[]
for ca in germanAlphabet:
    inTextFrequency.append(encrytedText.count(ca))
print(inTextFrequency);

#######################################################################
### Erzeugung von einem dict, das  als key (the Character) hat und als value (die Auftritt wahrscheinlichkeit) hat.
#######################################################################
WB_inTextFrequency = dict(zip(germanAlphabet,inTextFrequency))
print(WB_inTextFrequency);

################################################################################
######### steigend Sortierung des Dict  nach Value(die Auftritt-Wharscheinlichkeit)
sorted_dic_list = sorted(WB_inTextFrequency.items(), key=operator.itemgetter(1))
#################################################################################
###  get all the Values after ascendant Sorting
### (eine Liste von characters, die absteigend sortiert sind nach Eintrittwahrscheinlichkeit)
#################################################################################
reversed_sorted_list=[]
for i in reversed(sorted_dic_list): reversed_sorted_list.append(i)
print("The sorted letter by high apparent frequency at the beginning");
print(reversed_sorted_list);

# ###save the letters which have the same frequency##################
# # diese Methode erzeugt ein Dict, das dict enthält als Value ( die Characters, die gleiche Auftrittwharscheinlichkeit)
# # und als key die Anzahl ( der AuftrittWahkeit )
# ####################################################################
# sameFrequencyDic = defaultdict(list)
# dct = dict(reversed_sorted_list)
# print(dct);
# for key, value in dct.items():
#     # print (key, value)
#     actualVal = value
#     for key2, value2 in dct.items():
#         if ((key != key2 ) and (value == value2 )):
#             if (key not in sameFrequencyDic[str(value)]):sameFrequencyDic[str(value)].append(key)
#             if (key2 not in sameFrequencyDic[str(value)]):sameFrequencyDic[str(value)].append(key2)
# print("Dictionnary of the letters with the same freqency");
# print(sameFrequencyDic);
# ###################################################################

###  Python: changing value in a tuple ##############################
allKeys=[]
for i, v in enumerate(reversed_sorted_list):
    lst = list(v)
    allKeys.append(lst[0])
print("the frequent letter in Cipher Text:");
print(allKeys);

#####################################################################
###  Erste entschlüsslung Versuch
#####################################################################
WB_correspendance = dict(zip(allKeys,germanLetterFrequency))
print("WB_correspendance:");
print(WB_correspendance);

firstDecryptedVersion=""
for c2 in encrytedText:
    if (c2 != ' '):
        firstDecryptedVersion = firstDecryptedVersion + WB_correspendance[c2]
    else:
        firstDecryptedVersion = firstDecryptedVersion +' '

print(lowerUnencyptedText);
print(firstDecryptedVersion);
firstOfAlldecryptedText = firstDecryptedVersion;
### first comparing with German Dictionnary ################################

# #this function count how many letter with same frequency in a Word
# def containTwoLetterSameFrequence(word, sameFrequencyDic):
#     for key, value in sameFrequencyDic.items():
#         c = 0
#         y = []
#         for i, content in enumerate(word):
#             if ( content in value):
#                 c += 1;
#                 y.append(i)
#                 if (c>=2):
#                     print(i);
#         if (c ==2):
#             print(value)
#             print("The word "+ word +" have "+ str(c)+" characters with same frequency with Indexes ="+ str(y) );
#             return y

######################################################################
def getNumberDifferences(a,b):
    u = zip(a, b)
    y = []
    for i, j in u:
        if i != j:
            y.append(j)
    return len(y)


# list of the character that must be not changed
characterToNotpermute =""

def getMatchedWordfromDict(word):
    newList = list()
    differencesDic = defaultdict(list)
    with open('Dictionnary.txt') as f:
        for line in f:
            if len(line) == len(word) + 1:
                newList.append(str(line).lower().replace("\n", ""))
    for i in newList:
        # print(i)
        differencesDic[str(i)].append(getNumberDifferences(i,word))
    # sort dictionary by value
    sorted_differencesDic = sorted(differencesDic.items(), key=operator.itemgetter(1))
    print(sorted_differencesDic)
    l = [str(i[0]) for i in sorted_differencesDic]
    if str(l[0]) != word:
        return str(l[0]);
    else: return "Guessed";

######################################################################
def differencePositionsIn2Words(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]
######################################################################
# diese methode ermöglicht den Tausch von characters in einem Text ###
######################################################################
def permuteCharactersInText(text, cToReplace, cNew):
    text = text.replace(cToReplace, '_')
    text = text.replace(cNew, cToReplace)
    text = text.replace('_', cNew)
    return text
######################################################################
######################################################################
######################################################################
### eine liste von allen entdeckten gefunden words  ##################
wordsToNotpermute = list()
### entfernen duplizierten charecters in Word  #######################
def getAllCharectersFromWords():
    notToPermuteCharecters=""
    for i in wordsToNotpermute:
        notToPermuteCharecters+=i
    return ''.join(ch for ch, _ in itertools.groupby(notToPermuteCharecters))
######################################################################


secondDecryptedVersion = firstDecryptedVersion
i=1
while (i<5):
    # erstmal versuchen wir alle entdeckte Worte in einer Liste zu sammelen
    # und diese worte intakt zu lassen. sogar die Characters in diesem Worte müssen nicht getauscht werden.
    for word in secondDecryptedVersion.split():
        matchedWord = getMatchedWordfromDict(word)
        # if not (isinstance(matchedWord, str)):
        if ( matchedWord == "Guessed"):
            wordsToNotpermute.append(word)

    for word in secondDecryptedVersion.split():
        # diese Method sucht alle Worte mit den gleichen Längen und packt sie in einer Liste.
        # denn, suchen wir in dieser Liste das entsprechende Wort, dieses wort muss ein Kriterium respektieren.
        # das Kriterium ist so : die 2 Worte müssen die minimale Anzahl von differents Characters haben,
        #  wenn wir die characters der Worte paarweise vergleichen.
        # diese Methode nehmt "word" aus dem zuentschlüsselten text
        # und gibt zurück das entsprechende Wort in dem Fall wo eines gefunden ist  und liefert nix, wenn das wort ist shon entdeckt.
        matchedWord = getMatchedWordfromDict(word)
        if (isinstance(matchedWord, str) and word not in wordsToNotpermute ):
            print("for the word : " + word + " ***** matched word =" + matchedWord)
            positionsToPermute = differencePositionsIn2Words(word, matchedWord)
            s1 = matchedWord[int(positionsToPermute[0])]
            s2 = word[int(positionsToPermute[0])]
            if (s2 not in getAllCharectersFromWords()):
                secondDecryptedVersion = permuteCharactersInText(secondDecryptedVersion, s1, s2)
                # print(firstDecryptedVersion)
    i+=1


print("the Plain Text is:");
print(unencyptedText);
print("the encrypted Text is:");
print(encrytedText);
print("the first decrypted vesion Text is:");
print(firstDecryptedVersion);
print("the second decrypted vesion Text is:");
print(secondDecryptedVersion);






