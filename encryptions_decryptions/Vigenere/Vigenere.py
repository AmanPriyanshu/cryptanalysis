## Vignere Cipher:
from random import randint
from random import choice
import binascii

class Vigenere_Encryption:

	nos_of_encryptions = 0

	def __init__(self, plain_text, key, sequence, cipher_text):
		self.plain_text = plain_text
		self.cipher_text = cipher_text
		self.key = key
		#self.k_padded = ""
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

	def encryption_add(self):
		for i,j in zip(self.plain_text, self.k_padded):
			#self.cipher_text = self.cipher_text + self.sequence[(self.sequence.index(i) + self.sequence.index(j))%len(self.sequence)]
			try:
				self.cipher_text = self.cipher_text + self.sequence[(self.sequence.index(i) + self.sequence.index(j))%len(self.sequence)]
			except:
				self.cipher_text = self.cipher_text + i

		return self.cipher_text	

	def decryption_add(self):
		for i,j in zip(self.cipher_text, self.k_padded):
			#self.cipher_text = self.cipher_text + self.sequence[(self.sequence.index(i) + self.sequence.index(j))%len(self.sequence)]
			try:
				self.plain_text = self.plain_text + self.sequence[(self.sequence.index(i) - self.sequence.index(j))%len(self.sequence)]
			except:
				self.plain_text = self.plain_text + i

		return self.plain_text	

	def encryption_xor(self):
		
		for i in range(len(self.plain_text)//len(self.key)):
			self.cipher_text += hex(int(self.plain_text[i*len(self.key):(i+1)*len(self.key)], 16) ^ int(self.key, 16))
		self.cipher_text += hex(int(self.plain_text[-len(self.plain_text)%len(self.key):], 16) ^ int(self.key[len(self.plain_text)%len(self.key)], 16))
		return self.cipher_text


	


def main():
	opt = int(input("Enter 1 for encryption-add and 2 for decryption-add [TODO: or 3 for encryption-xor and 4 for decryption-xor]"))
	opt -= 1
	if opt == 0:
		plain_text = input("Enter Plain Text:\t")
		sequence = input("Enter sequence of character:\t")
		key = input("Enter Key:\t")
		cipher_text = ""
		v = Vigenere_Encryption(plain_text, key, sequence, cipher_text)
		#v.padding_simple(len(plain_text))
		v.padding_ignore(plain_text)
		c = v.encryption_add()
		print(c)
	elif opt == 1:
		cipher_text = input("Enter Cipher Text:\t")
		sequence = input("Enter sequence of character:\t")
		key = input("Enter Key:\t")
		plain_text = ""
		v = Vigenere_Encryption(plain_text, key, sequence, cipher_text)
		#v.padding_simple(len(cipher_text))
		v.padding_ignore(cipher_text)
		p = v.decryption_add()
		print(p)
	elif opt == 2:
		plain_text = input("Enter Plain Text:\t")
		plain_text = binascii.hexlify(plain_text.encode())
		plain_text = str(plain_text)
		plain_text = plain_text[2:-1]
		sequence = ""
		key = input("Enter Key:\t")
		key = binascii.hexlify(key.encode())
		key = str(key)
		key = key[2:-1]
		cipher_text = ""
		v = Vigenere_Encryption(plain_text, key, sequence, cipher_text)
		c = v.encryption_xor()
		print(c)

	

	
	





def health_check():
	sequence = list(string.ascii_lowercase)
	for i in range(10):
		len_plain_text = randint(10, 50)
		len_key = randint(2, 15)
		plain_text = "".join([choice(sequence) for i in range(len_plain_text)])
		key = "".join([choice(sequence) for i in range(len_key)])

		
main()
## TO check whether key_padding works please use the health function

## Simple padding can be removed if we use the simple case where we can just mod key over and over again. 
## The issue of such padding does not exist for ex-or encryption/decryption or atleast I haven't found yet.