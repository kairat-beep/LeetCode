class Solution {
public:
    vector<int> countBits(int n) {
        int  current,accum,shifted ;
        vector<int> result;
        result.resize(n+1);
        for (int i = 0; i <=n;i++){
            accum = 0;
            shifted = 0;
            current = i;
            while (shifted != 32){
                accum +=  (current>>(shifted++)) & 1;
            }
            result[i]=accum;
        }
        return result;
    }
};
