#assumes that all digits are greater than or equal to 0
# s is subsequence
# m is an array to save subprolem solutions to
# i is the index of the current subproblem being calculated
def lis(i,s,m):
    if m[i] != -1:
        return m[i]   
    else:
        max_len = 1
        for j in range(i+1, len(s)):
            if s[j] > s[i]:
                temp_len = lis(j,s,m)+1
                if max_len < temp_len:
                    max_len = temp_len
            
        m[i] = max_len
        return max_len


def longest_increasing_subsequence(s):
    m = [-1]* len(s) #saves subproblem solutions
    m[len(s)-1] = 1
    for i in range(len(s)):
        lis(i,s,m)
        
    print("Longest increasing subsequence: " + str(max(m)))
    print(m)
    return max(m)


sequence1 = [11,17,5,8,6,4,7,12,3]
sequence2 = [1, 2, 3, 4, 5, 6, 7, 8,9, 10]
sequence3 = [10,9,8,7,6,5,4,3,2,1]

longest_increasing_subsequence(sequence1) #longest 4
longest_increasing_subsequence(sequence2) #longest 10
longest_increasing_subsequence(sequence3) #longest 1


