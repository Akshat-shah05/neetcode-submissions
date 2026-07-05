#include <unordered_map>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int, int> needed;

        for (int i = 0; i < nums.size(); ++i) {
            int required = target - nums[i];
            if (needed.contains(required)) {
                std::vector<int> ans = {needed[required], i};
                return ans;
            }
            needed[nums[i]] = i;
        }
        return {0, 0};
    }
};
