import networkx as nx

def build_skill_graph(skills, projects):
    G = nx.Graph()

    for skill in skills:
        G.add_node(skill)

    for project in projects:
        for skill in project["skills"]:
            G.add_edge(project["name"], skill)

    return G
