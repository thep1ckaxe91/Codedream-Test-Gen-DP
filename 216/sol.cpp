// Sero solution
// #include<bits/stdc++.h>
// using namespace std;


// const int oo = 1e5 + 5;

// int n;
// int a[oo], b[oo], c[oo];
// int f[oo][5];


// int present(int i, int type)
// {
//     if(type == 1) return a[i];
//     else if(type == 2) return b[i];
//     else return c[i];
// }


// int cal(int i, int type)
// {
//     if(i > n) return 0;
//     if(f[i][type] != -1) return f[i][type];


//     for(int newType = 1; newType <= 3; newType++) 
//     {
//         if(newType == type) continue;
//         cerr << &f[i][type] << endl;
//         f[i][type] = max(f[i][type], cal(i + 1, newType) + present(i, newType));
//     }

//     return f[i][type];
// }


// int main()
// {
//     cin >> n;
//     for(int i = 1; i <= n; i++) cin >> a[i] >> b[i] >> c[i];

//     memset(f, -1, sizeof(f));
//     cout << cal(1, 0);    


//     return 0;
// }

// // checker sol

#include<bits/stdc++.h>
#define int long long
#define fast_io ios_base::sync_with_stdio(false), cin.tie(0);
#define bruh signed main
#define easy return 0

using namespace std;

bruh() {
    fast_io

    int n;
    cin >> n;

    int dp[n][3];
    int a[n][3];

    for (int i = 0; i < n; i++) {
        cin >> a[i][0] >> a[i][1] >> a[i][2];
    }

    dp[0][0] = a[0][0];
    dp[0][1] = a[0][1];
    dp[0][2] = a[0][2];

    for (int i = 1; i < n; i++) {
        dp[i][0] = a[i][0] + max(dp[i-1][1], dp[i-1][2]); // màu đỏ
        dp[i][1] = a[i][1] + max(dp[i-1][0], dp[i-1][2]); // màu xanh
        dp[i][2] = a[i][2] + max(dp[i-1][0], dp[i-1][1]); // màu vàng
    }

    int result = max(dp[n-1][0], max(dp[n-1][1], dp[n-1][2]));

    cout << result << endl;
    easy;
}
