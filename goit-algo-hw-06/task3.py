import networkx as nx
from task1 import G

start = "Vörösmarty tér"
end = "Keleti pályaudvar"

dijkstra_path = nx.dijkstra_path(G, source=start, target=end, weight='weight')
dijkstra_time = nx.dijkstra_path_length(G, source=start, target=end, weight='weight')

print(f"Найшвидший маршрут від {start} до {end}:")
print(f"Маршрут: {dijkstra_path}")
print(f"Час у дорозі: {dijkstra_time} хв")