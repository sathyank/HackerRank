#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the array2D function below.
 */
int array2D(vector<vector<int>> arr) {
    int max = -1000,sum,i,j;
    for(i=0;i<4;i++){
        for(j=0;j<4;j++){
            sum = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2];
            if(sum > max)
                max = sum;
        }
    }
    return max;
}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    vector<vector<int>> arr(6);
    for (int arr_row_itr = 0; arr_row_itr < 6; arr_row_itr++) {
        arr[arr_row_itr].resize(6);

        for (int arr_column_itr = 0; arr_column_itr < 6; arr_column_itr++) {
            cin >> arr[arr_row_itr][arr_column_itr];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = array2D(arr);

    fout << result << "\n";

    fout.close();

    return 0;
}
