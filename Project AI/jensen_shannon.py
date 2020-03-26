import math


def js_divergence(prob, qn):
    sum1 = 0
    sum2 = 0
    for i in range(len(prob)):
        sum1 += prob[i] * math.log((prob[i]) / (0.5 * (prob[i] + qn[i])))
        sum2 += qn[i] * math.log((qn[i] / (0.5 * (prob[i] + qn[i]))))
    js = sum1 + sum2
    return js
