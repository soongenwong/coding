def getMinimumOperations(versionNumbers):
    operations = 0
    n = len(versionNumbers)
    
    for i in range(1, n):
        if versionNumbers[i] <= versionNumbers[i - 1]:
            needed = versionNumbers[i - 1] - versionNumbers[i] + 1
            increment_value = i + 1  # Convert 0-based to 1-based position
            times = (needed + increment_value - 1) // increment_value
            versionNumbers[i] += times * increment_value
            operations += times
    
    return operations