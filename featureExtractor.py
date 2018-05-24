from textatistic import Textatistic
import binascii
import math

def countAlpha(string):
    # returns number of alphabetical Characters in string
    alphas = "abcdefghijklmnopqrstuvwxyz"
    myString = string.lower()
    if (len(myString) < 1):
        return 0
    return len([l for l in myString if l in alphas])

def a2n(string):
    # returns ratio between Alphabetical and Other characters
    if(len(string) < 1):
        return 0
    return countAlpha(string)/len(string)

def countVowels(string):
    # returns number of vowels in string
    vowels = "aouei"
    myString = string.lower()
    if (len(myString) < 1):
        return 0
    return len([l for l in myString if l in vowels])

def v2c(string):
    #returns the ratio between vowels and consonants
    if(len(string) < 1):
        return -1
    total = countAlpha(string)
    v = countVowels(string)
    if(total<1):
        return -1
    return v/total

def entropy(string):
    #Calculates the Shannon entropy of a string
    prob = [float(string.count(c)) / len(string) for c in dict.fromkeys(list(string))]
    entropy = - sum([p * math.log(p) / math.log(2.0) for p in prob])
    return entropy

def entropy_ideal(length):
    #Calculates the ideal Shannon entropy of a string with given length
    prob = 1.0 / length
    return -1.0 * length * prob * math.log(prob) / math.log(2.0)

def entropyPercentage(string):
    #calculates percentage of entropy relative to the ideal
    return entropy(string)/entropy_ideal(len(string))

def extract(input_file, output_file):
    with open(output_file,'w') as output:
        with open(input_file,'r') as input:
            i = 0
            lines = input.readlines()
            output.write('len,cnt_alpha,cnt_nonAlpha,alpha_to_special,cnt_vowel,cnt_consonant,vowel_to_consonant,entropy,entropy_ideal,emtropy_percentage,fleschkincaid,smog,dalechall,gunningfog,sybl,hex\n')
            for line in lines:
                myLine = line.strip()
                if(myLine and len(myLine)>0):
                    alphas = countAlpha(myLine)
                    specials = len(myLine)-countAlpha(myLine)
                    alpha2numerical = a2n(myLine)
                    vowels = countVowels(myLine)
                    consonants = countAlpha(myLine) - countVowels(myLine)
                    vowel2consonant = v2c(myLine)
                    shannon = entropy(myLine)
                    ideal = entropy_ideal(len(myLine))
                    ent_percent = entropyPercentage(myLine)
                    try:
                        t = Textatistic(myLine+'.')
                        fleschkincaid = t.fleschkincaid_score
                        smog = t.smog_score
                        dalechall = t.dalechall_score
                        gunningfog = t.gunningfog_score
                        sybl = t.sybl_count
                    except ZeroDivisionError:
                        fleschkincaid = -1
                        smog = -1
                        dalechall = -1
                        gunningfog = -1
                        sybl = -1
                        pass
                    data = (str(len(myLine)) + ','
                              + str(alphas) + ','
                              + str(specials) + ','
                              + str(alpha2numerical) + ','
                              + str(vowels) + ','
                              + str(consonants) + ','
                              + str(vowel2consonant) + ','
                              + str(shannon) + ','
                              + str(ideal) + ','
                              + str(ent_percent) + ','
                              + str(fleschkincaid) + ','
                              + str(smog) + ','
                              + str(dalechall) + ','
                              + str(gunningfog) + ','
                              + str(sybl) + ','
                              + myLine.encode('utf-8').hex() + '\n')
                    output.write(data)
                    i += 1
                    print("%d/%d" % (i,len(lines)))



input_data = "Data/plain/data.txt"
output_data = "Data/features.csv"

input_data_neg = "Data/plain/data.neg.txt"
output_data_neg = "Data/features.neg.csv"

extract(input_data, output_data)
extract(input_data_neg, output_data_neg)