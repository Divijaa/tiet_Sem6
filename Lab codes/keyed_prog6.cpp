#include <iostream>
using namespace std;
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_map>
#include <stack>

string encrypt(string text,vector<int> key){
    int q=key.size();
    int n=text.length()/q;
    int i=0;
    string ans="";
   
    for(int j=0;j<n;j++){
        string test="";
        for(int j=0;j<q;j++){
            test+="*";
        }
        //Reordering acc to key
        for(int y=0;y<q;y++){
            test[key[y]-1]=text[i];
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
    for(int j=0;j<q;j++){
        test+="*";
    }
    for(int y=0;y<q;y++){
        test[key[y]-1]=yo[i];
        i++;
    }
    ans+=test;
    return ans;
    
}
string decrypt(string text,vector<int> key){
    int q=key.size();  //no. of cols
    int n=text.length()/q;  //no. of rows
    int i=0;
    string ans="";
   
    for(int j=0;j<n;j++){
        string test="";
        string t=text.substr(i,q);
        for(int y=0;y<q;y++){
            test+=t[key[y]-1];
            i++;
        }
        ans+=test;
    }
    
    return ans;
    
}
int main(){
    
    cout<<"this is keyed cipher. \n";
    vector<int> key={3,1,4,5,2};
    string text="enemyattackstonight";
    string encrypted =encrypt(text, key);
    cout<<"Encrypted text is: "<<encrypted<<endl;
    string decrypted=decrypt(encrypted, key);
    cout<<"Decrypted text is: "<<decrypted<<endl;
}

