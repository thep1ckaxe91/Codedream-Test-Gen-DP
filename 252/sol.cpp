// 252 
#include<bits/stdc++.h>
using namespace std;

int n, m;
int res;
string s, a, b;
int f[102][2][10004];

int main()
{
    cin >> n >> s;
    cin >> a >> b;

    m = s.size();
    s = " " + s;
    a = " " + a;
    b = " " + b;

    
    for(int i = 0; i <= n; i++) f[i][0][0] = f[i][1][0] = 1;
    for(int i = 1; i <= n; i++)
    {
        for(int k = 1; k <= m; k++)
        {
            if(k > i) break;
            if(a[i] == s[k])
            {
                for(int j = i-1; j >= 0; j--)
                {
                    if(b[j] == s[k-1]) f[i][0][k] += f[j][1][k-1];
                }
            }
            
            if(b[i] == s[k])
            {
                for(int j = i-1; j >= 0; j--) 
                {
                    if(a[j] == s[k-1]) f[i][1][k] += f[j][0][k-1];
                }
            }
        }
    }


    for(int i = 1; i <= n; i++) res += f[i][0][m] + f[i][1][m];
    cout << res;



    return 0;
}