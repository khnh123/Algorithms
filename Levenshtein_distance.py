
def distance_1(a, b):
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

def distance_2(a, b):
    # https://ru.wikibooks.org/wiki/Реализации_алгоритмов/Расстояние_Левенштейна#Scala
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n, m)) space
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)  # Keep current and previous row, not entire matrix
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]

str1 = 'Hello World'
str2 = 'Hel Wld'

lev = dist(str1, str2)
bigger = max([len(str1), len(str2)])
pct = ((bigger - lev) / bigger) *100

print('distance: ' + str(lev))
print('string #1 : {str1}\nString #2 : {str2}\n===\nSimilarity : {pct}%'.format(str1=str1, str2=str2, pct=pct))
