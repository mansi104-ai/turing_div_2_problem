def solve():
    n = int(input())
    if n == 1:
        w = int(input())
        print(0)
        return
    weights = list(map(int, input().split()))
    
    adj = [[] for _ in range(n)]
    for _ in range(n-1):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    
    # dp[mask] = minimum cost to merge all nodes in mask into one connected component
    dp = [float('inf')] * (1 << n)
    total_weight = [0] * (1 << n)
    
    # Calculate total weight for each mask
    for mask in range(1 << n):
        total_weight[mask] = sum(weights[i] for i in range(n) if mask & (1 << i))
    
    # Initialize single nodes
    for i in range(n):
        dp[1 << i] = 0
    
    # Process all possible masks in increasing order of number of bits
    for mask in range(1, 1 << n):
        if bin(mask).count('1') == 1:
            continue
        
        # Check if current mask forms a connected component
        nodes = [i for i in range(n) if mask & (1 << i)]
        visited = set()
        queue = [nodes[0]]
        visited.add(nodes[0])
        
        while queue:
            u = queue.pop(0)
            for v in adj[u]:
                if v in nodes and v not in visited:
                    visited.add(v)
                    queue.append(v)
        
        if len(visited) == len(nodes):  # Connected
            # Try all possible ways to split mask into two connected submasks that can be merged
            submask = (mask - 1) & mask
            while submask > 0:
                other = mask ^ submask
                if submask != 0 and other != 0:
                    # Check if both submasks are connected
                    nodes1 = [i for i in range(n) if submask & (1 << i)]
                    nodes2 = [i for i in range(n) if other & (1 << i)]
                    
                    # Check connectivity of submask
                    conn1 = True
                    if len(nodes1) > 1:
                        vis1 = set()
                        q1 = [nodes1[0]]
                        vis1.add(nodes1[0])
                        while q1:
                            u = q1.pop(0)
                            for v in adj[u]:
                                if v in nodes1 and v not in vis1:
                                    vis1.add(v)
                                    q1.append(v)
                        if len(vis1) != len(nodes1):
                            conn1 = False
                    
                    # Check connectivity of other
                    conn2 = True
                    if len(nodes2) > 1:
                        vis2 = set()
                        q2 = [nodes2[0]]
                        vis2.add(nodes2[0])
                        while q2:
                            u = q2.pop(0)
                            for v in adj[u]:
                                if v in nodes2 and v not in vis2:
                                    vis2.add(v)
                                    q2.append(v)
                        if len(vis2) != len(nodes2):
                            conn2 = False
                    
                    if conn1 and conn2:
                        # Check if there's an edge between the two components
                        has_edge = False
                        for u in nodes1:
                            for v in adj[u]:
                                if v in nodes2:
                                    has_edge = True
                                    break
                            if has_edge:
                                break
                        
                        if has_edge:
                            cost = dp[submask] + dp[other] + total_weight[submask] + total_weight[other]
                            dp[mask] = min(dp[mask], cost)
                
                submask = (submask - 1) & mask
    
    print(dp[(1 << n) - 1])

solve()

'''

Answer received :

5
20
23
30
133
0
'''