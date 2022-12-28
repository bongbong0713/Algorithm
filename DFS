answer=0
def DFS(numbers, target, value):
    global answer
    if numbers:
        DFS(numbers[1:], target, value+numbers[0])
        DFS(numbers[1:], target, value-numbers[0])
    elif not numbers:
        if value == target:
            answer+=1
            return
        else:
            return 
        
def solution(numbers, target):
    global answer
    DFS(numbers, target, 0)
    return answer
