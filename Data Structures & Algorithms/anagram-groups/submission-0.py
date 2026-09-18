class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        strs_map = {}

        for i in strs:
            if ''.join(sorted(i)) in strs_map:
                strs_map[''.join(sorted(i))].append(i)
            else:
                strs_map[''.join(sorted(i))] = [i]
        
        for k, v in strs_map.items():
            result.append(v)

        return result
