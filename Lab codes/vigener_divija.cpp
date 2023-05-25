#include <iostream>
#include <string>
using namespace std;
int main() 
{
	string pt;
	cout<<"Enter string "<<endl;
	cin>>pt;
	string key;
	cout<<"Enter key"<<endl;
	cin>>key;
	
	int n=pt.length();
	int m=key.length();
	
	int r=n/m;
	string s="";
	while(r--)
	{
	    s+=key;
	}
	r=n%m;
	int i=0;
	while(r--)
	{
	    s+=key[i];
	    i++;
	}
	string ct;
	for(int i=0;i<n;i++)
	{
	    char q='A'+(pt[i]+s[i])%26;
	    ct+=q;
	}
	cout<<"Ciphertext is: "<<ct<<endl;
	string dc;
	for(int i=0;i<n;i++)
	{
	    char q='A'+(ct[i]-s[i]+26)%26;
	    dc+=q;
	}
	cout<<"Plaintext is: "<<dc<<endl;

}
