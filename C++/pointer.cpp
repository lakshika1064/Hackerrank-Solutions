#include<iostream>
#include<math.h>
using namespace std;
void update(int,int);
int main()
{
    int a,b;
    cin>>a>>b;
    update(a,b);
}
void update(int a,int b)
{
    int k,l;
    k=a+b;
    l=abs(a-b);
    cout<<k<<endl<<l;
}
