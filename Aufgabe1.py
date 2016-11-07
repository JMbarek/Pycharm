import codecs
import random
import operator
from collections import defaultdict

abc = [chr(a+97) for a in range(26)]
# umlaute =['ä','ü','ö',' ','ß']
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
#######################################

# unencyptedText = "Die Bedienungsanleitung eines Fahrzeugs kann einige hundert Seiten umfassen. Um die Unterlagen übersichtlicher und benutzerfreundlich zu gestalten, werden umfangreichere Ausstattungen wie Navigationssystem, audiovisuelle Systeme oder Telefon oft in separaten Heften beschrieben. Die meisten Bedienungsanleitungen beschreiben alle möglichen Ausstattungen eines Fahrzeugs. Der Kunde muss dann die für seine Fahrzeugausstattung zutreffenden Texte und Daten selber heraussuchen, was sehr umständlich ist und zu Missverständnissen oder sogar zu Bedienungsfehlern führen kann"
# uncyptedText = "Jede gute Geschichte berührt. Umso mehr, wenn sie elementare Werte, die jeder von uns in sich fühlt, bewusst werden lässt und wenn sie zu spontanen Einsichten und Erkenntnissen führt. Als Kinder haben wir viel Weisheit aus Märchen, Sagen und Parabeln gelernt. Dieser Prozess hört nicht auf, wenn wir erwachsen sind. Fast alle grossen Bücher der Weltgeschichte, von der Bibel über die Bhagavadgita bis hin zum Tao Te King sind in Form von Metaphern, Geschichten und Gleichnissen verfasst. Leider finden wir oft in im Alltag kaum die Zeit, inspirative Geschichten zu lesen, darüber nachzudenken und daraus Gewinn für die Gestaltung unseres Lebens zu ziehen. Gönnen Sie sich also häufiger mal eine kleine Auszeit, um sich von einer guten Geschichte berühren und auch inspirieren zu lassen, beispielsweise von der einen oder anderen der Kleinen Weisheitsgeschichten, so wie ich sie in den monatlichen Newslettern für Sie gesammelt habe"


k = germanAlphabet[:]
print(k)
random.shuffle(k)
WB = dict(zip(germanAlphabet,k))
print(WB)
lowerUnencyptedText= unencyptedText.lower().replace("  "," ").replace("\n"," ")
print(lowerUnencyptedText)

encrytedText=''
for c in lowerUnencyptedText:
    if (c !=' '): encrytedText = encrytedText + WB[c]
    else: encrytedText = encrytedText + ' '

print(encrytedText)
germanLetterFrequency = ["e","n","i","r","s","t","a","h","d","u","l","c","g","m","o","b","w","f","k","z","v","p","ü","ä","ß","ö","j","y","x","q"]

################################
inTextFrequency =[]
for ca in germanAlphabet:
    inTextFrequency.append(encrytedText.count(ca))

print(inTextFrequency);

WB_inTextFrequency = dict(zip(germanAlphabet,inTextFrequency))
print(WB_inTextFrequency);
# sort on values a representation of a dict
sorted_dic_list = sorted(WB_inTextFrequency.items(), key=operator.itemgetter(1))



reversed_sorted_list=[]
for i in reversed(sorted_dic_list): reversed_sorted_list.append(i)
print("The sorted letter by high apparent frequency");
print(reversed_sorted_list);

###save the letters which have the same frequency###
sameFrequencyDic = defaultdict(list)
dct = dict(reversed_sorted_list)
print(dct);
for key, value in dct.items():
    # print (key, value)
    actualVal = value
    for key2, value2 in dct.items():
        if ((key != key2 ) and (value == value2 )):
            if (key not in sameFrequencyDic[str(value)]):sameFrequencyDic[str(value)].append(key)
            if (key2 not in sameFrequencyDic[str(value)]):sameFrequencyDic[str(value)].append(key2)
print("Dictionnary of the letters with the same freqency");
print(sameFrequencyDic);
#######################################################

###  Python: changing value in a tuple
allKeys=[]
for i, v in enumerate(reversed_sorted_list):
    lst = list(v)
    allKeys.append(lst[0])
print("the frequent letter in Cipher Text:");
print(allKeys);

#######################################################

WB_correspendance =dict(zip(allKeys,germanLetterFrequency))
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

### first comparing with German Dictionnary ###

###
#this function count how many letter with same frequency in a Word
def containTwoLetterSameFrequence(val, sameFrequencyDic):
    for key, value in sameFrequencyDic.items():
        c = 0
        for i in val:
            if (i in value):
                c += 1;
                print(i);
        if ( c >=2):
            print (value)
            print("The word "+val+" qre "+ str(c)+" caracters with same frequency");
            return c

######################################################################
def getNumberDifferences(a,b):
    u = zip(a, b)
    y = []
    for i, j in u:
        if i != j:
            y.append(j)
    print('the number of differences', len(y))
    return len(y)

def getMatchedWordfromDict(word):
    newList = list()
    with open('Dictionnary.txt') as f:
        for line in f:
            if len(line) == len(word) + 1:
                newList.append(str(line).lower().replace("\n", ""))
    for i in newList:
        if getNumberDifferences(i ,word)==1:
            return word

######################################################################
def differencePositionsInStrings(a, b):
    return [i for i in range(len(a)) if a[i] != b[i]]
######################################################################
######################################################################

def permuteCharacterInString(s, old, new):
    s = s.replace(old, '#')
    s = s.replace(new, old)
    s = s.replace('#', new)
    return s
######################################################################
######################################################################
######################################################################
######################################################################

# wordsList = list()
# wordsList = firstDecryptedVersion.split(' ')
# print(wordsList);
#
#
# guessedRightWords = list()
# for i, val in enumerate(wordsList):
#     if(getWordFromDictByLength(len(val), val) == val):
#         guessedRightWords.insert(i,val)
#         print("the word "+ val +" is found");
#     d = containTwoLetterSameFrequence(val, sameFrequencyDic)
#     if((val not in guessedRightWords) and ( isinstance( d, int ) and d >=2)):
#         print("the word " + val +" have "+ str(d) +" letter with same frequency");
# # sameFrequencyDic

# secondDecryptedVersion=""
foundDifference = True
while foundDifference:
    for word in firstDecryptedVersion.split():
        if ( isinstance( getMatchedWordfromDict( word), str )):
            matchedWord = getMatchedWordfromDict(word)
            positionsToPermute = differencePositionsInStrings(word, matchedWord)
            # get the character to swap
            if ( len(positionsToPermute) > 0):
                s1 = matchedWord[int(positionsToPermute[0])]
                s2 = word[int(positionsToPermute[0])]
                # print("swap : " + s1 + " to " + s2)
                firstDecryptedVersion = permuteCharacterInString(firstDecryptedVersion, s1, s2)
                foundDifference = True
            # break out of the loop and re run the outer loop
            break
        foundDifference = False

    # if (getWordFromDictByLength(len(word), word) == word):
    #     secondDecryptedVersion += word+" "
    # elif (isinstance( containTwoLetterSameFrequence( word, sameFrequencyDic), int ) and containTwoLetterSameFrequence(word, sameFrequencyDic) >=2):
    #     secondDecryptedVersion += "2SAME "

        # secondDecryptedVersion += getMatchedWordfromDict(word)+" "

print("the Plain Text is:");
print(unencyptedText);
print("the encrypted Text is:");
print(encrytedText);
print("the first decrypted vesion Text is:");
print(firstDecryptedVersion);
# print("the second decrypted vesion Text is:");
# print(secondDecryptedVersion);









#
# ######################################################################
# def sortStringListByLength(myList):
#     newList = list(myList)
#     newList.sort(key = lambda s: len(s))
#     newList.reverse()
#     return newList
# ######################################################################
# def readFileToString(filename):
#     f = open (filename, "r")
#     f = codecs.open(filename, "r", "utf-8")
#     s_unicode = f.read()
#     f.close()
#     return s_unicode
# ######################################################################
# def filterListByLengthOfElements(myList, length):
#     newList=list()
#     for s in myList:
#         if (len(s) == length):
#             newList.append(s)
#     return newList
# ######################################################################
# def levenshtein(s1, s2):
#     if len(s1) < len(s2):
#         return levenshtein(s2, s1)
#
#     # len(s1) >= len(s2)
#     if len(s2) == 0:
#         return len(s1)
#
#     previous_row = range(len(s2) + 1)
#     for i, c1 in enumerate(s1):
#         current_row = [i + 1]
#         for j, c2 in enumerate(s2):
#             insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
#             deletions = current_row[j] + 1       # than s2
#             substitutions = previous_row[j] + (c1 != c2)
#             current_row.append(min(insertions, deletions, substitutions))
#         previous_row = current_row
#
#     return previous_row[-1]
#
#
# def findBestMathWord(original, candidates):
#     # initial bestMatch is the first candidate
#     distance = levenshtein(original, candidates[0])
#     bestMatch = candidates[0]
#     for candidate in candidates:
#         newDistance = levenshtein(original, candidate)
#         #print("newDistance: " + str(newDistance) + " from: " + original + " to: " + candidate)
#         if (newDistance < distance):
#             bestMatch = candidate
#             distance = newDistance
#     #print("bestMatch: " + bestMatch + " (distance : " + str(distance) + " )")
#     return bestMatch

# ######################################################################

#
# ######################################################################
# # read the local dictionary
# sDictionary = readFileToString("Dictionnary.txt")
# lDictionary = sDictionary.split()
# ######################################################################
#
# foundDifference = True
# while foundDifference:
#     # get a list of all words in the text
#     listWords = firstDecryptedVersion.split()
#     listWords = sortStringListByLength(listWords)
#
#     for word in lDictionary:
#         sameLengthWords = filterListByLengthOfElements(listWords, len(word))
#         print(word + ": found words with same length: " + str(sameLengthWords))
#         print("get best math from list: " + str(sameLengthWords))
#         bestMatchWord = findBestMathWord(word, sameLengthWords)
#         print("bestMatch: " + word + " -> " + bestMatchWord)
#         swapPositions = differencePositionsInStrings(word, bestMatchWord)
#         # found a difference?
#         if len(swapPositions) > 0:
#             # only use the first swap position to avoid mistakes and double swaps
#             pos = swapPositions[0]
#             # get the character to swap
#             s1 = bestMatchWord[pos]
#             s2 = word[pos]
#             #print("swap : " + s1 + " to " + s2)
#             sDecrypted = swapCharacterInString(firstDecryptedVersion, s1, s2)
#             foundDifference = True
#             # break out of the loop and re run the outer loop
#             break
#         foundDifference = False
#
#
#









