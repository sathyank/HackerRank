#include <bits/stdc++.h>

using namespace std;

long getWays(int n, int m,vector < long > c){
    vector<long> nways(n+1);
    nways[0] = 1;
    for(int i=0;i<m;i++)
    {
        for(int j=c[i];j<=n;j++)
        {
            nways[j] += nways[j-c[i]];
        }
    }
    return nways[n];
}

int main() {
    int n;
    int m;
    cin >> n >> m;
    vector<long> c(m);
    for(int c_i = 0; c_i < m; c_i++){
       cin >> c[c_i];
    }
    // Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    long ways = getWays(n,m, c);
    cout<<ways;
    return 0;
}
