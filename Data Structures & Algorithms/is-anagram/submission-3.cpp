#include <vector>

class Solution {
public:
    bool isAnagram(string s, string t) {
        vector<int> freqs(26, 0);
        for (char chr : s) {
            freqs[chr - 'a'] += 1;
        }

        for (char chr : t) {
            freqs[chr - 'a'] -= 1;
        }

        for (int i : freqs) {
            if (i != 0) {
                return false;
            }
        }
        return true;
        
    }
};
