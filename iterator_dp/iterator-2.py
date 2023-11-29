#Following code is the example of an explicitly created Iterator method
""" helper method for iterator"""


def alphabets_upto(letter):
	"""Counts by word numbers, up to a maximum of five"""
	for i in range(65, ord(letter)+1):
			yield chr(i)


"""main method"""
if __name__ == "__main__":

	alphabets_upto_K = alphabets_upto('K')
	alphabets_upto_M = alphabets_upto('M')

	for alpha in alphabets_upto_K:
		print(alpha, end=" ")

	print()

	for alpha in alphabets_upto_M:
		print(alpha, end=" ")
