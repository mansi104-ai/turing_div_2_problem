def solve():
    import sys
    from itertools import combinations
    
    n = int(input())
    if n == 1:
        w = int(input())
        print(w)
        return
        
    weights = list(map(int, input().split()))
    
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1  # Convert to 0-indexed
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    # dp[mask] = minimum cost to merge all nodes in the mask into one component
    dp = [float('inf')] * (1 << n)
    
    # Initialize single nodes
    for i in range(n):
        dp[1 << i] = 0  # Cost to have a single node by itself is 0
    
    # For each subset size
    for mask in range(1, 1 << n):
        if bin(mask).count('1') == 1:
            continue  # Already handled single nodes
            
        # Find connected components in current mask
        visited = [False] * n
        components = []
        
        for i in range(n):
            if mask & (1 << i) and not visited[i]:
                # BFS to find connected component
                comp = []
                queue = [i]
                visited[i] = True
                
                while queue:
                    node = queue.pop(0)
                    comp.append(node)
                    
                    for neighbor in adj[node]:
                        if (mask & (1 << neighbor)) and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                components.append(comp)
        
        # If the current mask is connected, calculate its total weight
        if len(components) == 1:
            total_weight = sum(weights[i] for i in components[0])
            
            # Try all possible ways to merge two sub-components
            submask = mask
            while submask > 0:
                submask = (submask - 1) & mask
                if submask == 0:
                    continue
                
                # Check if both submask and (mask ^ submask) are connected
                # and there's an edge between them
                comp1_mask = submask
                comp2_mask = mask ^ submask
                
                if dp[comp1_mask] != float('inf') and dp[comp2_mask] != float('inf'):
                    # Check connectivity within each component
                    visited1 = [False] * n
                    visited2 = [False] * n
                    connected1 = True
                    connected2 = True
                    
                    # Check if comp1_mask is connected
                    nodes1 = [i for i in range(n) if comp1_mask & (1 << i)]
                    if len(nodes1) > 1:
                        queue = [nodes1[0]]
                        visited1[nodes1[0]] = True
                        count1 = 1
                        while queue:
                            node = queue.pop(0)
                            for neighbor in adj[node]:
                                if (comp1_mask & (1 << neighbor)) and not visited1[neighbor]:
                                    visited1[neighbor] = True
                                    queue.append(neighbor)
                                    count1 += 1
                        connected1 = (count1 == len(nodes1))
                    
                    # Check if comp2_mask is connected
                    nodes2 = [i for i in range(n) if comp2_mask & (1 << i)]
                    if len(nodes2) > 1:
                        queue = [nodes2[0]]
                        visited2[nodes2[0]] = True
                        count2 = 1
                        while queue:
                            node = queue.pop(0)
                            for neighbor in adj[node]:
                                if (comp2_mask & (1 << neighbor)) and not visited2[neighbor]:
                                    visited2[neighbor] = True
                                    queue.append(neighbor)
                                    count2 += 1
                        connected2 = (count2 == len(nodes2))
                    
                    if connected1 and connected2:
                        # Check if there's an edge between the two components
                        has_edge = False
                        for i in range(n):
                            if comp1_mask & (1 << i):
                                for neighbor in adj[i]:
                                    if comp2_mask & (1 << neighbor):
                                        has_edge = True
                                        break
                                if has_edge:
                                    break
                        
                        if has_edge:
                            # Cost to merge these two components
                            comp1_weight = sum(weights[j] for j in range(n) if comp1_mask & (1 << j))
                            comp2_weight = sum(weights[j] for j in range(n) if comp2_mask & (1 << j))
                            merge_cost = dp[comp1_mask] + dp[comp2_mask] + comp1_weight + comp2_weight
                            dp[mask] = min(dp[mask], merge_cost)
    
    result = dp[(1 << n) - 1]
    print(result)

solve()

'''

Answer received :

5
20
33
30
133
42
'''