//combined
#include<bits/stdc++.h>
using namespace std;

string encrypt1(string text,vector<int> key){
    int q=key.size();
        int n=text.length()/q;
        int i=0;
        string ans="";
       //writting row by row
        for(int j=0;j<n;j++){
            string test="";
            string t=text.substr(i,q);
            //reordering the cols
            for(int y=0;y<q;y++){
                test+=t[key[y]-1];
                i++;
            }
            ans+=test;
        }
        
        //adding the bogus characters
    int y=text.length()%q;
    string yo=text.substr(text.length()-y);
    int u=q-y;
    for(int i=0;i<u;i++){
        yo+='z'-i;
    }
    i=0;
    string test="";
    
    for(int y=0;y<q;y++){
        test+=yo[key[y]-1];
        i++;
    }
    ans+=test;
    return ans; //read row wise
    
}
string encrypt(string message,int col) {
    int len = message.length();
    int rows = ceil(len / float(col));
    
    char matrix[rows][col];
    int k = 0;
// Fill the matrix with the message characters
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < col; j++) {
            if (k < len)
                matrix[i][j] = message[k++];
            else
                matrix[i][j] = ' ';
        }
    }

    // Read the characters from the matrix column-wise
    string encrypted = "";
    for (int j = 0; j < col; j++) {
        for (int i = 0; i < rows; i++) {
            encrypted += matrix[i][j];
        }
    }

    return encrypted;
}

// Function to decrypt the message using transposition keyless cipher
string decrypt(string message,int col) {
    int len = message.length();
    int rows = ceil(len / float(col));
    
    char matrix[rows][col];
    int k = 0;

    // Fill the matrix column-wise with the message characters
    for (int j = 0; j < col; j++) {
        for (int i = 0; i < rows; i++) {
            matrix[i][j] = message[k++];
        }
    }

    // Read the characters from the matrix row-wise
    string decrypted = "";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < col; j++) {
            if (matrix[i][j] != ' ')
                decrypted += matrix[i][j];
        }
    }

    return decrypted;
}
string decrypt1(string text,vector<int> key){
    int q=key.size();
    int n=text.length()/q;
    int i=0;
    string ans="";
   
    for(int j=0;j<n;j++){
        string test="";
        for(int j=0;j<q;j++){
            test+="*";
        }
        for(int y=0;y<q;y++){
            test[key[y]-1]=text[i];
            i++;
        }
        ans+=test;
    }
    
    return ans;
    
}
int main() {
    string message = "enemyattackstonight";
    vector<int> key={3,1,4,5,2};
    cout << "Original message: " << message << endl;
    
    int col=key.size();
    

    string encrypted = encrypt1(message,key);
    cout << "Encrypted message after first encyption: " << encrypted << endl;
    encrypted=encrypt(encrypted,col);
    cout << "Encrypted message after second encyption: " << encrypted << endl;

    string decrypted = decrypt(encrypted,col);
    cout << "Decrypted message after first decryption: " << decrypted << endl;
    decrypted = decrypt1(decrypted,key);
    cout << "Decrypted message after second decryption: " << decrypted << endl;

    return 0;
}


