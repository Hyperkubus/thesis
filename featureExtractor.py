import textatistic
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
                    sybl = textatistic.sybl_counts(myLine)['sybl_count']
                    fleschkincaid = 205.82-84.6*sybl
                    smog = 3.1291+1.0430*math.sqrt(30*(sybl>2))

                    dccnt = textatistic.notdalechall_count(myLine)
                    dalechall = 19.4265*dccnt+0.0496

                    gunningfog = 0.4+40*(sybl>2)
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
                              + myLine.encode('utf-8').hex()+'\n')
                    output.write(data)
                    i += 1
                    print("%d/%d" % (i,len(lines)))



input_data = "Data/plain/data.txt"
output_data = "Data/features.new.csv"

input_data_neg = "Data/plain/data.neg.txt"
output_data_neg = "Data/features.new.neg.csv"

extract(input_data, output_data)
extract(input_data_neg, output_data_neg)