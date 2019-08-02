import argparse
import os
import pandas as pd
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import robust_scale
import sys
import time
from util import DataFrameCache, get_dataset_path_dict, no_extension

def cross_validate(df, predict_column, learner):
    meta_cols = list(df.select_dtypes(include=['object', 'int']).columns)
    X = robust_scale(df.drop(meta_cols, axis="columns"))
    y = df[predict_column]

    scoring_metric = "balanced_accuracy"
    n_jobs = 4

    scores = []
    for i in range(iterations):
        fit_params = learner[1]
        estimator = learner[0](**fit_params)

        if "random_state" in fit_params:
            fit_params["random_state"] = i

        scores += list(cross_val_score(estimator, X, y, scoring=scoring_metric, cv=folds, n_jobs=n_jobs))

    return scores

def baseline(df, column):
    return df[column].value_counts().max() / len(df)

def get_batch_col(dataset):
    if "bladderbatch" in dataset:
        return "batch"
    elif "tcga" in dataset:
        return "CancerType"
    elif "gse" in dataset:
        return "plate"
    else:
        return "Batch"

def get_true_col(dataset):
    if "bladderbatch" in dataset:
        return "cancer"
    elif "tcga" in dataset:
        return "TP53_Mutated"
    elif "gse" in dataset:
        return "Stage"
    else:
        return "Batch"

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-dirs", nargs="+", help="List of input directories", required=True)
parser.add_argument("-o", "--output-path1", help="Path to output file 1", required=True)
parser.add_argument("-p", "--output-path2", help="Path to output file 1", required=True)
args = parser.parse_args()

iterations = 10
# It makes sense to use 2 folds because there are few samples for some of the classes
folds = 2

cache = DataFrameCache()

#LEARNERS = [(RandomForestClassifier, {"n_estimators": 100, "random_state": 0})]
LEARNERS = [
    (RandomForestClassifier, {"n_estimators": 100, "random_state": 0}),
    (SVC, {"gamma": "auto", "random_state": 0}),
    (KNeighborsClassifier, {})
]

batch_results = [["metric", "adjuster", "dataset", "value"]]
true_results = list(batch_results)

for inpath in args.input_dirs:
    unadjusted_path = inpath + "/unadjusted.csv"

    unadj = cache.get_dataframe(unadjusted_path)
    dataset = os.path.basename(inpath)

    batch_column = get_batch_col(dataset)
    true_column = get_true_col(dataset)

    baseline_batch_acc = baseline(unadj, batch_column)
    baseline_true_acc = baseline(unadj, true_column)

    for method in ["unadjusted", "scaled", "combat", "confounded"]:
        df = cache.get_dataframe(inpath + "/" + method + ".csv")

        for learner in LEARNERS:
            classifier_name = str(learner[0]).split("'")[1].split(".")[-1].replace("Classifier", "")

            for score in cross_validate(df, batch_column, learner):
                batch_results.append([classifier_name, method, dataset, str(score)])

            for score in cross_validate(df, true_column, learner):
                true_results.append([classifier_name, method, dataset, str(score)])

with open(args.output_path1, 'w') as output_file:
    for line in batch_results:
        output_file.write(",".join(line) + "\n")

with open(args.output_path2, 'w') as output_file:
    for line in true_results:
        output_file.write(",".join(line) + "\n")
