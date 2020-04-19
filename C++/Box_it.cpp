#include<bits/stdc++.h>

using namespace std;
//Implement the class Box  
class Box
{
private:
int l,b,h;
//l,b,h are integers representing the dimensions of the box
public:
// The class should have the following functions : 

// Constructors: 
 Box()
 {
     l=0;b=0;h=0;
 }

Box(int length,int breath,int height)
{
    l=length;b=breath;h=height;
}

Box(Box &B)
{
    l=B.l;h=B.h;b=B.b;
}

// int getLength(); // Return box's length
int getLength()
{
    return l;
}

// int getBreadth (); // Return box's breadth
int getBreadth()
{
    return b;
}
// int getHeight ();  //Return box's height
int getHeight()
{
    return h;
}
// long long CalculateVolume(); // Return the volume of the box
long long CalculateVolume()
{
        return(l*b*h);
}

//Overload operator < as specified
//Overload operator < as specified
friend bool operator < ( Box& A, Box& B)
{
    if ((A.l<B.l) || ((A.b<B.b) && (A.l==B.l)) || ( (A.h<B.h) && (A.b==B.b) && (A.l==B.l) ))
         return true;            
    else
        return false;
}

friend ostream& operator << (ostream& out , Box& B)
{	
    out <<B.l<<" "<<B.b<<" "<<B.h;   
    return out;

}
//Overload operator << as specified
//ostream& operator<<(ostream& out, Box& B)
};

void check2()
{
	int n;
	cin>>n;
	Box temp;
	for(int i=0;i<n;i++)
	{
		int type;
		cin>>type;
		if(type ==1)
		{
			cout<<temp<<endl; //<<
		}
		if(type == 2)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			temp=NewBox;
			cout<<temp<<endl; //<<
		}
		if(type==3)
		{
			int l,b,h;
			cin>>l>>b>>h;
			Box NewBox(l,b,h);
			if(NewBox<temp)
			{
				cout<<"Lesser\n";
			}
			else
			{
				cout<<"Greater\n";
			}
		}
		if(type==4)
		{
			cout<<temp.CalculateVolume()<<endl;
		}
		if(type==5)
		{
			Box NewBox(temp);
			cout<<NewBox<<endl;

		}

	}
}

int main()
{
	check2();
}		
