
infile = open("sometext.txt",'r') 
words = infile.read().split(" ") 
dictionary = {} 

for character in words: 
    if character.isalnum(): 

        if character in dictionary: 
            dictionary[character] = dictionary.get(character)+1
        else:
            dictionary[character] = 1 

dictionary = sorted(dictionary.items(), key=lambda x: x[1]) 


for character in dictionary: 
    print(character[0]+":"+str(character[1])+"\n")
