#include <iostream>
using namespace std;
#include <string>
#include <vector>
#include <set>
#include <map>
 /* Playfair cipher  */
int main() {

    cout<<"Enter plaintext"<<endl;
    string pt;
    cin>>pt;
    cout<<"Enter key"<<endl;
    string key;
    cin>>key;
    vector<vector<char>> vec( 5 , vector<char> (5, '*'));
    int n=key.length();
    int no=pt.length();
    int t=0;
    set<char> s;
map<char,pair<int,int>> m;
    int flag=0;
     for(int i=0;i<5;i++){
         for(int j=0;j<5;j++){
             vec[i][j]=key[t];
             m[key[t]]=make_pair(i, j);
             s.insert(key[t]);
             
             t++;
             if(t==n){
                 flag=1;
                 break;
             }
         }
         if(flag==1){
             break;
         }
     }


    int k=0;
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            if(vec[i][j]=='*'){
                if(k==9){
                    k++;
                    
                }
                 while(s.find('A'+k)!=s.end()){
                    k++;
                }
                vec[i][j]='A'+k;
                m['A'+k]=make_pair(i, j);
                
                k++;
            }
        }
    }
    cout<<endl;
    
    for(int i=0;i<5;i++){
        for(int j=0;j<5;j++){
            cout<<vec[i][j]<<" ";
        }
        cout<<endl;
    }
    int i=0;
    int j=1;
    string ct;
while(j<no){
        if(pt[i]!=pt[j]){
            if(m[pt[i]].first==m[pt[j]].first){
                ct+=vec[m[pt[i]].first][(m[pt[i]].second+1)%5];
                ct+=vec[m[pt[j]].first][(m[pt[j]].second+1)%5];
                i+=2;
                j+=2;
            }else if(m[pt[i]].second==m[pt[j]].second){
                ct+=vec[(m[pt[i]].first+1)%5][m[pt[i]].second];
                ct+=vec[(m[pt[j]].first+1)%5][m[pt[j]].second];
                i+=2;
                j+=2;
            }else{
                ct+=vec[m[pt[i]].first][m[pt[j]].second];
                ct+=vec[m[pt[j]].first][m[pt[i]].second];
                i+=2;
                j+=2;
            }
        }else{
            if(m[pt[i]].first==m['X'].first){
                ct+=vec[m[pt[i]].first][(m[pt[i]].second+1)%5];
                ct+=vec[m['X'].first][(m['X'].second+1)%5];
 i++;
                j++;
            }else if(m[pt[i]].second==m['X'].second){
                ct+=vec[(m[pt[i]].first+1)%5][m[pt[i]].second];
                ct+=vec[(m['X'].first+1)%5][m['X'].second];
                i++;
                j++;
            }else{
                ct+=vec[m[pt[i]].first][m['X'].second];
                ct+=vec[m['X'].first][m[pt[i]].second];
                i++;
                j++;
            }
            
        }
    }
    if(i<no){
        if(m[pt[i]].first==m['Z'].first){
            ct+=vec[m[pt[i]].first][(m[pt[i]].second+1)%5];
            ct+=vec[m['Z'].first][(m['Z'].second+1)%5];
            i++;
 }else if(m[pt[i]].second==m['Z'].second){
            ct+=vec[(m[pt[i]].first+1)%5][m[pt[i]].second];
            ct+=vec[(m['Z'].first+1)%5][m['Z'].second];
            i++;
            
        }else{
            ct+=vec[m[pt[i]].first][m['Z'].second];
            ct+=vec[m['Z'].first][m[pt[i]].second];
            i++;
            
        }
    }
    
    cout<<"Ciphertext is: "<<ct<<endl;
}
