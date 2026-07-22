class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> hashmap, hashmap2;
        for(char c : s){
            hashmap[c] += 1;
        }
        for(char c : t){
            hashmap2[c] += 1;
        }
        return hashmap == hashmap2;
    }
};
