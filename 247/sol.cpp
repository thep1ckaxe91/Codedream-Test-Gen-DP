// 247
#include <bits/stdc++.h>
using namespace std;

int n, m, T;
int f[1003][1003], pref[1003];

struct huy
{
    int val, type;
    bool operator<(const huy &o)
    {
        return val != o.val ? val < o.val : type < o.type;
    }
} a[1003];

int cal(int i, int t)
{
    if (i > m + n)
        return 0;
    if (f[i][t] != -1)
        return f[i][t];

    int res = 0;

    // xe nho
    if (a[i].type == 1 && t + a[i].val <= T)
    {
        res = max(res, cal(i + 1, t + a[i].val) + 1);
    }
    // xe to
    if (pref[i] - t <= T)
    {
        res = max(res, cal(i + 1, t) + 1);
    }

    return f[i][t] = res;
}

int main()
{
    cin >> T;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        cin >> a[i].val;
        a[i].type = 1;
    }

    cin >> m;
    for (int i = 1; i <= m; i++)
    {
        cin >> a[i + n].val;
        a[i + n].type = 2;
    }

    sort(a + 1, a + 1 + m + n);

    for (int i = 1; i <= m + n; i++)
    {
        pref[i] = pref[i - 1] + a[i].val;
    }
    memset(f, -1, sizeof(f));
    cout << cal(1, 0);

    return 0;
}