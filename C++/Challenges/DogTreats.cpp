#include <iostream>
using namespace std;
int main() {
    int S;
    int M;
    int L;
    cin >> S;
    cin >> M;
    cin >> L;

    if (S + 2*M + 3*L >= 10) {
        cout << "Happy";
    } else {
        cout << "Sad";
    }

}