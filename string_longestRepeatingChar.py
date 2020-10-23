"""
Tucker Ferguson 10/9/2020

@description https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.

"""
class Solution:
    def getWeight(self,subStr,k):
        weight = 1
        kValue = k
        while kValue >= 0:
            if kValue == 0:
                for i in range(1,len(subStr)):
                    if subStr[i-1] == subStr[i]:
                        weight += 1
                    elif subStr[i-1] != subStr[i]:
                        return weight
                       
                    
                

            elif kValue > 0:
                for i in range(1,len(subStr)):
                    if subStr[i-1] == subStr[i]:
                        weight += 1
                    else:
                        kValue -= 1
                        weight += 1
                    if kValue == 0:
                        i == len(subStr) - 1;
                        
        return weight


    def characterReplacement(self,inputStr,k):
        weightDict = {}
        subStringList = []
        for i,char in enumerate(inputStr):
            temp = ""
            for x in range(i,len(inputStr)):
                temp = temp + (inputStr[x])
                
                subStringList.append(temp)
        for subString in subStringList:
            if len(subString) <= k:
                weightDict[subString] = len(subString)
            else:
                weightDict[subString] = self.getWeight(subString,k)
                weight = 0
     
        return max(weightDict.values())

s = Solution.characterReplacement(Solution,"ABCDE",1)
print(s)
