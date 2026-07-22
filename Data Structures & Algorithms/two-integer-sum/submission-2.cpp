class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> hashmap;
        for(int i=0; i<nums.size(); i++){
            if(hashmap[target - nums[i]] != 0){
                return {hashmap[target - nums[i]] - 1, i};
            }
            hashmap[nums[i]] = i + 1;
        }
    }
};
