from time import time

def main():
	
#	with open('sample.txt', 'r') as file:
	with open('rosalind_prsm.txt', 'r') as file:
		prot = [item.strip("\n") for item in file.readlines()]
		
		
	spectra = [float(e) for e in prot[int(prot[0])+1:]]
	
	spectra.sort()
	print(spectra)

	for s in spectra:
		print(s)
		print(rec(s, ""))
	
def rec(sp, seq):
	massTable = {71.03711 : "A", 103.00919 : "C", 115.02694 : "D", 129.04259 : "E",
	147.06841 : "F", 57.02146 : "G", 137.05891 : "H", 113.08406 : "I", 128.09496 : "K",
	113.08406 : "L", 131.04049 : "M", 114.04293 : "N", 97.05276 : "P", 128.05858 : "Q",
	156.10111 : "R", 87.03203 : "S", 101.04768 : "T", 99.06841 : "V", 186.07931 : "W",
	163.06333 : "Y"}
	
	if round(sp, 5) == 0:
		print(seq)
		return seq
	elif sp < 0:
		return
	else:
		for m, l in massTable.items():
			rec(sp-m, seq + l)
	
if __name__ == "__main__":
	s = time()
	main()
	e = time()
	print(e-s)