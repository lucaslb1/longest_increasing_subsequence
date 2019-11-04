def lis(i): # may have to account for special case of last digit
    if m[i] != -1:
        return m[i]   
    else:
        max_len = 1
        for j in range(i+1, len(s)):
            if s[j] > s[i]:
                temp_len = lis(j)+1
                if max_len < temp_len:
                    max_len = temp_len
            
        m[i] = max_len
        return max_len


s = [11,17,5,8,6,4,7,12,3]

m = [-1]* len(s)
m[len(s)-1] = 1

for i in range(len(s)):
    lis(i)
    
print("Longest increasing subsequence: " + str(max(m)))
print(m)
