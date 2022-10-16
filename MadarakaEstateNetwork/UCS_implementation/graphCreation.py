import networkx as nx
import matplotlib.pyplot as plt
import json

def show_weighted_graph(networkx_graph, node_size, font_size, fig_size):
  plt.figure(num=None, figsize=fig_size, dpi=80)
  plt.axis('off')
  nodes = ["SportsComplex", "Siwaka", "Ph.1A", "Ph.1B", "Phase2", "J1", "Mada", "STC", "Phase3", "ParkingLot"]

  nodes_position = nx.spring_layout(networkx_graph)

  edges_weights  = nx.get_edge_attributes(networkx_graph,'weight')

  nx.draw_networkx_nodes(networkx_graph, nodes_position, node_size=node_size,
                         node_color = ["grey"]*networkx_graph.number_of_nodes())
  nx.draw_networkx_edges(networkx_graph, nodes_position, edgelist=list(networkx_graph.edges), width=2)
  nx.draw_networkx_edge_labels(networkx_graph, nodes_position, edge_labels = edges_weights)
  nx.draw_networkx_labels(networkx_graph, nodes_position, font_size=font_size,
                          font_family='sans-serif')
  plt.axis('off')
  plt.show()



def load_graph_from_file(filename):
	with open(filename) as nodes:
		dict_cities = json.load(nodes)
		return nx.Graph(dict_cities)

