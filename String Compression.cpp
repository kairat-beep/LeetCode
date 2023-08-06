class Solution {
public:
    int compress(vector<char>& chars) {
        int start = 0, j=1;
        for (int i = 0; i < chars.size(); i=j){
            for (j= i+1;j<chars.size() && chars[i] == chars[j];j++);
            int size = j-i;
            if(size>1)
                start = resize(chars, chars[i], start, size);
            else{
                chars[start++]=chars[i];
            }
        }
        return start;
    }

    //Guaranteed extra space to map size > String
    int resize(vector<char>&chars,char c, int start, int size){
        string num = std::to_string(size);
        chars[start++] = c;
        for(int i = 0; i <num.size();i++){
            chars[start++] = num[i];
        }
        return start;
    }
};
