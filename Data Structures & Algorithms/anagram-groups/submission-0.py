class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = defaultdict(list) # to map the charCount to the list of Anagrams

        for s in strs:
            count = [0] * 26 # a to z -> this 
                             #should give a list [0,...,0] 26x

            for c in s:
                count[ord(c) - ord("a")] +=1 # will compute ascii of char(c) do 
                                         #the difference with the ascii # of "a"
            results[tuple(count)].append(s)
        return list(results.values())