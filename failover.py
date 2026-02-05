# Task (b): Simple Redundancy and Failover
# Student implementation

import time

class Node:
    def __init__(self, name, is_backup=False):
        self.name = name
        self.is_backup = is_backup
        self.alive = True
        self.last_check = time.time()
    
    def check_health(self):
        # simulate checking if node is alive
        current = time.time()
        if current - self.last_check > 5:  # 5 sec timeout
            self.alive = False
            return False
        return True

class FailoverSystem:
    def __init__(self):
        self.nodes = {}
        self.backups = {}
    
    def add_node(self, name, backup_name=None):
        # add primary node
        self.nodes[name] = Node(name)
        print(f"Added node: {name}")
        
        # add backup if provided
        if backup_name:
            self.backups[name] = Node(backup_name, is_backup=True)
            print(f"  Backup: {backup_name}")
    
    def check_all_nodes(self):
        print("\nChecking nodes...")
        for name, node in self.nodes.items():
            if not node.check_health():
                print(f"FAILED: {name}")
                self.do_failover(name)
            else:
                print(f"OK: {name}")
    
    def do_failover(self, failed_node):
        # switch to backup
        if failed_node in self.backups:
            backup = self.backups[failed_node]
            print(f">>> FAILOVER: {backup.name} taking over for {failed_node}")
            backup.alive = True
        else:
            print(f">>> ERROR: No backup for {failed_node}!")

# test the system
if __name__ == "__main__":
    print("=== Failover System Demo ===\n")
    
    system = FailoverSystem()
    
    # setup from dataset
    system.add_node("Edge1", "Edge1_Backup")
    system.add_node("Core1", "Core1_Backup")
    system.add_node("Cloud1", "Cloud1_Backup")
    system.add_node("Edge2")  # no backup
    
    # check health
    system.check_all_nodes()
    
    # simulate failure
    print("\n--- Simulating Core1 failure ---")
    system.nodes["Core1"].alive = False
    system.check_all_nodes()
