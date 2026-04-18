class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> mappa;
        for (int i = 0; i < nums.size(); i++){
            int n = nums[i];
            int t = target - n;
            if (mappa.count(t)){
                return {mappa[t], i};
            }
            mappa[n] = i;
        }
        return {};
    }
};