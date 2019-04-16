st = 'Print every word in this sentence that has a even number of letters'
ls = st.split(" ")
l = [i for i in ls if len(i)%2 == 0]
print l