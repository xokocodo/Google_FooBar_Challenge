"""
String cleaning
===============
Your spy, Beta Rabbit, has managed to infiltrate a lab of mad scientists who are turning rabbits into zombies. He sends
a text transmission to you, but it is intercepted by a pirate, who jumbles the message by repeatedly inserting the same
word into the text some number of times. At each step, he might have inserted the word anywhere, including at the
beginning or end, or even into a copy of the  word he inserted in a previous step. By offering the pirate a dubloon, you
get him to tell you what that word was. A few bottles of rum  later, he also tells you that the original text was the
shortest possible string formed by repeated removals of that word, and that the  text was actually the lexicographically
earliest string from all the possible shortest candidates. Using this information, can you work  out what message your
spy originally sent?
For example, if the final chunk of text was "lolol," and the inserted word was "lol," the shortest possible strings  are
"ol" (remove "lol" from the beginning) and "lo" (remove "lol" from the end). The original text  therefore must have been
"lo," the lexicographically earliest string.
Write a function called answer(chunk, word) that returns the shortest, lexicographically earliest string that can be
formed by removing occurrences of word from chunk. Keep in mind that the occurrences may be nested, and that removing
one occurrence might result in another. For example, removing "ab" from "aabb" results in another "ab" that was not
originally present. Also keep in mind that your spy's original message might have been an empty string.
chunk and word will only consist of lowercase letters [a-z].
chunk will have no more than 20 characters.
word will have at least one character, and no more than the number of characters in chunk.
"""

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
