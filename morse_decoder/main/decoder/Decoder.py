import morse_decoder.main.Morsecode as Morsecode

morse_alphabet = Morsecode.morseAlphabet


def encodeLetter(input):
    for letter, morsecoder in morse_alphabet.items():
        if morsecoder == input:
            return letter


def encodeWord(input):
    word = ""
    letters = input.split(" ")
    for letter in letters:
        word += encodeLetter(letter)
    return word


def encodeSentence(input):
    sentence = []
    words = input.split("   ")
    for word in words:
        sentence.append(encodeWord(word))
    return " ".join(sentence)
