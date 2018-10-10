import morse_decoder.main.Morsecode as Morsecode

morse_alphabet = Morsecode.morseAlphabet


def encodeLetter(input):
    return morse_alphabet.get(input)


def encodeWord(input):
    word = []
    for letter in input:
        word.append(encodeLetter(letter))
    return " ".join(word)


def encodeSentence(input):
    sentence = []
    for word in input.split(" "):
        sentence.append(encodeWord(word))
    return "   ".join(sentence)
