#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> arr;
  int n, a;
  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> a;
    arr.push_back(a);
  }
  reverse(arr.begin(), arr.end());
  for (int i = 0; i < n; i++) {
    cout << arr[i] << " ";
  }
}

