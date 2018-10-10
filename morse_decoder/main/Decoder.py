import main.decoder.Morsecode as Morsecode

morse_alphabet = Morsecode.morseAlphabet


def encodeValue(letter):
    for key, value in morse_alphabet.items():
        if value == letter:
            return key


def encodeWord(word):
    output = ""
    letters = word.split(" ")
    for letter in letters:
        output += encodeValue(letter)
    return output


def encodeSentence(sentence):
    output = []
    words = sentence.split("   ")
    for word in words:
        output.append(encodeWord(word))
    return " ".join(output)
