
#include <iostream>
#include <list>
#include <cstdlib>
#include <vector>
#include <time.h>
#include <math.h>
using namespace std;

int main(void) {
    clock_t tStart = clock();
    int NumPrimes = 2000000;
    int check = 0;
    int check2 = 0;
    int prime;
    int numOfPrimes = 1;
    int counter = 0;
    std::vector<int> primes;
    primes.push_back(2);
    primes.push_back(3);
    primes.push_back(5);
    primes.push_back(7);

    for (int number = 6; number+=6;) {
        int size = primes.size();

        for(int i = 0; i < size; i++) {
            if (primes[i] > sqrt(number)) {
                break;
            }
            if ((number - 1) % primes[i] == 0) {
                check = 1;
                break;
            } else {
            }
        }

        if (check == 0) {
            primes.push_back(number - 1);
            counter += 1;
            if (counter > NumPrimes - 5) {
                break;
            } 
        } else {
            check = 0;
        }

        for(int i = 0; i < size; i++) {
            if (primes[i] > sqrt(number)) { // pow(number, 0.493577)
                break;
            }
            if ((number + 1) % primes[i] == 0) {
                check = 1;
                break;
            } else {
            }
        }

        if (check == 0) {
            primes.push_back(number + 1);
            counter += 1;
            if (counter > NumPrimes - 5) {
                break;
            } 
        } else {
            check = 0;
        }

    }
    int hi = 0;
    for(int i : primes) {
        hi += 1;
        if (hi > 1999800) {
            // cout << "i = " << i << endl;
        } else {

        }
    }
    cout << primes.size() << endl;
    printf("Time taken: %.2fs\n", (double)(clock() - tStart)/CLOCKS_PER_SEC);
    return 0;
}
