## Vignere Cipher:
from random import randint
from random import choice

class Vigenere_Encryption:

	nos_of_encryptions = 0

	def __init__(self, plain_text, key, sequence, cipher_text):
		self.plain_text = plain_text
		self.cipher_text = cipher_text
		self.key = key
		self.k_padded = ""
		self.sequence = sequence
		Vigenere_Encryption.nos_of_encryptions += 1

	def padding_simple(self, length):
		self.k_padded = ''.join([self.key for i in range(length//len(self.key))]) + self.key[:length%len(self.key)]
		if len(self.k_padded) != length:
			raise Exception("Padded Key Length does not match length of Plain Text")

	def padding_ignore(self, string_inp):
		c = 0
		for i in string_inp:
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

	def decryption(self):
		for i,j in zip(self.cipher_text, self.k_padded):
			#self.cipher_text = self.cipher_text + self.sequence[(self.sequence.index(i) + self.sequence.index(j))%len(self.sequence)]
			try:
				self.plain_text = self.plain_text + self.sequence[(self.sequence.index(i) - self.sequence.index(j))%len(self.sequence)]
			except:
				self.plain_text = self.plain_text + i

		return self.plain_text	



def main():
	opt = int(input("Enter 1 for encryption and 2 for decryption"))
	opt -= 1
	if opt == 0:
		plain_text = input("Enter Plain Text:\t")
		sequence = input("Enter sequence of character:\t")
		key = input("Enter Key:\t")
		cipher_text = ""
		v = Vigenere_Encryption(plain_text, key, sequence, cipher_text)
		v.padding_simple(len(plain_text))
		#v.padding_ignore(plain_text)
		c = v.encryption()
		print(c)
	else:
		cipher_text = input("Enter Cipher Text:\t")
		sequence = input("Enter sequence of character:\t")
		key = input("Enter Key:\t")
		plain_text = ""
		v = Vigenere_Encryption(plain_text, key, sequence, cipher_text)
		v.padding_simple(len(cipher_text))
		#v.padding_ignore(cipher_text)
		p = v.decryption()
		print(p)

	
	





def health_check():
	sequence = list(string.ascii_lowercase)
	for i in range(10):
		len_plain_text = randint(10, 50)
		len_key = randint(2, 15)
		plain_text = "".join([choice(sequence) for i in range(len_plain_text)])
		key = "".join([choice(sequence) for i in range(len_key)])

		
main()
## TO check whether key_padding works please use the health function