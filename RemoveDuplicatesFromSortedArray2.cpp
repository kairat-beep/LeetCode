class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 0, right = 0;
        while(right < nums.size()){
            int counted = 0;
            while(right<nums.size() && nums[right] == nums[left]){
                nums[left+counted] = nums[right];
                right++;
                counted++;
            }
            left += std::min(counted,2);
            if (right<nums.size())
                nums[left] = nums[right];
        }
        return left;
    }
};
