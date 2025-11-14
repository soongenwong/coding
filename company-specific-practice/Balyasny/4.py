def findBreakDuration(n, k, t, start, finish):
    if n == 0:
        return t
    
    if k >= n:
        return t
    
    # Calculate all gaps
    gaps = [start[0]]  # Gap before first meeting
    
    for i in range(n - 1):
        gaps.append(start[i + 1] - finish[i])
    
    gaps.append(t - finish[n - 1])  # Gap after last meeting
    
    max_break = 0
    
    # Merge k+1 consecutive gaps by removing k meetings between them
    for i in range(len(gaps) - k):
        total_gap = sum(gaps[i:i + k + 1])
        max_break = max(max_break, total_gap)
    
    return max_break