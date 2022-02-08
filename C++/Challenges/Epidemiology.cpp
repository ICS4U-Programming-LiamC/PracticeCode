#include <iostream>
using namespace std;

int main() {
    int R;
    int N;
    int P;
    cin >> P;
    cin >> N;
    cin >> R;
    int day = 0;
    int total = N;
    // cout << "\n" << total << endl;
    while (true) {
        total = total + N*R;
        N = N*R;
        // cout << N << endl;
        day ++;
        if (total > P) {
            break;
        }
    }
    // cout << total << endl;
    cout << day;
}