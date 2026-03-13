def binning(values, num_bins):
    """
    Assign each value to an equal-width bin.
    """
    # Write code here
    l = len(values)
    res = [0] * l
    w = (max(values) - min(values)) / num_bins
    if l == values.count(values[0]):
        return res
    else:
        for i,x in enumerate(values):
            res[i] = (x - min(values)) // w
            if x == max(values):
                res[i] = num_bins - 1
        return res
            