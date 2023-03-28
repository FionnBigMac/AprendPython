import numpy as np

def distancia(a, item):
    return np.linalg.norm(a-item)

labels = np.zeros_like(y_test)
for i, row in enumerate(X_test):
    row_dist = np.apply_along_axis(distancia, 1, X_train, item=row)
    row_sort = np.argsort(row_dist)
    row_label = y_train[row_sort[:k]]
    u, c = np.unique(y_train[row_sort[:k]], return_counts = True)
    labels[i] = u[c == c.max()]

print(len(labels))
print(labels)
print((labels - y_test)==0)