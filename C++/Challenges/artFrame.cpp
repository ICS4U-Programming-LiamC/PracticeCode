#include <iostream>
#include <string>
using namespace std;

int main() {
    int x1 = 100;
    int y1;
    int x2;
    int y2;
    int x;
    int y;
    string str;
    string numPaint;
    cout << "How many drops of paint: ";
    getline(cin, numPaint);
    int numLines = stoi(numPaint);
    int i = 0;
    while (i < numLines) {
        i++;
        getline(cin, str);
        if (str == "exit") {
            break;
        }
        string str1;
        string str2;

        string delimiter = ",";

        size_t pos = 0;
        std::string token;
        int counter = 0;
        while ((pos = str.find(delimiter)) != std::string::npos) {
            token = str.substr(0, pos);
            // std::cout << token << std::endl;
            str.erase(0, pos + delimiter.length());
            counter++;
        }
        x = stoi(token);
        y = stoi(str);

        if (x < x1) {
            x1 = x;
        } 
        if (x > x2) {
            x2 = x;
        }
        if (y < y1) {
            y1 = y;
        } 
        if (y > y2) {
            y2 = y;
        }
    }
    cout << x1 - 1 << "," << y1 - 1 << endl;
    cout << x2 + 1 << "," << y2 + 1 << endl;
}
