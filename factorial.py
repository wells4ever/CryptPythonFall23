#iteration
def fact1(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, n + 1):
            f = f * i
        return f
#head recursion
def fact2(n):
    if n == 0:
        return 1
    else:
        return n * fact2(n-1)

#tail recursion
def fact3(n):
    def helperFact(n, ans):
        if n == 0:
            return ans
        else:
            return helperFact(n - 1 , n * ans)
    return helperFact(n, 1)

if __name__ == "__main__":
    print(fact1(5))
    print(fact2(5))
    print(fact3(5))
    
    
