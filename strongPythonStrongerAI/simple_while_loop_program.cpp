#include<iostream>
#include<string>
using namespace std;

int main(){
    char ch;
    string str;

    do{
        cout <<"Enter full name: ";
        cin.ignore();
        getline(cin,str);
        cout <<"If you want to enter another name enter (y) else enter (n): ";
        cin >>ch;
        
        if(ch =='n' || ch == 'N')
        break;
    }
    while(true);
    return 0;
}