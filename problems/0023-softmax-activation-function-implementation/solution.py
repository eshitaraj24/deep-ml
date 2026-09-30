import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    exps = []
    max_val = max(scores)
    for x in scores:
        new_x = x - max_val
        exps.append(math.exp(new_x))
    
    total = sum(exps)

    result = []
    for x in exps:
        result.append(round((x/total),4))
    
    return result

