def loadBalancing(k, arrival, load):
    """
    Determines which server(s) did the most work based on a round-robin
    load balancing scheme.

    This implementation is a direct simulation with O(N*K) time complexity,
    making it simple but potentially slow for the largest constraints.

    Args:
        k: The number of web servers.
        arrival: A list of arrival times for each request.
        load: A list of the load of each corresponding request.

    Returns:
        A sorted list of integers denoting the IDs of the servers that
        did the most work.
    """
    if k == 0:
        return []

    # Combine requests and sort them by arrival time.
    requests = sorted(zip(arrival, load))
    
    # Track when each server will be free and its total accumulated load.
    server_free_at = [0] * k
    server_loads = [0] * k
    
    # This index determines where the round-robin search starts for the next request.
    round_robin_idx = 0

    for arrival_time, load_time in requests:
        request_assigned = False
        # Search for an available server, checking each one at most once.
        for i in range(k):
            # Calculate the actual server index to check, starting from round_robin_idx.
            server_to_check = (round_robin_idx + i) % k
            
            # Check if this server is available.
            if server_free_at[server_to_check] <= arrival_time:
                # Assign the request to this server.
                server_free_at[server_to_check] = arrival_time + load_time
                server_loads[server_to_check] += load_time
                
                # The next search will start from the server after this one.
                round_robin_idx = (server_to_check + 1) % k
                request_assigned = True
                break  # Stop searching for a server for this request.
        
        # If no server was found after checking all k, the request is dropped.
        # The round_robin_idx remains unchanged in this case.

    # Find the maximum load after all requests have been processed.
    if not any(server_loads):
        max_load = 0
    else:
        max_load = max(server_loads)

    # Collect all servers that have the maximum load.
    busiest_servers = []
    for i in range(k):
        if server_loads[i] == max_load:
            busiest_servers.append(i + 1) # Append 1-based server ID.
            
    return busiest_servers