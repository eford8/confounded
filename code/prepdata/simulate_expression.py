from sklearn import preprocessing
from sklearn.datasets import make_classification
import sys

out_file_path = sys.argv[1]

n_samples = 100 # Must be an even number
n_random_features = 800
n_informative_features = 25
n_redundant_features = 175
#n_redundant_features = 175
#n_random_features = 19800
#n_informative_features = 25
#n_redundant_features = 175
class_sep = 1.0
random_state = 0

n_features = n_random_features + n_informative_features + n_redundant_features

#sklearn.datasets.make_classification(n_samples=100, n_features=20, n_informative=2, n_redundant=2, n_repeated=0, n_classes=2, n_clusters_per_class=2, weights=None, flip_y=0.01, class_sep=1.0, hypercube=True, shift=0.0, scale=1.0, shuffle=True, random_state=None)[source]¶
X, y = make_classification(n_samples, n_features, n_informative_features, n_redundant_features, n_clusters_per_class=1, random_state=random_state, shuffle=False, flip_y=0.0, class_sep = class_sep)

X = preprocessing.scale(X)

labels = [i % 2 for i in range(n_samples)]

## Used this code to verify that we can differentiate the classes
#from sklearn.svm import LinearSVC
#clf = LinearSVC(C=1.0)
#from sklearn.model_selection import cross_val_score
#scores = cross_val_score(clf, X, y, cv=5)
#print(scores)
#sys.exit(0)

with open(out_file_path, 'w') as out_file:
    out_file.write("\t".join(["ID", "Class", "Batch"] + ["Gene%i" % i for i in range(1, n_features + 1)]) + "\n")

    i = 1
    for row in X:
        batch = y[i-1]
        label = "Label{}".format(labels[i-1])
        out_file.write("\t".join(["Sample%i" % i, label, str(batch)] + [str(x) for x in row]) + "\n")
        i += 1
