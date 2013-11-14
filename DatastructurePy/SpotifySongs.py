def Songs():
	Numbers = [int(i) for i in raw_input().strip().split()]
	N = Numbers[0]
	m = Numbers[1]
	dict = {}
	for i in range(N):
		Val = raw_input().strip().split()
		if int(Val[0])/(float(N - i)) not in dict:
			dict[int(Val[0])/(float(N - i))] = [str(Val[1])]
		else:
			LI = dict[int(Val[0])/(float(N - i))]
			LI.append(str(Val[1]))
			dict[int(Val[0])/(float(N - i))] = LI
	keys = dict.keys()
	keys.sort(reverse = True)
	Value = []
	I = 0
	K = 0 
	while K<m:
		List = dict[keys[I]]
		for i in List:
			print i
			K = K + 1
		I += 1
        

if __name__ == '__main__':
    Songs()
