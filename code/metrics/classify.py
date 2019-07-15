"""Predict the true class of MNIST digits with a SVC classifier.
"""
import pandas as pd
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from util import DataFrameCache, get_dataset_path_dict, no_extension
import time
from sklearn.model_selection import train_test_split

class CSVData(object):
    def __init__(self, path, meta_cols=None, predict="Batch"):
        df = pd.read_csv(path)
        if meta_cols is None:
            meta_cols = list(df.select_dtypes(include=['object', 'int']).columns)
        self.labels = df[predict]
        self.features = df.drop(meta_cols, axis="columns")
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(
            self.features, self.labels, test_size=0.2
        )

    @property
    def X(self):
        return self.features

    @property
    def Y(self):
        return self.labels

def cross_validate(path, meta_cols=None, predict="Batch", times=100, folds=5, model=RandomForestClassifier, **kwargs):
    classifier = model(**kwargs)
    data = CSVData(path, meta_cols, predict)
    accuracies = []
    elapsed_times = []
    for _ in range(times):
        start = time.time()
        try:
            accuracies += list(cross_val_score(
                classifier, data.X, data.Y, cv=folds, scoring="accuracy"
            ))
            elapsed_times.append(time.time() - start)
        except ValueError as e:
            print("Something didn't work with file {}, column {}, and classifier {}:".format(
                path, predict, model.__name__)
            )
            print(str(e))
    return {
        "accuracies": accuracies,
        "times": elapsed_times
    }

class Logger(object):
    def __init__(self, log_file):
        self.log_file = log_file
        self.values = {
            "path": [],
            "model": [],
            "predict": [],
            "dataset": [],
            "col_type": [],
            "baseline": [],
            "iteration": [],
            "accuracy": [],
            "time_elapsed": [],
            "adjuster": [],
        }

    def log(self, path, model, predict_col, dataset, col_type, baseline, accuracies, times_elapsed, adjuster):
        for i, (accuracy, time) in enumerate(zip(accuracies, times_elapsed)):
            self.values["path"].append(path)
            self.values["model"].append(model.__name__)
            self.values["predict"].append(predict_col)
            self.values["dataset"].append(dataset)
            self.values["col_type"].append(col_type)
            self.values["baseline"].append(baseline)
            self.values["iteration"].append(i)
            self.values["accuracy"].append(accuracy)
            self.values["time_elapsed"].append(time)
            self.values["adjuster"].append(adjuster)

    def save(self):
        pd.DataFrame(self.values).to_csv(self.log_file, index=False)


def baseline(path, column, cache=None):
    try:
        df = cache.get_dataframe(path)
    except AttributeError:
        df = pd.read_csv(path)
    return df[column].value_counts().max() / len(df)

if __name__ == "__main__":
    cache = DataFrameCache()
    # comparisons = cache.get_dataframe(COMPARISONS_PATH)
    LEARNERS = [
        (RandomForestClassifier, {"n_estimators": 10}),
        # (MLPClassifier, {"hidden_layer_sizes": tuple([5]*10), "max_iter": 1000}),
        (GaussianNB, {}),
        # (KNeighborsClassifier, {}),
        # (SVC, {"kernel": "rbf"})
    ]

    logger = Logger("../data/metrics/classification.csv")

    column_info = [
        ("../data/input/bladderbatch/", "batch", "cancer"),
        ("../data/input/gse37199/", "plate", "Stage"),
        ("../data/input/mnist/", "Batch", "Digit"),
        ("../data/input/tcga/", "CancerType", "TP53_mutation"),
    ]

    for data_dir, batch_col, true_class_col in column_info:
        unadj_path, adj_paths = list(get_dataset_path_dict(data_dir).items())[0]
        unadj = cache.get_dataframe(unadj_path)
        dataset = no_extension(unadj_path)
        for path in [unadj_path] + adj_paths:
            df = cache.get_dataframe(path)
            no_ext = no_extension(path)
            if no_ext == dataset:
                adjuster = "unadjusted"
            else:
                adjuster = no_ext.replace(dataset, "").lstrip("_")
            print("Working on {}: {}".format(dataset, adjuster))
            for column, col_type in [(batch_col, "batch_col"), (true_class_col, "true_class_col")]:
                for learner in LEARNERS:
                    baseline_acc = baseline(path, column, cache=cache)
                    cv_scores = cross_validate(
                        path,
                        predict=column,
                        model=learner[0],
                        folds=4,
                        times=3,
                        **learner[1]
                    )
                    logger.log(
                        path,
                        learner[0],
                        column,
                        dataset,
                        col_type,
                        baseline_acc,
                        cv_scores["accuracies"],
                        cv_scores["times"],
                        adjuster
                    )
    logger.save()
