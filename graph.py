# Graph
# Uses python3

class Graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdict = []
		self.gdict = gdict	
		
	def getVertices(self):
		return list(self.gdict.keys())
	
	def getEdges(self):
		return self.findedges()
		
	def findedges(self):
		edgename = []
		for vrtx in self.gdict:
			for nxtvrtx in self.gdict[vrtx]:
				print(nxtvrtx, vrtx)
				if {nxtvrtx, vrtx} not in edgename:
					print("Introducimos")
					edgename.append({vrtx, nxtvrtx})
		return edgename		

	def addVertex(self,vrtx):
		if vrtx not in self.gdict:
			self.gdict[vrtx] = []
		
		
graph_elements = {"a": ["b","c"],
		"b": ["a","d"],
		"c": ["a","d"],
		"d":["e"],
		"e":["d"],		
		}	

# Example of usage
if __name__ == "__main__":				
	g = Graph(graph_elements)

	print(g.getVertices())

	g.addVertex("f")

	print(g.getEdges())