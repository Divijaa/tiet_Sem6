#include <bits/stdc++.h>
using namespace std;

string encrypt(string message,int rows) {
    int len = message.length();
    int c = ceil(len / float(rows));
    
    char matrix[rows][c];
    int k = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < c; j++) {
            if (k < len)
                matrix[i][j] = message[k++];
            else
                matrix[i][j] = ' ';
        }
    }
    string encrypted = "";
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < rows; i++) {
            encrypted += matrix[i][j];
        }
    }

return encrypted;
}

// Function to decrypt the message using transposition keyless cipher
string decrypt(string message,int rows) {
    int len = message.length();
    int c = ceil(len / float(rows));
    
    char matrix[rows][5];
    int k = 0;

    // Fill the matrix column-wise with the message characters
    for (int j = 0; j < c; j++) {
        for (int i = 0; i < rows; i++) {
            matrix[i][j] = message[k++];
        }
    }

    // Read the characters from the matrix row-wise
    string decrypted = "";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < c; j++) {
            if (matrix[i][j] != ' ')
                decrypted += matrix[i][j];
        }
    }

    return decrypted;
}

int main() {
    string message = "meetmeatthepark";
    
    cout << "Original message: " << message << endl;
    cout<<"Enter no. of rows"<<endl;
    int rows;
    cin>>rows;

    string encrypted = encrypt(message,rows);
    cout << "Encrypted message: " << encrypted << endl;

    string decrypted = decrypt(encrypted,rows);
    cout << "Decrypted message: " << decrypted << endl;

	return 0;
}
