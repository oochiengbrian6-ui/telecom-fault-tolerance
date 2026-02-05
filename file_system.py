# Task (c): Distributed File System with Replication
# Simple version

class File:
    def __init__(self, name, owner, content):
        self.name = name
        self.owner = owner
        self.content = content
        self.replicas = []  # list of nodes storing this file
    
    def add_replica(self, node):
        if node not in self.replicas:
            self.replicas.append(node)

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role  # admin, operator, or viewer
    
    def can_write(self):
        return self.role in ["admin", "operator"]
    
    def can_delete(self):
        return self.role == "admin"

class FileSystem:
    def __init__(self):
        self.files = {}  # filename -> File object
        self.users = {}  # username -> User object
        self.nodes = ["Edge1", "Core1", "Cloud1"]  # storage nodes
    
    def add_user(self, name, role):
        self.users[name] = User(name, role)
        print(f"Added user: {name} ({role})")
    
    def create_file(self, filename, content, owner):
        # check if user can write
        if owner not in self.users:
            print(f"Error: User {owner} not found")
            return False
        
        if not self.users[owner].can_write():
            print(f"Error: {owner} cannot write files")
            return False
        
        # create file
        new_file = File(filename, owner, content)
        
        # replicate to 3 nodes
        for node in self.nodes[:3]:
            new_file.add_replica(node)
        
        self.files[filename] = new_file
        print(f"Created: {filename} by {owner}")
        print(f"  Replicas: {', '.join(new_file.replicas)}")
        return True
    
    def read_file(self, filename, username):
        if filename not in self.files:
            print(f"Error: {filename} not found")
            return None
        
        file = self.files[filename]
        print(f"Reading {filename} from {file.replicas[0]}")
        return file.content
    
    def delete_file(self, filename, username):
        if username not in self.users:
            print(f"Error: User {username} not found")
            return False
        
        if not self.users[username].can_delete():
            print(f"Error: {username} cannot delete files")
            return False
        
        if filename in self.files:
            del self.files[filename]
            print(f"Deleted: {filename}")
            return True
        return False
    
    def show_files(self):
        print("\nFiles in system:")
        for name, file in self.files.items():
            print(f"  {name} - owner: {file.owner}, replicas: {len(file.replicas)}")

# test
if __name__ == "__main__":
    print("=== Distributed File System Demo ===\n")
    
    fs = FileSystem()
    
    # add users
    fs.add_user("alice", "admin")
    fs.add_user("bob", "operator")
    fs.add_user("charlie", "viewer")
    
    print()
    
    # create files
    fs.create_file("config.txt", "network settings...", "alice")
    fs.create_file("logs.txt", "system logs...", "bob")
    
    # try operations
    print("\n--- Access Control Test ---")
    fs.create_file("test.txt", "data", "charlie")  # should fail
    fs.delete_file("logs.txt", "bob")  # should fail
    fs.delete_file("config.txt", "alice")  # should work
    
    fs.show_files()
