import unittest
import morse_decoder.main.encoder.Encoder as Encoder


class TestEncoder(unittest.TestCase):

    def test_should_encode_letter(self):
        self.assertEqual(Encoder.encodeLetter("A"), ".-")
        self.assertEqual(Encoder.encodeLetter("B"), "-...")

    def test_should_encode_word(self):
        self.assertEqual(Encoder.encodeWord("AB"), ".- -...")
        self.assertEqual(Encoder.encodeWord("ABC"), ".- -... -.-.")
        self.assertEqual(Encoder.encodeWord("HEY"), ".... . -.--")
        self.assertEqual(Encoder.encodeWord("JUDE"), ".--- ..- -.. .")

    def test_should_decode_sentence(self):
        self.assertEqual(Encoder.encodeSentence("HEY JUDE"), ".... . -.--   .--- ..- -.. .")
        self.assertEqual(Encoder.encodeSentence("HELLO WORLD"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..")
        self.assertEqual(Encoder.encodeSentence("HALLO IHR DA, WIE GEHT ES EUCH?"), ".... .- .-.. .-.. ---   .. .... .-.   -.. .- --..--   .-- .. .   --. . .... -   . ...   . ..- -.-. .... ..--..")


if "__main__" == __name__:
    unittest.main()
