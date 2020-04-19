#include <iostream>
#include <string>
using namespace std;

int main() {
	string a,b;
    cin>>a;
    cin>>b;
    int ken,len;
    len=a.size();
    ken=b.size();
    cout<<len<<" "<<ken<<endl;
    cout<<a<<b<<endl;
    char temp;
    temp=a[0];
    a[0]=b[0];
    b[0]=temp;
    cout<<a<<" "<<b;
    return 0;
}


