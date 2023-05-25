#include <iostream>
using namespace std;
#include <string>
int main() 
{
	string pt;
	cout<<"Enter plaintext string "<<endl;
	cin>>pt;
	char key;
	cout<<"Enter Autokey"<<endl;
	cin>>key;
	
	    int n=pt.length();
	    string s=pt.substr(0,n-1);
	    s=key+s;
	    cout<<"Concatenated string is: "<<s<<endl;
	    string ct;
	 
	    for(int i=0;i<n;i++){
	        char c='A'+(pt[i]+s[i])%26;
	        ct+=c;
	    }
	    cout<<"Ciphertext is: "<<ct<<endl;
	
	    for(int i=0;i<n;i++){
	        char c='A'+(ct[i]-s[i]+26)%26;
	        pt[i]=c;
	    }
	    cout<<"Plaintext is: "<<pt<<endl;
}
