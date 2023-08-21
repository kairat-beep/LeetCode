class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int left = 0, right = 0;
        while(right < nums.size()){
            while(right<nums.size() && nums[left]==nums[right]){
                nums[left]=nums[right];
                right++;
            }

            if(right<nums.size())
            nums[++left] = nums[right];
        }
        return left+1;
    }
};
