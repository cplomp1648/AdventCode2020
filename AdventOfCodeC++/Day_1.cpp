#include <iostream>
#include <fstream>
using namespace std;

int main () {
    ifstream f("inputs\\Day_1_input.txt");
    f.open("inputs\\Day_1_input.txt", ios::in);
    char data[100];
    cout << "Reading" << endl;
    f >> data;
    cout << data << endl;
    //for (int index = 0; index < 5; ++index)
    //  cout << line << endl;
    f.close();
    
    return 0;
}