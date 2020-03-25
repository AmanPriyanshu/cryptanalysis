## Vignere Cipher:
from random import randint
from random import choice

class Vigenere_Encryption:

	nos_of_encryptions = 0

	def __init__(self, plain_text, key, sequence):
		self.plain_text = plain_text
		self.cipher_text = ""
		self.key = key
		self.k_padded = ""
		self.sequence = sequence
		Vigenere_Encryption.nos_of_encryptions += 1

	def padding_simple(self):
		self.k_padded = ''.join([self.key for i in range(len(self.plain_text)//len(self.key))]) + self.key[:len(self.plain_text)%len(self.key)]
		if len(self.k_padded) != len(self.plain_text):
			raise Exception("Padded Key Length does not match length of Plain Text")

	def padding_ignore(self):
		c = 0
		for i in self.plain_text:
			if self.sequence.find(i) != -1:
				self.k_padded += self.key[c%len(self.key)]
				c += 1
			else:
				self.k_padded += i

	def encryption(self):
		for i,j in zip(self.plain_text, self.k_padded):
			#self.cipher_text = self.cipher_text + self.sequence[(self.sequence.index(i) + self.sequence.index(j))%len(self.sequence)]
			try:
				self.cipher_text = self.cipher_text + self.sequence[(self.sequence.index(i) + self.sequence.index(j))%len(self.sequence)]
			except:
				self.cipher_text = self.cipher_text + i

		return self.cipher_text	


def main():
	plain_text = input("Enter Plain Text:\t")
	sequence = input("Enter sequence of character:\t")
	key = input("Enter Key:\t")

	v = Vigenere_Encryption(plain_text, key, sequence)
	v.padding_simple()
	#v.padding_ignore()
	c = v.encryption()
	print(c)	
	
	





def health_check():
	sequence = list(string.ascii_lowercase)
	for i in range(10):
		len_plain_text = randint(10, 50)
		len_key = randint(2, 15)
		plain_text = "".join([choice(sequence) for i in range(len_plain_text)])
		key = "".join([choice(sequence) for i in range(len_key)])

		
main()