import networkx as nx
import matplotlib.pyplot as plt
from GBFS_implementation.classes.gbfs import GBfsTraverser
G = nx.Graph()
nodes=["SportsComplex","Siwaka","Ph.1A","Ph.1B","Phase2","J1","Mada","STC","Phase3","ParkingLot"]
G.add_nodes_from(nodes)
G.nodes()
H_table = {
    'SportsComplex': 730,
    'Siwaka': 405,
    'Phase1Ent.A': 380,
    'Phase1Ent.B': 280,
    'STC': 213,
    'Phase2': 210,
    'J1': 500,
    'Phase3': 160,
    'Mada': 630,
    'ParkingLot': 0
}

G.add_edge("SportsComplex","Siwaka",weight="405")
G.add_edge("Siwaka","Ph.1A",weight="10")
G.add_edge("Siwaka","Ph.1B",weight="230")
G.add_edge("Ph.1A","Mada",weight="850")
G.add_edge("Ph.1A","Ph.1B",weight="100")
G.add_edge("Ph.1B","Phase2",weight="112")
G.add_edge("Ph.1B","STC",weight="50")
G.add_edge("Phase2","J1",weight="600")
G.add_edge("J1","Mada",weight="200")
G.add_edge("STC","Phase2",weight="50")
G.add_edge("STC","ParkingLot",weight="250")
G.add_edge("Phase2","Phase3",weight="500")
G.add_edge("Phase3","ParkingLot",weight="350")
G.add_edge("Mada","ParkingLot",weight="700")

G.nodes["SportsComplex"]['pos']=(-4,4)
G.nodes["Siwaka"]['pos']=(-2,4)
G.nodes["Ph.1A"]['pos']=(0,4)
G.nodes["Ph.1B"]['pos']=(0,2)
G.nodes["STC"]['pos']=(0,0)
G.nodes["Phase2"]['pos']=(2,2)
G.nodes["J1"]['pos']=(4,2)
G.nodes["Mada"]['pos']=(6,2)
G.nodes["Phase3"]['pos']=(4,0)
G.nodes["ParkingLot"]['pos']=(4,-2)

H_table = {
    'SportsComplex': 730,
    'Siwaka': 405,
    'Phase1Ent.A': 380,
    'Phase1Ent.B': 280,
    'STC': 213,
    'Phase2': 210,
    'J1': 500,
    'Phase3': 160,
    'Mada': 630,
    'ParkingLot': 0
}
node_pos = nx.get_node_attributes(G,'pos')

arc_weight=nx.get_edge_attributes(G,'weight')
nx.draw_networkx(G, node_pos, node_size=450)
nx.draw_networkx_edges(G, node_pos,width=2)

nx.draw_networkx_edge_labels(G, node_pos, edge_labels=arc_weight)
plt.axis('off')
plt.show()
