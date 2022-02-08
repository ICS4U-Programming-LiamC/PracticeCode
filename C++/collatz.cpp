# include <iostream>
using namespace std;
int main () {
    int collatzNum;
    int num = 3;
    int counter;
    while (num < 1000000) {
        collatzNum = num;
        counter = 0;
        while (collatzNum != 1) {
            if (collatzNum % 2 == 0) {
                collatzNum /= 2;
            } else {
                collatzNum = collatzNum * 3 + 1;
            }
            counter++;
        }
        if (counter > 500) {
            cout << num << " ran for " << counter << endl;
        }
        num+=1;
    }
}
