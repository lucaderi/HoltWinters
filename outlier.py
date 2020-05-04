#!/usr/bin/env python3

import math

def calc_percentile(sorted_series, percentile):
    # Find the index in the sorted data that corresponds to the searched percentile
    index = int(len(sorted_series)*(percentile/100))
    
    # Find the element that identifies the percentile
    # as in prediction.py
    return((sorted_series[index-1] + sorted_series[index]) / 2)

def mean(series):
    return int(sum(series)/len(series))
    

def stddev(series, m):
    variance = 0
    
    for v in series:
        variance += (m-v)**2
        
    return math.sqrt(variance / len(series))
    
############

series = [ 0, 0, 0, 0, 6, 2, 0, 0, 0, 0, 0, 12, 0, 0, 33182, 51945 ]
#series = [ 4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 11 ]

# Sort the data
sorted_series = sorted(series)

print("Original series:")
print(sorted_series)

print("")

q1 = calc_percentile(sorted_series, 25)
q2 = calc_percentile(sorted_series, 50)
q3 = calc_percentile(sorted_series, 75)

iqr = q3-q1

print("Percentiles:     q1=%.1f, q2=%.1f, q3=%.1f" % (q1, q2, q3))
print("IQR:             %.1f" % iqr)

k = 1.5
lower_outlier_limit = q1-k*iqr
upper_outlier_limit = q3+k*iqr

# Compute the mean
m = mean(series)

# Compute the standard deviation
std = stddev(series, m)

print("Mean +/- Stddev  [ %.1f ... %.1f ]" % ((m-std), (m+std)))
print("Outlier Formula: [ %.1f ... %.1f ]" % (lower_outlier_limit, upper_outlier_limit))
