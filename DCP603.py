# Easy

# This problem was asked by Microsoft.

# You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:

#     L, meaning the domino has just been pushed to the left,
#     R, meaning the domino has just been pushed to the right, or
#     ., meaning the domino is standing still.

# Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.

# For example, given the string .L.R....L, you should return LL.RRRLLL.

# Given the string ..R...L.L, you should return ..RR.LLLL.

def dominoFall(initialCondition):
    initialCondition = list(initialCondition)
    print(initialCondition)
    start = 0
    end = 1
    checkPoint = end
    while start < len(initialCondition):
        while end < len(initialCondition) and initialCondition[end] == '.':
            end += 1    
        if end >= len(initialCondition):
            if initialCondition[start] == 'r':
                while start < len(initialCondition):
                    initialCondition[start] = 'r'
                    start += 1
            else:
                start = len(initialCondition) 
        else:    
            while start < end:
                if initialCondition[start] == 'r' and initialCondition[end] == 'r':
                    initialCondition[start+1] = 'r'
                    start += 1
                elif initialCondition[start] == 'r' and initialCondition[end] == 'l':
                    checkPoint = end
                    while start < end:
                        if initialCondition[start+1] == '.':
                            initialCondition[start+1] = 'r'
                        else:
                            initialCondition[start+1] = '.'
                            break
                        start += 1

                        if initialCondition[end-1] == '.':
                            initialCondition[end-1] = 'l'
                        else:
                            initialCondition[end-1] = '.'
                            break
                        end -= 1
                    start = checkPoint
                    end = checkPoint

                elif initialCondition[start] == 'l' and initialCondition[end] == 'l':
                    initialCondition[start+1] = 'l'
                    start += 1
                elif initialCondition[start] == 'l' and initialCondition[end] == 'r':
                    start = end
                elif initialCondition[start] == '.' and initialCondition[end] == 'l':
                    initialCondition[start] = 'l'
                    start += 1
                elif initialCondition[start] == '.' and initialCondition[end] == 'r':
                    start = end
        end += 1
    return initialCondition
print(dominoFall('..r...l.l'))