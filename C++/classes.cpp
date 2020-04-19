#include <iostream>
using namespace std;
class Student {
public:
  int age, standard;
  char first_name[51], last_name[51];
  void get_detail() {
    cin >> age;
    cin >> first_name;
    cin >> last_name;
    cin >> standard;
  }
};
int main() {
  Student st;
  st.get_detail();
  cout << st.age << endl;
  cout << st.last_name << ", " << st.first_name << endl;
  cout << st.standard << endl << endl;
  cout << st.age << "," << st.first_name << "," << st.last_name << ","
       << st.standard;
  return 0;
}

