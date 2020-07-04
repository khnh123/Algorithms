
def dist(a, b):
    def rec(i, j):
        if i == 0 or j == 0:
            # if string is empty : dist = length of the string
            return max(i, j)
        elif a[i - 1] == b[j - 1]:
            # if last symbols are equal : remove them
            return rec(i - 1, j - 1)
        else:
            #
            return 1 + min(
                rec(i, j - 1),  # remove symbol
                rec(i - 1, j),  # insert symbol
                rec(i - 1, j - 1)  # replace symbol
            )

    return rec(len(a), len(b))

str1 = 'Hello World'
str2 = 'Hel Wld'

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) *100

print('distance: ' + str(lev))
print('string #1 : {str1}\nString #2 : {str2}\n===\nSimilarity : {pct}%'.format(str1=str1, str2=str2, pct=pct))
