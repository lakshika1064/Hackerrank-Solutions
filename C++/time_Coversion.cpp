#include<iostream>
#include<sstream>
using namespace std;

string timeConversionFunction(string str)
{
    int len;
    int h1 = (int)str[1] - '0'; 
    int h2 = (int)str[0] - '0'; 
    int hh = (h2 * 10 + h1 % 10); 
  
    len=str.size();
    if (str[len-2]=='A')						//for AM 
        {
            if(hh==12)
	    {
		    str.resize(len-2);
                    return str.replace(0,2,"00");
	    }
            else
	    {
                     str.resize(len-2);
                    return str;
	    }
	}

    else if(str[len-2]=='P')					//for PM
    {
        if(hh==12)
	{	
             str.resize(len-2);
             return str;
	}        
	else
    	{
            hh=hh+12;
	    str.resize(len-2);
            return str.replace(0,2,to_string(hh));
        }
    }
   str.resize(len-2);
   return str;   
}

int main()
{
    string str;
    getline(cin,str);
    cout<<timeConversionFunction(str);
    
}

