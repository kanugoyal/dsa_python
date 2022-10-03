#Reverse individual words

def reverseWords(string):
	st = list()

	for i in range(len(string)):      
		if string[i] != " ":          #traverse given string and push all character of a word to stack
			st.append(string[i])

		else:                          #print content of stack when string == space
			while len(st) > 0:
				print(st[-1], end= "")
				st.pop()
			print(end = " ")

	while len(st) > 0:
		print(st[-1], end = "")
		st.pop()

def rev_sentence(sentence):

	words = sentence.split(' ')
	reverse_sentence=""
	for i in words:
		reverse_sentence+=i[::-1]+' '

	return reverse_sentence


if __name__ == '__main__':
	string = 'lets do it'
	reverseWords(string)
#print(rev_sentence(string))
