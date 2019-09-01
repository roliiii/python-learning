class Solution:
  def lengthOfLongestSubstring(self, s):
    longestLength=0
    i,j=0,0
    usedChars = dict()
    while j < len(s):
      if(s[j] in usedChars): #repeating char
        i=max(usedChars[s[j]]+1,i)
        usedChars[s[j]]=j
      else: #new char
        usedChars[s[j]]=j
        if(j-i+1 > longestLength):
          longestLength=j-i+1

      j+=1
        
    return longestLength

print(Solution().lengthOfLongestSubstring('231234561234123'))
# 6
