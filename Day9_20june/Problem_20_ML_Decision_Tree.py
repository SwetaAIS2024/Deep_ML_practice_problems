import torch
import torch.nn as nn
import torch.nn.functional as F

class DecisionTreeNode:
    def __init__(self, is_leaf=False, prediction=None, feature_index=None, threshold=None, left=None, right=None):
        self.is_leaf = is_leaf
        self.prediction = prediction
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right

class DecisionTreeClassifier(nn.Module):
    def __init__(self, max_depth=None, min_samples_split=2):
        super().__init__()
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        self.n_classes_ = len(torch.unique(y))
        self.root = self._build_tree(X, y, depth=0)

    def _entropy(self, y):
        hist = torch.bincount(y)
        ps = hist.float() / y.size(0)
        ps = ps[ps > 0]
        return -torch.sum(ps * torch.log2(ps))

    def _best_split(self, X, y):
        m, n = X.shape
        best_gain = 0
        best_idx, best_thr = None, None
        parent_entropy = self._entropy(y)
        for idx in range(n):
            thresholds, indices = torch.sort(X[:, idx])
            y_sorted = y[indices]
            for i in range(1, m):
                if thresholds[i] == thresholds[i-1]:
                    continue
                left, right = y_sorted[:i], y_sorted[i:]
                if len(left) == 0 or len(right) == 0:
                    continue
                left_entropy = self._entropy(left)
                right_entropy = self._entropy(right)
                gain = parent_entropy - (len(left)/m)*left_entropy - (len(right)/m)*right_entropy
                if gain > best_gain:
                    best_gain = gain
                    best_idx = idx
                    best_thr = (thresholds[i] + thresholds[i-1]) / 2
        return best_idx, best_thr

    def _build_tree(self, X, y, depth):
        if len(torch.unique(y)) == 1:
            return DecisionTreeNode(is_leaf=True, prediction=int(y[0].item()))
        if self.max_depth is not None and depth >= self.max_depth:
            values, counts = torch.unique(y, return_counts=True)
            prediction = int(values[torch.argmax(counts)].item())
            return DecisionTreeNode(is_leaf=True, prediction=prediction)
        if X.size(0) < self.min_samples_split:
            values, counts = torch.unique(y, return_counts=True)
            prediction = int(values[torch.argmax(counts)].item())
            return DecisionTreeNode(is_leaf=True, prediction=prediction)
        idx, thr = self._best_split(X, y)
        if idx is None:
            values, counts = torch.unique(y, return_counts=True)
            prediction = int(values[torch.argmax(counts)].item())
            return DecisionTreeNode(is_leaf=True, prediction=prediction)
        left_mask = X[:, idx] <= thr
        right_mask = X[:, idx] > thr
        left = self._build_tree(X[left_mask], y[left_mask], depth+1)
        right = self._build_tree(X[right_mask], y[right_mask], depth+1)
        return DecisionTreeNode(is_leaf=False, feature_index=idx, threshold=thr.item(), left=left, right=right)

    def predict_one(self, x):
        node = self.root
        while not node.is_leaf:
            if x[node.feature_index] <= node.threshold:
                node = node.left
            else:
                node = node.right
        return node.prediction

    def predict(self, X):
        return torch.tensor([self.predict_one(x) for x in X])

# Example usage:
if __name__ == "__main__":
    # Example: XOR problem
    X = torch.tensor([[0,0],[0,1],[1,0],[1,1]], dtype=torch.float32)
    y = torch.tensor([0,1,1,0], dtype=torch.long)
    clf = DecisionTreeClassifier(max_depth=2)
    clf.fit(X, y)
    preds = clf.predict(X)
    print("Predictions:", preds.tolist())
