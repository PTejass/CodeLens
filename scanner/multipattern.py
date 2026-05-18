from collections import deque

class AhoCorasick:
    def __init__(self):
        self.transitions = [] 
        self.outputs = []     
        self.fails = []       
        self._add_node() 
        
    def _add_node(self):
        self.transitions.append({})
        self.outputs.append([])
        self.fails.append(0)
        return len(self.transitions) - 1
        
    def add_pattern(self, pattern):
        if not pattern:
            return
        curr = 0
        for char in pattern:
            if char not in self.transitions[curr]:
                node = self._add_node()
                self.transitions[curr][char] = node
            curr = self.transitions[curr][char]
        self.outputs[curr].append(pattern)
        
    def build(self):
        queue = deque()
        for char, node in self.transitions[0].items():
            self.fails[node] = 0
            queue.append(node)
            
        while queue:
            r = queue.popleft()
            for char, child in self.transitions[r].items():
                queue.append(child)
                fail_state = self.fails[r]
                
                while fail_state != 0 and char not in self.transitions[fail_state]:
                    fail_state = self.fails[fail_state]
                    
                self.fails[child] = self.transitions[fail_state].get(char, 0)
                self.outputs[child].extend(self.outputs[self.fails[child]])

    def search(self, text):
        results = {}
        curr = 0
        for i, char in enumerate(text):
            while curr != 0 and char not in self.transitions[curr]:
                curr = self.fails[curr]
            
            curr = self.transitions[curr].get(char, 0)
            
            for pattern in self.outputs[curr]:
                if pattern not in results:
                    results[pattern] = []
                start_idx = i - len(pattern) + 1
                results[pattern].append(start_idx)
                
        return results

def search_multiple(text, patterns):
    """
    Aho-Corasick multi-pattern matching implementation.
    Returns a dictionary mapping pattern -> list of starting indices.
    """
    results = {p: [] for p in patterns}
    
    if not patterns:
        return results
        
    ac = AhoCorasick()
    for p in patterns:
        ac.add_pattern(p)
        
    ac.build()
    
    matches = ac.search(text)
    for p, indices in matches.items():
        results[p].extend(indices)
        
    return results
