//rail fence
string encrypt(string message) {
    int len = message.length();
    int c = ceil(len / 2.0);
    char matrix[2][c];
    int k = 0;

    // Fill the matrix with the message characters
    for (int i = 0; i < c; i++) {
        for (int j = 0; j < 2; j++) {
            if (k < len)
                matrix[j][i] = message[k++];
            else
                matrix[j][i] = ' ';
        }
    }

    // Read the characters from the matrix column-wise
    string encrypted = "";
    for (int j = 0; j < 2; j++) {
        for (int i = 0; i < c; i++) {
            encrypted += matrix[j][i];
        }
    }

    return encrypted;
    // Function to decrypt the message using transposition keyless cipher
string decrypt(string message) {
    int i=0;
    int j;
    if(message.length()%2==0){
        j=message.length()/2;
    }else{
        j=message.length()/2+1;
    }
    string ans="";
    while(j<message.length()){
        ans+=message[i];
        ans+=message[j];
        i++;
        j++;
    }
    if(message.length()%2==1){
        ans+=message[i];
    }
    return ans;
    
}

int main() {
    string message = "meetmeatthepark";
    cout << "Original message: " << message << endl;

    string encrypted = encrypt(message);
    cout << "Encrypted message: " << encrypted << endl;

    string decrypted = decrypt(encrypted);
    cout << "Decrypted message: " << decrypted << endl;

return 0;
}

