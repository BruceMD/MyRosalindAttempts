from math import sqrt

def main():

#	with open('sample.txt', 'r') as file:
	with open('rosalind_afrq.txt', 'r') as file:
		data = file.read().replace('\n', '').split()
		
	arr = [float(e) for e in data]
	
	for r in arr:
		answer = r + 2*sqrt(r)*(1-sqrt(r))
		print(round(answer, 3), end = " ")
	print("")
	
	
if __name__ == '__main__':
	main()