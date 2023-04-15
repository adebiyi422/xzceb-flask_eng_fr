#write unit tests

import unittest

from translator import english_to_french, french_to_english

class TestF2E(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None),None) #tests that the input is null
        self.assertEqual(french_to_english("Bonjour"),"Hello") #tests that hello translates to Bonjour


class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None),None)  #tests for null input
        self.assertEqual(english_to_french("Hello"),"Bonjour") #tests that it translates Bonjour to Hello

unittest.main()
      