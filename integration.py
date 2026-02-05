# Task (d): Edge-Core-Cloud Integration
# Simple version

class ServiceNode:
    def __init__(self, name, tier, latency):
        self.name = name
        self.tier = tier  # edge, core, or cloud
        self.latency = latency
        self.requests = 0
    
    def process_request(self, request):
        self.requests += 1
        print(f"  {self.name} processing: {request}")
        return self.latency

class IntegratedSystem:
    def __init__(self):
        self.edge_nodes = []
        self.core_nodes = []
        self.cloud_nodes = []
    
    def add_node(self, node):
        if node.tier == "edge":
            self.edge_nodes.append(node)
        elif node.tier == "core":
            self.core_nodes.append(node)
        else:
            self.cloud_nodes.append(node)
        print(f"Added {node.tier} node: {node.name}")
    
    def route_request(self, request, priority):
        # simple routing: low latency requests go to edge
        print(f"\nRequest: {request} (priority: {priority})")
        
        if priority == "critical":
            # use edge for fast response
            if self.edge_nodes:
                node = self.edge_nodes[0]
                latency = node.process_request(request)
                print(f"  Latency: {latency}ms")
                return
        
        # normal requests go through core
        if self.core_nodes:
            node = self.core_nodes[0]
            latency = node.process_request(request)
            print(f"  Latency: {latency}ms")
        else:
            print("  Error: No core nodes available")
    
    def show_stats(self):
        print("\n=== System Statistics ===")
        print("Edge tier:")
        for node in self.edge_nodes:
            print(f"  {node.name}: {node.requests} requests")
        print("Core tier:")
        for node in self.core_nodes:
            print(f"  {node.name}: {node.requests} requests")
        print("Cloud tier:")
        for node in self.cloud_nodes:
            print(f"  {node.name}: {node.requests} requests")

# test
if __name__ == "__main__":
    print("=== Edge-Core-Cloud Integration Demo ===\n")
    
    system = IntegratedSystem()
    
    # add nodes from dataset
    system.add_node(ServiceNode("Edge1", "edge", 12))
    system.add_node(ServiceNode("Edge2", "edge", 15))
    system.add_node(ServiceNode("Core1", "core", 8))
    system.add_node(ServiceNode("Core2", "core", 10))
    system.add_node(ServiceNode("Cloud1", "cloud", 22))
    
    # test requests
    system.route_request("User login", "critical")
    system.route_request("Data sync", "normal")
    system.route_request("Analytics job", "normal")
    
    system.show_stats()
