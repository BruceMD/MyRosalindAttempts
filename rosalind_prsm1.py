from time import time

#massTable = {71.03711 : "A", 103.00919 : "C", 115.02694 : "D", 129.04259 : "E",
#147.06841 : "F", 57.02146 : "G", 137.05891 : "H", 113.08406 : "I", 128.09496 : "K",
#113.08406 : "L", 131.04049 : "M", 114.04293 : "N", 97.05276 : "P", 128.05858 : "Q",
#156.10111 : "R", 87.03203 : "S", 101.04768 : "T", 99.06841 : "V", 186.07931 : "W",
#163.06333 : "Y"}

def main():
	
	with open('sample.txt', 'r') as file:
#	with open('rosalind_prsm.txt', 'r') as file:
		prot = [item.strip("\n") for item in file.readlines()]
		
	spectra = [float(e) for e in prot[int(prot[0])+1:]]
	spectra.sort()
	
	sequences = [f for f in prot[1:int(prot[0])+1]]
	
	for i in range(2, 150):
		
	
	
	
def sumSpec(seq):
	mT = {'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I':113.08406, 'L': 113.08406, 'K': 128.09496, 'M': 131.04049, 'N': 114.04293, 'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333}
	total = 0
	for s in seq:
		total += mT[s]
	
	return total
	
	
if __name__ == "__main__":
	s = time()
	main()
	e = time()
	print(e-s)
