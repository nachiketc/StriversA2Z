class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # so we need to decide the structure
        # I am thinking we do a list of dictionarries for each index
        # each dictionary will have key, value as char, count of occurance
        # how do we compare dictionary and group them?

        # lets try to store values in dictionary
        # we iterate over each string and update dict
        strdict = {ch: 0 for ch in string.ascii_lowercase}
        # main dict that will keep track and will be used for hashmap
        maindict = defaultdict(list)


# approach 1
        # # iteratoe over list of strings
        # for i in range(len(strs)):
        #     for ch in strs[i]:
        #         strdict[ch]+=1
        #     # print( str(strdict))
        #     # now we have a dict tha contains anagram sturcture
        #     #  we want to hash this value with index as value and some key
        #     # we form a hashkey that we can store in maindict
        #     # key creations logic - alphabetcountalphabetcount....
        #     # if str(strdict) in maindict.keys():
        #     maindict[str(strdict)].append(strs[i])
        #     # or we just filter non zero key values and compare dict but that will also take time
        #     # each time reset values
        #     for key in strdict:
        #         strdict[key] = 0
        #     # print(list(maindict.values()))
        # return list(maindict.values())

# approach 2
        # optimised approach use sorted method at the string level and add it to dictionary
        maindict= defaultdict(list)
        # loop through strings
        for i in range(len(strs)):
            setstr = ''.join(sorted(strs[i])) #this will take the char and sort them

            maindict[setstr].append(strs[i])
        
        return list(maindict.values())