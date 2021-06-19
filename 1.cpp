#include<iostream>
#include<vector>

using namespace std;

class Solution {
  public:
	vector<int> twoSum(vector<int>& nums, int target){
        vector<int> ret;
        for(int i=0;i<nums.size();i++){
            for(int j=0;j<nums.size();j++){
                if(nums[i] + nums[j] == target and i != j){
                    ret.push_back(i);
                    ret.push_back(j);
                    return ret;
                }
            }
        }
        return ret;
	};
};

int main (){
    // Solution sol;
    // vector<int> v;
    // int target = 6;
    // v = {3, 3};
    // vector<int> ans = sol.twoSum(v, target);
    // for(int i=0;i<ans.size();i++){
    //     cout << ans[i] << endl;
    // }
    int n, target;
    cin >> n >> target;
    int arr[n], ans[2];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }
    for(int i=0;i<n;i++){
        cout << arr[i] << endl;;
    }
    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(arr[i] + arr[j] == target) {
                ans[0] = i;
                ans[1] = j;
            }
        }
    }
    for(int i=0;i<2;i++){
        cout << ans[i] << " ";
    }
    return 0;
};