class CustomDataset:
    def __init__(self, X, y):
        self.X = X
        self.y = y
    
    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# Example
X = [1,2,3,4]
y = [10,20,30,40]
dataset = CustomDataset(X, y)

print(len(dataset))      # 4
print(dataset[2])        # (3, 30)
