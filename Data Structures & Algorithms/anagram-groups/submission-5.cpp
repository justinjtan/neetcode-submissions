class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string,vector<string>> hashmap;
        for(string str : strs){
            string temp = str;
            std::sort(str.begin(), str.end());
            hashmap[str].push_back(temp);
        }
        for(const auto& pair : hashmap){
            res.push_back(pair.second);
        }
        return res;
    }
};
