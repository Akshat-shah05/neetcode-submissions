#include <vector>
#include <unordered_map>
#include <map>
#include <string>

class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        std::vector<std::vector<std::string>> ans;
        std::map<std::vector<int>, std::vector<std::string>> anagrams;

        for (auto& str : strs) {
            std::vector<int> freq(26, 0);
            for (auto chr : str) {
                freq[chr - 'a'] += 1;
            }
            anagrams[freq].push_back(str);
        }

        for (auto& [k, v] : anagrams) {
            ans.push_back(v);
        }

        return ans;
    }
};
