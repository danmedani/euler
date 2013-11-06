
import time
import io

# Functions
def isPrime(val):
    if prime_list.__contains__(val):
        return True
    else:
        return False

def isCircPrime(prime):
    prime_str = str(prime)
    
    # All single digit primes are circular
    if len(prime_str) == 1:
        return True

    # This value seems to be used frequently
    len_str_minus_one = len(prime_str) - 1
    
    # Rotate!
    for i in range(len_str_minus_one):
        prime_str = prime_str[len_str_minus_one] + prime_str[0:len_str_minus_one]
        if not isPrime(int(prime_str)):
            return False

    # All tests passed. It's gotta be a circular prime
    return True

t0 = time.time()

print ''
print 'Prime Time'

prime_list = []

# Grabs the list of primes from 'primes.txt'
prime_file = open('primes.txt','r')
prime_list_str = prime_file.readline().split(',')
for i in range(len(prime_list_str)):
    prime_list.append(int(prime_list_str[i]))

print 'Num Primes: ', len(prime_list)

# Take out all (non-single-digit) primes that contain the digits [0,2,4,5,6,8] (thank you Mr. Lappin)
i = 4
while i < len(prime_list):
    prime_str = str(prime_list[i])
    if prime_str.__contains__('0') or prime_str.__contains__('2') or prime_str.__contains__('4') or prime_str.__contains__('5') or prime_str.__contains__('6') or prime_str.__contains__('8'):
        prime_list.remove(prime_list[i])
        i = i - 1
    i = i + 1

print 'Num Possible Primes: ', len(prime_list)

# Build list of circular primes
circ_prime_list = []
for i in range(len(prime_list)):
    if isCircPrime(prime_list[i]):
        circ_prime_list.append(prime_list[i])

print 'Num Circ Primes: ', len(circ_prime_list)
print 'Circ Prime List', circ_prime_list
print 'Total Time: ', time.time() - t0, 'seconds'

