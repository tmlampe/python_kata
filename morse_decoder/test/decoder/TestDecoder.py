import unittest
import morse_decoder.main.decoder.Decoder as Decoder


class TestDecoder(unittest.TestCase):

    def test_should_decode_letter(self):
        self.assertEqual(Decoder.encodeLetter(".-"), "A")
        self.assertEqual(Decoder.encodeLetter("-..."), "B")

    def test_should_decode_word(self):
        self.assertEqual(Decoder.encodeWord(".- -..."), "AB")
        self.assertEqual(Decoder.encodeWord(".- -.-."), "AC")
        self.assertEqual(Decoder.encodeWord(".... . -.--"), "HEY")
        self.assertEqual(Decoder.encodeWord(".--- ..- -.. ."), "JUDE")

    def test_should_decode_sentence(self):
        self.assertEqual(Decoder.encodeSentence(".... . -.--   .--- ..- -.. ."), "HEY JUDE")
        self.assertEqual(Decoder.encodeSentence(".... . .-.. .-.. ---   .-- --- .-. .-.. -.."), "HELLO WORLD")
        self.assertEqual(Decoder.encodeSentence(".... .- .-.. .-.. ---   .. .... .-.   -.. .-   .-- .. .   --. . .... -   . ...   . ..- -.-. ...."), "HALLO IHR DA WIE GEHT ES EUCH")
        self.assertEqual(Decoder.encodeSentence(".... .- .-.. .-.. ---   .. .... .-.   -.. .- --..--   .-- .. .   --. . .... -   . ...   . ..- -.-. .... ..--.."), "HALLO IHR DA, WIE GEHT ES EUCH?")

if "__main__" == __name__:
    unittest.main()
