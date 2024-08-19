// 216
#include<bits/stdc++.h>
using namespace std;


const int oo = 1e5 + 5;

int n;
int a[oo], b[oo], c[oo];
int f[oo][5];


int present(int i, int type)
{
    if(type == 1) return a[i];
    else if(type == 2) return b[i];
    else return c[i];
}


int cal(int i, int type)
{
    if(i > n) return 0;
    if(f[i][type] != -1) return f[i][type];


    for(int newType = 1; newType <= 3; newType++) 
    {
        if(newType == type) continue;
        f[i][type] = max(f[i][type], cal(i + 1, newType) + present(i, newType));
    }

    return f[i][type];
}


int main()
{
    cin >> n;
    for(int i = 1; i <= n; i++) cin >> a[i] >> b[i] >> c[i];

    memset(f, -1, sizeof(f));
    cout << cal(1, 0);    


    return 0;
}