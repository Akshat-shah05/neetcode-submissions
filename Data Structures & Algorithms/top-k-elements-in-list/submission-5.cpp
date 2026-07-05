#include <vector>
#include <unordered_map>
using namespace std;

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<vector<int>> res(nums.size() + 1);
        unordered_map<int, int> freqs;

        for (auto i : nums) {
            if (freqs.contains(i)) {
                freqs[i] += 1;
            }
            else {
                freqs[i] = 1;
            }
        }

        for (auto& [k, v] : freqs) {
            res[v].push_back(k);
        }

        vector<int> ans;

        for (int i = nums.size(); i >= 0; --i) {
            for (int j : res[i]) {
                ans.push_back(j);
                k -= 1;
                if (k == 0) {
                    return ans;
                }
            }
            if (k == 0) {
                return ans;
            }
        }
        return ans;


    }
};
