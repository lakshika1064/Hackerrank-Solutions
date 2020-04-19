#include<iostream>
using namespace std;
int test(int,int,int,int);
int main()
{
    int a,b,c,d,k;
    cin>>a>>b>>c>>d;
    cout<<test(a,b,c,d);
    return 0;
}
int test(int a, int b, int c, int d)
{
    if(a>b && a>c && a>d)
    {
        return a;
    }
    else 
    {
        if(b>c && b>d && b>a)
            return b;
        else
        {
            if (c>b && c>a && c>d)
                return c;
            else 
                return d;
        }
    }
}
