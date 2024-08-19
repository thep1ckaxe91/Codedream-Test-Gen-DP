// 213
#include <bits/stdc++.h>
using namespace std;

const int mod = 1e9 + 7;
const int oo = 1e4 + 3;

int n, k;
int mp[oo], f[oo];

int cal(int i)
{
    if (mp[i])
        return 0;
    if (i == n)
        return 1;

    if (f[i] != -1)
        return f[i];

    f[i] = cal(i + 1) + cal(i + 2);
    f[i] %= mod;

    return f[i];
}

int main()
{
    cin >> n >> k;
    for (int i = 1; i <= k; i++)
    {
        int x;
        cin >> x;
        mp[x] = 1;
    }

    memset(f, -1, sizeof(f));
    cout << cal(1);

    return 0;
}

//