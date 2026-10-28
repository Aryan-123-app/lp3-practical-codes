# PageRank Algorithm

def page_rank(graph, damping=0.85, iterations=100):

    n = len(graph)

    # Initial PageRank
    rank = [1 / n] * n

    for _ in range(iterations):

        new_rank = [(1 - damping) / n] * n

        for i in range(n):

            # Number of outgoing links
            outgoing = sum(graph[i])

            if outgoing == 0:
                continue

            for j in range(n):

                if graph[i][j] == 1:
                    new_rank[j] += damping * rank[i] / outgoing

        rank = new_rank

    return rank


# Example graph
# 0 -> 1, 2
# 1 -> 2
# 2 -> 0, 3
# 3 -> 0

graph = [
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0]
]

ranks = page_rank(graph)

print("PageRank Values:")

for i in range(len(ranks)):
    print("Page", i + 1, ":", round(ranks[i], 6))

# Display ranking
ranking = sorted(
    range(len(ranks)),
    key=lambda x: ranks[x],
    reverse=True
)

print("\nPage Ranking:")

for position, page in enumerate(ranking, 1):
    print(position, "-> Page", page + 1)