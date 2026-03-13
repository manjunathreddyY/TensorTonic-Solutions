def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    l = len(values)
    min_value = min(values)
    max_value = max(values)
    res = [0] * l
    w = (max_value - min_value) / num_bins
    if l == values.count(values[0]):
        return res
    else:
        for i,x in enumerate(values):
            res[i] = (x - min_value) // w
            if x == max_value:
                res[i] = num_bins - 1
        return res
            