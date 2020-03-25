import numpy

class Vigenere_cracker():
	def __init__(self, cipher_text):
		self.cipher_text = cipher_text
		self.key = ""
		self.plain_text = ""
		