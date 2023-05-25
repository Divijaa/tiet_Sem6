#include <iostream>
#include <string>
using namespace std;
string encrypt(string message, int a, int b) {
    string ciphertext = "";
    for (int i = 0; i < message.length(); i++) {
        char c = message[i];
        if (isalpha(c)) {
            c = toupper(c);
            int x = c - 'A';
            int y = (a * x + b) % 26;
            ciphertext += char(y + 'A');
        }
    }
    return ciphertext;
}

string decrypt(string ciphertext, int a, int b) {
    string message = "";
    int a_inv = 0;
    int m = 26;
    a = a % m;
    for (int x = 1; x < m; x++) {
        if ((a * x) % m == 1) {
           a_inv = x;
        }
    }
    for (int i = 0; i < ciphertext.length(); i++) {
        char c = ciphertext[i];
        if (isalpha(c)) {
            c = toupper(c);
            int y = c - 'A';
            int x = (a_inv * (y - b + 26)) % 26;
            message += char(x + 'A');
        }
    }
    return message;
}

int main() {
    string pt;
    cout<<"Enter string "<<endl;
	cin>>pt;
    int a = 17;
    int b = 20;
    
    string ciphertext = encrypt(pt, a, b);
    string decrypted = decrypt(ciphertext, a, b);
    
    cout << "Key: (" << a << ", " << b << ")" << endl;
    cout << "CipherText is " << ciphertext << endl;
    cout << "Plain Text is " << decrypted << endl;
    
    return 0;
}

