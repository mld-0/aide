import math
import sys

class primes_sieve_optimised(object):

    def __init__(self, limit):
        self.sieve_size = limit
        self.bit_values = [True] * int(self.sieve_size)
        self.result_primes = None

    def _countPrimes(self):
        return sum(1 for b in self.bit_values[2:] if b)

    def _collectResults(self):
        for num in range(2, self.sieve_size):
            if self.bit_values[num]:
                self.result_primes.append(num)

    def run_sieve(self):
        self.result_primes = []
        factor = 2
        q = math.sqrt(self.sieve_size)
        while (factor < q):
            for num in range(factor, self.sieve_size):
                if self.bit_values[num]:
                    factor = num
                    break
            for num in range(factor*2, self.sieve_size, factor):
                self.bit_values[num] = False
            factor += 1
        self._collectResults()

if __name__ == '__main__':
    p = primes_sieve_optimised(20)
    p = primes_sieve_optimised(1000000)
    p.run_sieve()
    #print(p.result_primes)
    print(p._countPrimes())



