import numpy
'''
Time taken by brute force: 256^L (L being key length)
Time taken to find key length: 256*L
Time take to find key bytes or key: (256^2)*L
Linear in L
'''

'''
Question:
F96DE8C227A259C87EE1DA2AED57C93FE5DA36ED4EC87EF2C63AAE5B9A7EFFD673BE4ACF7BE8923CAB1ECE7AF2DA3DA44FCF7AE29235A24C963FF0DF3CA3599A70E5DA36BF1ECE77F8DC34BE129A6CF4D126BF5B9A7CFEDF3EB850D37CF0C63AA2509A76FF9227A55B9A6FE3D720A850D97AB1DD35ED5FCE6BF0D138A84CC931B1F121B44ECE70F6C032BD56C33FF9D320ED5CDF7AFF9226BE5BDE3FF7DD21ED56CF71F5C036A94D963FF8D473A351CE3FE5DA3CB84DDB71F5C17FED51DC3FE8D732BF4D963FF3C727ED4AC87EF5DB27A451D47EFD9230BF47CA6BFEC12ABE4ADF72E29224A84CDF3FF5D720A459D47AF59232A35A9A7AE7D33FB85FCE7AF5923AA31EDB3FF7D33ABF52C33FF0D673A551D93FFCD33DA35BC831B1F43CBF1EDF67F0DF23A15B963FE5DA36ED68D378F4DC36BF5B9A7AFFD121B44ECE76FEDC73BE5DD27AFCD773BA5FC93FE5DA3CB859D26BB1C63CED5CDF3FE2D730B84CDF3FF7DD21ED5ADF7CF0D636BE1EDB79E5D721ED57CE3FE6D320ED57D469F4DC27A85A963FF3C727ED49DF3FFFDD24ED55D470E69E73AC50DE3FE5DA3ABE1EDF67F4C030A44DDF3FF5D73EA250C96BE3D327A84D963FE5DA32B91ED36BB1D132A31ED87AB1D021A255DF71B1C436BF479A7AF0C13AA14794
'''

class Vigenere_cracker():
	def __init__(self, cipher_text):
		self.cipher_text = cipher_text
		self.key = ""
		self.plain_text = ""
		self.key_length = 0

	def frequency_analyzer_length(self, i):
		q = 0
		for j in range(len(cipher_text)//i):
			uniques = ''.join(set(self.cipher_text))


	def frequency_analyzer(self):
		# summation: q(0-255)^2
		print('bruh')


	def key_size_predictor(self):
		'''
		Concept: So we know that from the plain text every Nth character N being key length is shifted by the "same" factor, so it means that frequency analysis sum of 
		this whole mess should be the same as that of English. Cause like if there are i then all i's having been shifted by the same factor will give an output which 
		has the same frequency. That's the concept which finds us key length.
		'''
		key_length_prob = []
		for i in range(0,256):
			key_length_prob.append(self.frequency_analyzer_length(i))
		return key_length

	def key_char_predictor(self):
		'''
		Make streams of Nth and Nth multiples, now we will have a string having gibberish now just take 0 to 256 and then count frequency of each of the letters between 
		32 to 127 whatever is closest to english (p)i^2 = 0.065 maybe the char.
		'''
	def key_finder(self):
		self.key_length = self.key_size_predictor()

