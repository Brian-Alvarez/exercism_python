def latest(scores):
    a = scores.pop()
    return a


def personal_best(scores):
    scores.sort()
    a = scores.pop()
    return a


def personal_top_three(scores):
        scores.sort()
        scores.reverse()
        a = scores[:3]
        return a

