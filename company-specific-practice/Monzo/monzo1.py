import collections
import bisect

def getRequestStatus(requests):
    # Write your code here(
    domain_timestamps = collections.defaultdict(list)
    
    ok_message = "{status: 200, message: OK}"
    limit_message = "{status: 429, message: Too many requests}"
    
    
    results = []
    
    for i, domain in enumerate(requests):
        ts_list = domain_timestamps[domain]
        
        cutoff_30 = i - 30
        start_index_30 = bisect.bisect_right(ts_list, cutoff_30)
        
        ts_list = ts_list[start_index_30:]
        
        if len(ts_list) >= 5:
            results.append(limit_message)
            domain_timestamps[domain] = ts_list
            continue
            
        cutoff_5 = i - 5
        start_index_5 = bisect.bisect_right(ts_list, cutoff_5)
        count5 = len(ts_list) - start_index_5
        
        if count5 >= 2:
            results.append(limit_message)
            domain_timestamps[domain] = ts_list
            continue
        
        results.append(ok_message)
        ts_list.append(i)
        domain_timestamps[domain] = ts_list
    
    return results