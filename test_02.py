'''
id:49. 字母异位词分组
'''
a=[]
class Solution:
    def sort(self,list1):
        param ={}
        list2 = [i.lower() for i in list1]
        list3 = []
        for i1 in list2:
            list3.append(''.join(sorted(i1)))
        for idx,value in enumerate(list3):
            exact_num=param.get(value,[])
            param.update({value:[list1[idx]]+exact_num})
        return list(param.values())

    def groupAnagrams(self, strs: list) -> list:
        if len(strs)==0:return [strs]
        elif len(strs)==1:return [strs]
        params = {}
        result_list=[]
        for it in strs:
            exact_list = params.get(len(it),[])
            params.update({len(it): [it]+exact_list})
        for key,item in enumerate(list(params.keys())):
            tmp_list = self.sort(list1=params[item])
            result_list+= tmp_list
        return result_list

if __name__ == '__main__':
    solution = Solution()
    solution.groupAnagrams(strs=a)