class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            sortedstr = "".join(sorted(s))

            if sortedstr not in groups:
                groups[sortedstr] = []

            groups[sortedstr].append(s)

        return list(groups.values())



