class Solution:
    def Anagrams(self, words, n):
        '''
        words: list of word
        n:      no of words
        return : list of group of anagram {list will be sorted in driver code (not word in grp)}
        '''
        
        #code here
        d = dict()
        for i in words:
           s = ''.join(sorted(i))
           if d.get(s,0) == 0:
               d[s] = [i]
           else:
               d[s].append(i)
        ans = []
        for i in d:
           ans.append(d[i])
        return ans

if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        n = int(input())
        words = input().split()

        ob = Solution;
        ans = ob.Anagrams(words , n)

        for (grp) in sorted(ans):
            for word in grp:
                print(word , end='')
            print()

    