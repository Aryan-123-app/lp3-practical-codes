import xml.etree.ElementTree as ET


class DiGraph:
    """Minimal directed graph implementation used by this example."""

    def __init__(self):
        self._out_edges = {}

    def add_node(self, node):
        self._out_edges.setdefault(node, [])

    def add_edge(self, source, target):
        self.add_node(source)
        self.add_node(target)
        if target not in self._out_edges[source]:
            self._out_edges[source].append(target)

    def nodes(self):
        return self._out_edges.keys()

    def edges(self):
        return [
            (source, target)
            for source, targets in self._out_edges.items()
            for target in targets
        ]


def pagerank(graph, alpha=0.85, personalization=None, max_iter=100, tol=1e-6):
    nodes = list(graph.nodes())
    if not nodes:
        return {}

    if personalization is None:
        personalization = {node: 1 / len(nodes) for node in nodes}
    else:
        total = sum(personalization.values())
        personalization = {
            node: personalization.get(node, 0) / total for node in nodes
        }

    scores = {node: 1 / len(nodes) for node in nodes}
    for _ in range(max_iter):
        dangling_mass = sum(
            scores[node] for node in nodes if not graph._out_edges[node]
        )
        updated = {
            node: (1 - alpha + alpha * dangling_mass) * personalization[node]
            for node in nodes
        }

        for source in nodes:
            targets = graph._out_edges[source]
            if targets:
                share = alpha * scores[source] / len(targets)
                for target in targets:
                    updated[target] += share

        if sum(abs(updated[node] - scores[node]) for node in nodes) < len(nodes) * tol:
            return updated
        scores = updated

    return scores

# XML data containing pages, topics, and hyperlinks
xml_data = """
<web>
    <page id="A" topic="AI">
        <link>B</link>
        <link>C</link>
    </page>

    <page id="B" topic="AI">
        <link>C</link>
        <link>D</link>
    </page>

    <page id="C" topic="Sports">
        <link>A</link>
        <link>D</link>
    </page>

    <page id="D" topic="AI">
        <link>A</link>
    </page>
</web>
"""

# 1. Parse XML
root = ET.fromstring(xml_data)

# 2. Generate web graph
G = DiGraph()
page_topics = {}

for page in root.findall("page"):

    page_id = page.get("id")
    topic = page.get("topic")

    G.add_node(page_id)
    page_topics[page_id] = topic

    for link in page.findall("link"):

        target = (link.text or "").strip()
        if target:
            G.add_edge(page_id, target)

print("Web Graph Edges:")
print(list(G.edges()))

# 3. Select the topic
selected_topic = "AI"

# 4. Create topic preference vector
preference = {}

for page in G.nodes():

    if page_topics[page] == selected_topic:
        preference[page] = 1
    else:
        preference[page] = 0

# Normalize preference scores
total = sum(preference.values())

for page in preference:
    preference[page] /= total

# 5. Compute topic-specific PageRank
topic_scores = pagerank(
    G,
    alpha=0.85,
    personalization=preference
)

# 6. Display results
print("\nTopic:", selected_topic)
print("\nTopic-Specific PageRank:")

for page, score in sorted(
    topic_scores.items(),
    key=lambda item: item[1],
    reverse=True
):
    print(page, ":", round(score, 4))