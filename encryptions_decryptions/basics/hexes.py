import binascii
class hexes():
	def __init__(self, str_input):
		self.str_input = str_input
		self.str_output = ''

	def hex_to_int(self):
		try:
			self.str_output = int(self.str_input.encode(),16)
		except ValueError:
			self.str_output = int(self.str_input[2:].encode(),16)

	def int_to_hex(self):
		self.str_output = hex(int(self.str_input))

	def hex_to_ascii(self):
		try:
			self.str_output = binascii.unhexlify(self.str_input.encode())
		except ValueError:
			self.str_output = binascii.unhexlify(self.str_input[2:].encode())

		
	def ascii_to_hex(self):
		self.str_output = binascii.hexlify(self.str_input.encode())

def health_check():
	inp = ['c8', '200', '68656c6c6f20776f726c64', 'hello world']
	a = hexes(inp[0])
	a.hex_to_int()
	print(a.str_input, a.str_output)
	a = hexes(inp[1])
	a.int_to_hex()
	print(a.str_input, a.str_output)
	a = hexes(inp[2])
	a.hex_to_ascii()
	print(a.str_input, a.str_output)
	a = hexes(inp[3])
	a.ascii_to_hex()
	print(a.str_input, a.str_output)

def main():
	str_input = input("Input Conversion\t")
	input_type = int(input("Enter Input Type [1. INT, 2. ASCII, 3. HEX_ASCII, 4. HEX_INT]:\t"))
	input_type -= 1
	if input_type == 0:
		a = hexes(str_input)
		a.int_to_hex()
		print(a.str_output)
	elif input_type == 1:
		a = hexes(str_input)
		a.ascii_to_hex()
		print(a.str_output)
	elif input_type == 2:
		a = hexes(str_input)
		a.hex_to_ascii()
		print(a.str_output)
	elif input_type == 3:
		a = hexes(str_input)
		a.hex_to_int()
		print(a.str_output)



main()