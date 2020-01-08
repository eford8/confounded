import numpy as np
import random
from sklearn import preprocessing
#from sklearn.datasets import make_classification
from sklearn.datasets import make_checkerboard
import sys

out_file_path = sys.argv[1]

n_samples = 400
n_features = 10000
n_clusters = 4
n_samples_per_cluster =  int(n_samples / n_clusters)

X, rows, columns = make_checkerboard(
    shape=(n_samples, n_features), n_clusters=(n_clusters, n_clusters), noise=1,
    shuffle=False, random_state=0, minval=-3, maxval=3)

#X = preprocessing.scale(X)

labels = [0] * n_samples_per_cluster + [1] * n_samples_per_cluster + [0] * n_samples_per_cluster + [1] * n_samples_per_cluster
batches = [0] * n_samples_per_cluster + [0] * n_samples_per_cluster + [1] * n_samples_per_cluster + [1] * n_samples_per_cluster

## Used this code to verify that we can differentiate the classes
from sklearn.svm import SVC
clf = SVC(gamma="scale", random_state=0)
from sklearn.model_selection import cross_val_score
print("Predicting true labels:")
print(np.mean(cross_val_score(clf, X, labels, cv=5)))
print("Predicting randomized labels:")
random.seed(0)
random_labels = list(labels)
random.shuffle(random_labels)
print(np.mean(cross_val_score(clf, X, random_labels, cv=5)))
print("Predicting batches:")
print(np.mean(cross_val_score(clf, X, batches, cv=5)))
print("Predicting randomized batches:")
random_batches = list(batches)
random.shuffle(random_batches)
print(np.mean(cross_val_score(clf, X, random_batches, cv=5)))

with open(out_file_path, 'w') as out_file:
    out_file.write(",".join(["ID", "Class", "Batch"] + ["Gene%i" % i for i in range(1, n_features + 1)]) + "\n")

    i = 0
    for row in X:
        batch = str(batches[i])
        label = str(labels[i])
        out_file.write(",".join(["Sample{}".format(i + 1), label, batch] + [str(x) for x in row]) + "\n")
        i += 1
