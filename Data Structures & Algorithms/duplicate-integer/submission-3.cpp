class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> hashmap;
        for (int num : nums){
            if (hashmap[num] == 1){
                return true;
            }
            hashmap[num] = 1;
        }
        return false;
    }
};