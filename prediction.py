#!/usr/bin/env python3


def single_exponential_smoothing(series, alpha):
    result = [series[0]] # first value is same as series
    for n in range(1, len(series)):
        result.append(alpha * series[n] + (1 - alpha) * result[n-1])

    # Now let's add the prediction
    result.append(alpha * series[n] + (1 - alpha) * result[n])
    return result

    
def double_exponential_smoothing(series, alpha, beta):
    result = [series[0]]
    for n in range(1, len(series)+2):
        if n == 1:
            level, trend = series[0], series[1] - series[0]
        if n >= len(series): # we are forecasting
            value = result[-1]
        else:
            value = series[n]

        last_level, level = level, alpha*value + (1-alpha)*(level+trend)
        trend = beta*(level-last_level) + (1-beta)*trend
        result.append(level+trend)
    return result


series = [3,10,12,13,12,10,12]

alpha = 0.9
beta = 0.9

print("Original series (order %d)" % len(series))
print(series)
print("----------------------")
ses = single_exponential_smoothing(series, alpha)
print("Single Exponential Smoothing (order %d)" % len(ses))
print(ses)
print("----------------------")
des = double_exponential_smoothing(series, alpha, beta)
print("Double Exponential Smoothing (order %d)" % len(des))
print(des)
