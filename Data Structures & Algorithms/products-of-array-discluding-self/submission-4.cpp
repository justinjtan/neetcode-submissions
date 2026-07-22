class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> vpref(nums.size(), 1), vsuff(nums.size(), 1), vres;
        int pref = 1;
        for(int i=1; i<nums.size(); i++){
            pref *= nums[i - 1];
            vpref[i] = pref;
        }
        int suff = 1;
        for(int i=nums.size() - 2; i >= 0; i--){
            suff *= nums[i + 1];
            vsuff[i] = suff;
        }
        for(int i = 0; i < nums.size(); i++){
            vres.push_back(vpref[i] * vsuff[i]);
        }
        return vres;
    }
};
