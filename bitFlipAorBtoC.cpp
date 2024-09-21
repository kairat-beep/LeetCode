class Solution {
public:
    int minFlips(int a, int b, int c) {
        int flips = 0;
        int a1,b1,c1 ;
        while(a > 0 || b>0 || c>0){
            a1 = a&1;
            b1 = b&1;
            c1 = c&1;
            if((a1|b1) != c1){
                flips += c1==1?1:(a1 * b1 + 1);
            } 
            a = a >> 1;
            b = b >> 1;
            c = c >> 1;
        }
        return flips;
    }

};
