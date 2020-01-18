import numpy as np
import random
from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
import sys

out_file_path = sys.argv[1]

n_samples = 100 # Must be an even number
n_random_features = 800
#n_random_features = 19800
n_informative_features = 25
n_redundant_features = 175

# This controls the ability to differentiate between the batches and class labels.
class_sep = 2.0

random_state = 0
random.seed(random_state)

n_features = n_random_features + n_informative_features + n_redundant_features

X, batches = make_classification(n_samples, n_features, n_informative_features,
        n_redundant_features, n_clusters_per_class=2, random_state=random_state,
        shuffle=False, flip_y=0.0, class_sep = class_sep)

labels = [0 for x in range(int(n_samples / 2))] + [1 for x in range(int(n_samples / 2))]
random_labels = list(labels)
random.shuffle(random_labels)
labels = np.array(labels)
random_labels = np.array(random_labels)
random_batches = list(batches)
random.shuffle(random_batches)
random_batches = np.array(random_batches)

X = preprocessing.scale(X)

## Used this code to verify that we can differentiate the classes and batches
clf = RandomForestClassifier(max_depth=5, n_estimators=100, random_state=random_state)
#clf = SVC(gamma="scale", random_state=random_state)

print("Predicting true labels:")
print(np.mean(cross_val_score(clf, X, labels, cv=5)))
print("Predicting randomized labels:")
print(np.mean(cross_val_score(clf, X, random_labels, cv=5)))
print("Predicting batches:")
print(np.mean(cross_val_score(clf, X, batches, cv=5)))
print("Predicting randomized batches:")
print(np.mean(cross_val_score(clf, X, random_batches, cv=5)))

with open(out_file_path, 'w') as out_file:
    out_file.write(",".join(["ID", "Class", "Batch"] + ["Gene%i" % i for i in range(1, n_features + 1)]) + "\n")

    i = 0
    for row in X:
        batch = str(batches[i])
        label = str(labels[i])
        out_file.write(",".join(["Sample{}".format(i + 1), label, batch] + [str(x) for x in row]) + "\n")
        i += 1
