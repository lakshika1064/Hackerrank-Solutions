#include<iostream>
#include<vector>
using namespace std;

int main()
{
int n,k,q,o,t,val;
cin>>n>>q;			//array size and no. of queries
vector<vector<int>> v1;						//creating a 2D vector
for(auto i=0;i<n;i++)
	{	
		cin>>k;		
		vector<int> row;		//creating a row vector first and storing values
		for(auto j=0;j<k;j++)
			{
			cin>>val;
			row.push_back(val);
			}
	v1.push_back(row);				//now here we are pushing that whole vector into the vector indices
	row.clear();
	}
for(int k=0;k<n;k++)
	{	
	cin>>o>>t;
	cout<< v1[o][t] << " ";
	}

	
return 0;
}
