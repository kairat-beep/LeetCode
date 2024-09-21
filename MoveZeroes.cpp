#include <vector>
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        std::vector<int>::iterator i = nums.begin();
        std::vector<int>::iterator j = i + 1, end = nums.end() ;

        while(i<end){
            while( i<end && *i != 0 ){
                i++;
            }
            if ( i > j)  j = 1 + i;
            while (j<end && *j == 0) j++;
            if(i < end && j < end)
            {
                *i = (*i)^(*j);
                *j = (*i)^(*j);
                *i = (*i)^(*j);
            }
            i++;j++;
        }
    }
};
