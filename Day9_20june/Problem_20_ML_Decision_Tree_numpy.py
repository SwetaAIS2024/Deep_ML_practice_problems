import numpy as np
from collections import Counter

def entropy(y):
    counts = np.bincount(y)
    ps = counts[counts > 0] / len(y)
    return -np.sum(ps * np.log2(ps))

def best_split(X, y):
    m, n = X.shape
    best_gain = 0
    best_idx, best_thr = None, None
    parent_entropy = entropy(y)
    for idx in range(n):
        thresholds = np.unique(X[:, idx])
        for i in range(1, len(thresholds)):
            thr = (thresholds[i] + thresholds[i-1]) / 2
            left = y[X[:, idx] <= thr]
            right = y[X[:, idx] > thr]
            if len(left) == 0 or len(right) == 0:
                continue
            left_entropy = entropy(left)
            right_entropy = entropy(right)
            gain = parent_entropy - (len(left)/m)*left_entropy - (len(right)/m)*right_entropy
            if gain > best_gain:
                best_gain = gain
                best_idx = idx
                best_thr = thr
    return best_idx, best_thr

class DecisionTreeNode:
    def __init__(self, is_leaf=False, prediction=None, feature_index=None, threshold=None, left=None, right=None):
        self.is_leaf = is_leaf
        self.prediction = prediction
        self.feature_index = feature_index
        self.threshold = threshold
        self.left = left
        self.right = right

class DecisionTreeClassifierNumpy:
    def __init__(self, max_depth=None, min_samples_split=2):
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.root = None

    def fit(self, X, y):
        self.n_classes_ = len(np.unique(y))
        self.root = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        if len(np.unique(y)) == 1:
            return DecisionTreeNode(is_leaf=True, prediction=int(y[0]))
        if self.max_depth is not None and depth >= self.max_depth:
            prediction = Counter(y).most_common(1)[0][0]
            return DecisionTreeNode(is_leaf=True, prediction=prediction)
        if X.shape[0] < self.min_samples_split:
            prediction = Counter(y).most_common(1)[0][0]
            return DecisionTreeNode(is_leaf=True, prediction=prediction)
        idx, thr = best_split(X, y)
        if idx is None:
            prediction = Counter(y).most_common(1)[0][0]
            return DecisionTreeNode(is_leaf=True, prediction=prediction)
        left_mask = X[:, idx] <= thr
        right_mask = X[:, idx] > thr
        left = self._build_tree(X[left_mask], y[left_mask], depth+1)
        right = self._build_tree(X[right_mask], y[right_mask], depth+1)
        return DecisionTreeNode(is_leaf=False, feature_index=idx, threshold=thr, left=left, right=right)

    def predict_one(self, x):
        node = self.root
        while not node.is_leaf:
            if x[node.feature_index] <= node.threshold:
                node = node.left
            else:
                node = node.right
        return node.prediction

    def predict(self, X):
        return np.array([self.predict_one(x) for x in X])

# Example usage:
if __name__ == "__main__":
    # Example: XOR problem
    X = np.array([[0,0],[0,1],[1,0],[1,1]], dtype=float)
    y = np.array([0,1,1,0], dtype=int)
    clf = DecisionTreeClassifierNumpy(max_depth=2)
    clf.fit(X, y)
    preds = clf.predict(X)
    print("Predictions:", preds.tolist())
