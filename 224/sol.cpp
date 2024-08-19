
// 224 
#include<bits/stdc++.h>
using namespace std;

#define int long long

const int oo = 1e3 + 2;
const int inf = 1e18;



int n, k;
int a[oo], f[oo][oo];


int cal(int i, int tickets)
{
    if(i > n)
    {
        if(tickets == n) return 0;
        else return inf;
    }

    if(tickets == n) return 0;

    if(f[i][tickets] != -1) return f[i][tickets];


    int res = inf;
    for(int j = 0; j <= min(n - tickets, k); j++) 
    {
        res = min(res, cal(i + 1, tickets + j) + j * a[i]);
    }

    return f[i][tickets] = res;
}

int32_t main()
{
    cin >> n >> k;
    for(int i = 1; i <= n; i++) cin >> a[i];

    memset(f, -1, sizeof(f));
    cout << cal(1, 0);

    return 0;
}