import time
n = 5000
 
start = time.time()
# lista liczb od 2 do n, 0 i 1 nie sa liczbami pierwszymi
numbers = list(range(2, n + 1))
  
# usuwanie wielokrotnosci liczb pierwszych
for prime in numbers:
    for multiple in range(2 * prime, n + 1, prime):
    	# try except pass is 4 sec faster for n = 50000 !!!!
        if multiple in numbers:
            numbers.remove(multiple)

print "Liczby pierwsze z zakresu od 2 do {0}:".format(n)
print numbers

end = time.time()
print 'czas: %s' %(end - start) 