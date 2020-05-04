#!/usr/bin/env python3

series = [13,43,54,34,40,56,34,61,34,23]

# Percentile we want to compute
percentile = 80

# Sort the data
sorted_series = sorted(series)

# Find the index in the sorted data that corresponds to the searched percentile
index = len(sorted_series)*(percentile/100)

# Round it to the nearest upper integer
rounded_index = int(index + 0.5)

# Find the element that identifies the percentile
pcentile = sorted_series[rounded_index-1]

print(sorted_series)
print("%uth percentile: %u" % (percentile, pcentile))
