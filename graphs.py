class graph:
    def __init__(self, edges):
        self.edges = edges
        self.dict = {}
        for start, end in self.edges:
            if start in self.dict:
                self.dict[start].append(end)
            else:
                self.dict[start] = [end]
        print("Graph dict:", self.dict)

    def get_paths(self, start, end, path=None):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.dict:
            return []
        paths = []
        for node in self.dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

    def get_shortest_path(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if start not in self.dict:
            return None
        shortest_path = None
        for node in self.dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp:
                    if shortest_path is None or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path


if __name__ == "__main__":
    routes = [
        ("Mumbai", "paris")
        , ("Mumbai", "dubai")
        , ("paris", "dubai")
        , ("paris", "new york")
        , ("dubai", "new york")
        , ("new york", "toronto")
    ]
    route_graph = graph(routes)
    start = "Mumbai"
    end = "new york"
    print(f"paths {start} and {end}", route_graph.get_shortest_path(start, end))
