import unittest
import main.decoder.Decoder as Decoder


class TestDecoder(unittest.TestCase):

    def test_should_return_value_for_one_morseInput(self):
        self.assertEqual(Decoder.encodeValue(".-"), "A")
        self.assertEqual(Decoder.encodeValue("-..."), "B")

    def test_should_return_word_for_multiple_morseInputs(self):
        self.assertEqual(Decoder.encodeWord(".- -..."), "AB")
        self.assertEqual(Decoder.encodeWord(".- -.-."), "AC")
        self.assertEqual(Decoder.encodeWord(".... . -.--"), "HEY")
        self.assertEqual(Decoder.encodeWord(".--- ..- -.. ."), "JUDE")

    def test_should_return_sentence_for_multiple_words(self):
        self.assertEqual(Decoder.encodeSentence(".... . -.--   .--- ..- -.. ."), "HEY JUDE")
        self.assertEqual(Decoder.encodeSentence(".... . .-.. .-.. --- / .-- --- .-. .-.. -.."), "HELLO WORLD")
        self.assertEqual(Decoder.encodeSentence(".... .- .-.. .-.. --- / .. .... .-. / -.. .- / .-- .. . / --. . .... - / . ... / . ..- -.-. ...."), "HALLO IHR DA WIE GEHT ES EUCH")
        self.assertEqual(Decoder.encodeSentence(".... .- .-.. .-.. --- / .. .... .-. / -.. .- --..-- / .-- .. . / --. . .... - / . ... / . ..- -.-. .... ..--.."), "HALLO IHR DA, WIE GEHT ES EUCH?")

if "__main__" == __name__:
    unittest.main()
