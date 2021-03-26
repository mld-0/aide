import math
import sys

class primes_sieve_optimised(object):

    def __init__(self, limit):
        self.sieve_size = limit
        self.bit_values = [True] * int((self.sieve_size+1)/2)
        self.result_primes = None

    def _GetBit(self, index):
        if (index % 2 == 0) and (index != 2):
            return False
        else:
            return self.bit_values[int(index/2)]

    def _ClearBit(self, index):
        if (index % 2 == 0):
            assert("Don't need to clear even bits")
            return False
        else:
            self.bit_values[int(index/2)] = False

    def _countPrimes(self):
        return sum(1 for b in self.bit_values if b)

    def _collectResults(self):
        for num in range(2, self.sieve_size):
            if self._GetBit(num):
                self.result_primes.append(num)

    def run_sieve(self):
        self.result_primes = []
        factor = 3
        q = math.sqrt(self.sieve_size)
        while (factor < q):
            for num in range(factor, self.sieve_size):
                if self._GetBit(num):
                    factor = num
                    break
            #   2nd instance already dealt with, so start with 3rd instance, and skip over even values
            for num in range(factor*3, self.sieve_size, factor*2):
                self._ClearBit(num)
            factor += 2  # skip to next odd value
        self._collectResults()

if __name__ == '__main__':
    p = primes_sieve_optimised(20)
    p = primes_sieve_optimised(1000000)
    p.run_sieve()
    #print(p.result_primes)
    print(p._countPrimes())
    #print(p.bit_values)



