#include<bits/stdc++.h>
using namespace std;
int main(){
    int x;
    cin >> x;
    for (int i=0;i<2*x-1;i++){
        for (int j=0; j<2*x-1;j++){
            int left=j;
            int top=i;
            int right=2*x-2-j;
            int bottom=2*x-2-i;
            cout << x- min(min(left,right),min(top,bottom));

        }

        cout << endl;
    }
    return 0;
}