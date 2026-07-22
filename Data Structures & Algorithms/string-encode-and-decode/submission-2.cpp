class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for(string str : strs){
            res += str + ".";
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string curr = "";
        for(char c : s){
            if(c == '.'){
                res.push_back(curr);
                curr = "";
            }else{
                curr += c;
            }
        }
        return res;
    }
};
