def main():

    lowerbound = 367479
    upperbound = 893698
    validpwds = 0

    for i in range(lowerbound, upperbound):

        if repeated(str(i)):
            ascending = "".join(sorted(str(i)))
            if int(ascending) == int(i):
                validpwds = validpwds + 1

    print(validpwds)

def repeated (s):
    if len(s) == len(set(s)): return False #--all letters are unique
    for k, c in enumerate(s[:-1]):
        if k <= 3:
            if c == s[k+1] and c != s[k+2] and s[k-1] != c: return True
        else:
            if c == s[k + 1] and c != s[k-1]: return True
    return False

if __name__ == '__main__':
    main()