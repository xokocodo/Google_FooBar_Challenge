def answer(chunk, word):
    new_chunks = [chunk]
    quit = False
    while not quit:
        chunks = set(new_chunks)
        new_chunks = []
        quit = True
        # for all of the possible chunks
        for chunk in chunks:
            #scan the whole chunk for occurances of the string
            for i in range(len(chunk)-len(word)+1):
                if chunk[i:i+len(word)] == word:
                    #if the word is found, keep going
                    quit = False
                    # add the new chunk with word occurance removed
                    new_chunks.append(chunk[:i]+chunk[i+len(word):])
        
    min_len = len(min(chunks, key=len))
    #only consider strings of the minimum length in the list
    result = [p for p in chunks if len(p) is min_len]
    #lexicographical sort of strings
    result.sort()
    #return first string
    return result[0]

text = "llllllllllllllllllllllllll"
word = "l"
print answer(text, word)

text = "lololololololololol"
word = "lol"
print answer(text, word)

text = "lololololololololol"
word = "lo"
print answer(text, word)

text = "vedodogggaddodogddogoggogs"
word = "dog"
print answer(text, word)

text = "lololololo"
word = "lol"
print answer(text, word)

text = "goodlololololo"
word = "lol"
print answer(text, word)


text = "goodgooogoogfogoood"
word = "goo"
print answer(text, word)

"""
"lololololo"
"olololo"
"oolo"

"lololololo"
"ololololo"
"ooo"
"ooo"
"""
