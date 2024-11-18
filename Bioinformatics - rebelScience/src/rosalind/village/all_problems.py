
# installing python
import this

# variables and some arithmetics
a = 919 
b = 862

def hypotenuse(a,b):
    
    hyp = a**2 + b**2
    print(hyp)

hypotenuse(a,b)

# strings and lists

def slices(text,start1,stop1,start2,stop2):

    firstWord = text[start1:stop1+1]
    secondWord = text[start2:stop2+1]
    print(firstWord + " " + secondWord)

slices("7mkT0KQXovfA2toXunoJAevrHXGfnkDYbBmshGxw6TkHdBp11DIy6SGr1G47NgHc2DdnTIxQIWJTKwt9nmrxLpv6cFSternaJ9W4OaMjzg053lbTJoMJq1yFe5fDEe4piOeu99L4T8TIqfLCEehcyanochlorisAkK83Ku9v9vPbaiFDnrNX3ssBaHaGYlm.",90, 95, 147, 158)

# ======= conditions and loops ======

def oddsSum(start,stop):

    sum = 0

    if start >= stop:
        print("wrong range")
        return False
    else:
        for number in range(start,stop+1):
            if number%2 is not 0:
                sum += number
        print("total sum is ", sum)

oddsSum(4992, 9735)

# ==== working with files ====

outputFile = []

with open('src/rosalind/village/input.txt','r') as f:
    outputFile = [line for pos,line in enumerate(f.readlines()) if pos%2 !=0]

with open('src/rosalind/village/output.txt','w') as f:
    f.write(''.join([line for line in outputFile]))


# ==== Dictionaries ==== #

def wordCounter(text):

    counterDict = {}
    wordsList = text.split()
    keysList = counterDict.keys()
    for word in wordsList:
        if word in keysList:
            counterDict[word] += 1
        else:
            counterDict[word] = 1

    for k,v in counterDict.items():
        print(k,v)     

text = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"
wordCounter(text) 


