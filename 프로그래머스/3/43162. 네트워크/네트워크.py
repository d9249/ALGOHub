def solution(n, computers):
    visited = [False] * n
    network_count = 0
    
    for i in range(n):
        if not visited[i]:
            network_count += 1
            
            # DFS를 위한 스택 초기화 (i번 컴퓨터부터 시작)
            stack = [i]
            visited[i] = True
            
            # 스택이 빌 때까지 탐색
            while stack:
                current = stack.pop()
                
                # current 컴퓨터와 연결된 컴퓨터 확인
                for j in range(n):
                    if computers[current][j] == 1 and not visited[j]:
                        visited[j] = True
                        stack.append(j)
    
    return network_count