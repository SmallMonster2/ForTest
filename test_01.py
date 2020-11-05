'''
id 17. 电话号码的字母组合
'''

#["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]

class Solution(object):
    exact_dict = \
        {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

    def testV2(self,list1,list2):
        result_list = []
        for it1 in list1:
            for it2 in list2:
                result_list.append(it1+it2)
        return result_list

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = digits.split(',')
        list1 = self.exact_dict[digits[0]]; list2 = self.exact_dict[digits[1]]
        if len(digits)==0 or len(digits)==1:
            return_list = digits
            return return_list
        elif len(digits)==2:
            return_list = self.testV2(list1=list1,list2=list2)
            return return_list
        else:
            for key,value in enumerate(digits):
                if key != len(digits)-2:
                    list1 = self.testV2(list1=list1,list2=list2)
                    list2 = self.exact_dict[digits[key+2]]
                else:
                    return_list = self.testV2(list1=list1,list2=list2)
                    return return_list

if __name__ == '__main__':
    solution = Solution()
    print(solution.letterCombinations(digits="2,3,4,5,6"))