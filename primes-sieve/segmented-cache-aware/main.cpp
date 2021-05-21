//	LINK: https://github.com/kimwalisch/primesieve/wiki/Segmented-sieve-of-Eratosthenes
//	Modified to count runs to 1000000 per 10 seconds
//	(Significantly) faster than the Dave's Garage C++ implementation
//	More pressingly - can an M1 Mac run this faster than the PrimePy.faster.py implementation (because it can run that faster than Dave's C++ implementation, something, my guess is, to do with the implementation of pythons bytearray.index() function) (and things aren't right with the world, without a demonstration that there exists some C/C++ implementation that is faster than any python implementation). 

//	Origional Header:
/// @file     segmented_sieve.cpp
/// @author   Kim Walisch, <kim.walisch@gmail.com> 
/// @brief    This is a simple implementation of the segmented sieve of
///           Eratosthenes with a few optimizations. It generates the
///           primes below 10^9 in 0.8 seconds (single-threaded) on an
///           Intel Core i7-6700 3.4 GHz CPU.
/// @license  Public domain.

#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstdlib>
#include <stdint.h>

/// Set your CPU's L1 data cache size (in bytes) here
const int64_t L1D_CACHE_SIZE = 32768;

/// Generate primes using the segmented sieve of Eratosthenes.
/// This algorithm uses O(n log log n) operations and O(sqrt(n)) space.
/// @param limit  Sieve primes <= limit.
///
void segmented_sieve(int64_t limit)
{
  int64_t sqrt = (int64_t) std::sqrt(limit);
  int64_t segment_size = std::max(sqrt, L1D_CACHE_SIZE);
  int64_t count = (limit < 2) ? 0 : 1;

  // we sieve primes >= 3
  int64_t i = 3;
  int64_t n = 3;
  int64_t s = 3;

  std::vector<char> sieve(segment_size);
  std::vector<char> is_prime(sqrt + 1, true);
  std::vector<int64_t> primes;
  std::vector<int64_t> multiples;

  for (int64_t low = 0; low <= limit; low += segment_size)
  {
    std::fill(sieve.begin(), sieve.end(), true);

    // current segment = [low, high]
    int64_t high = low + segment_size - 1;
    high = std::min(high, limit);

    // generate sieving primes using simple sieve of Eratosthenes
    for (; i * i <= high; i += 2)
      if (is_prime[i])
        for (int64_t j = i * i; j <= sqrt; j += i)
          is_prime[j] = false;

    // initialize sieving primes for segmented sieve
    for (; s * s <= high; s += 2)
    {
      if (is_prime[s])
      {
           primes.push_back(s);
        multiples.push_back(s * s - low);
      }
    }

    // sieve the current segment
    for (std::size_t i = 0; i < primes.size(); i++)
    {
      int64_t j = multiples[i];
      for (int64_t k = primes[i] * 2; j < segment_size; j += k)
        sieve[j] = false;
      multiples[i] = j - segment_size;
    }

    for (; n <= high; n += 2)
      if (sieve[n - low]) // n is a prime
        count++;
  }

  //std::cout << count << " primes found." << std::endl;
}

///// Usage: ./segmented_sieve n
///// @param n  Sieve the primes up to n.
/////
//int main(int argc, char** argv)
//{
//  if (argc >= 2)
//    segmented_sieve(std::atoll(argv[1]));
//  else
//    segmented_sieve(1000000000);
//
//  return 0;
//}


int main()
{
    int passes = 0;
    //prime_sieve* sieve = nullptr;
    auto tStart = std::chrono::steady_clock::now();
    while (std::chrono::duration_cast<std::chrono::seconds>(std::chrono::steady_clock::now() - tStart).count() < 10)
    {
		//delete sieve;
		//sieve = new prime_sieve(1000000);
		//sieve->runSieve();
		//int result_count = sieve->countPrimes();
	//printf("%i\n", result_count);
	
		//	TODO: 2021-05-21T18:56:20AEST Did we find 78498 primes (correct answer for 1000000)
		
		segmented_sieve(1000000);
        passes++;
    }
    auto tD = std::chrono::steady_clock::now() - tStart;

	printf("passes=(%d)\n", passes);
    
    //if (sieve)
    //{
    //    sieve->printResults(false, std::chrono::duration_cast<std::chrono::microseconds>(tD).count() / 1000000, passes);
    //    delete sieve;
    //}
}

