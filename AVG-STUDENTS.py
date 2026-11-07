names = {
    1: "Ali",
    2: "karem",
    
}

scores = {
    "Ali": [19,18],
    "karem": [10],
    
}  

def calculate_average(names, scores):
    result = {}

    for name in names:
        average = sum(scores[name]) / len(scores[name])
        result[name] = average

    return result




print(calculate_average(scores, scores))
