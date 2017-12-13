st = 'Print only the words that start with s in this sentence, use for, split and if'

ls = st.split(" ")
for i in ls:
	if(i[0] == 's'):
		print(i)
