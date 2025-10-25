def loadBalancing(k, arrival, load):
    # Write your code here
    
    if k == 0:
        return []
        
    requests = sorted(zip(arrival, load))
    
    server_free_at = [0] * k
    server_loads = [0] * k
    
    round_robin_idx = 0
    
    for arrival_time, load_time in requests:
        request_assigned = False
        
        for i in range(k):
            server_to_check = (round_robin_idx + i) % k
            
            if server_free_at[server_to_check] <= arrival_time:
                server_free_at[server_to_check] = arrival_time + load_time
                server_loads[server_to_check] += load_time
                
                round_robin_idx = (server_to_check + 1) % k
                request_assigned = True
                break
            
    if not any(server_loads):
        max_load = 0
    else:
        max_load = max(server_loads)
        
    busiest_servers = []
    for i in range(k):
        if server_loads[i] == max_load:
            busiest_servers.append(i+1)
    
    return busiest_servers