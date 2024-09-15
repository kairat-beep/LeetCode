class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int number = 0;
        for (int i: nums){
            number ^= i;
        }
        return number;
    }
};
