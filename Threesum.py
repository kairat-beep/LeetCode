from collections import defaultdict
class Solution:
    def threeSum(self, nums )  :
        sorted_nums = sorted(nums)
        index_num = defaultdict(list)
        records = defaultdict(lambda : defaultdict(set))

        print(str(index_num))
        only2=sorted_nums[:2]
        i=2
        count_zeroes = only2[0]==0 + only2[1]==0
        while i < len(nums):
            if  sorted_nums[i]==0:
                count_zeroes +=1 
            if only2[-1] == only2[-2] == sorted_nums[i] :
                if  sorted_nums[i]==0:
                    count_zeroes +=1 
                i+=1
                continue
            only2.append(sorted_nums[i])
            i+=1
        for index,val in enumerate(only2):
            index_num[val].append(index)
        pairs = list() 
        for index, val in enumerate(only2):
            for index_n,val_n in enumerate(only2[index+1:],index+1):
                remainder = -(val + val_n)
                if remainder >= val_n and remainder in index_num and index_num[remainder][-1]>index_n:
                    print(val,val_n,remainder)
                    records[val][val_n].add(remainder)
                
        to_return = []
        for k,v in records.items():
            for kn,vn in v.items():
                to_return.extend([(k, kn, _) for _ in vn])
        if count_zeroes >=3:
            to_return.append([0,0,0])
        return to_return
