import unitest

from translator import english_to_french, french_to_english

class testsuit:

	def test1(self):
		self.assertEqual(english_to_french('hello','bonjour'))
		self.assertEqual(english_to_french('red','rogue'))
		self.assertEqual(english_to_french('',''))
		self.assertNOTEqual(english_to_french('hello','hello'))

	def test2(self):
		self.assertEqual(french_to_english('bonjour','hello'))
		self.assertEqual(french_to_english('rogue','red'))
		self.assertEqual(french_to_english('',''))
		self.assertNOTEqual(french_to_english('rogue','rogue'))


