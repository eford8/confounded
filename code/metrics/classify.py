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

def cross_validate(df, predict, model, **kwargs):
    meta_cols = list(df.select_dtypes(include=['object', 'int']).columns)
    X = robust_scale(df.drop(meta_cols, axis="columns"))
    y = df[predict]

    classifier = model(**kwargs)
    scores = []

    for _ in range(iterations):
        scores += list(cross_val_score(classifier, X, y, scoring="balanced_accuracy", cv=folds, n_jobs=4))

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

iterations = 5
folds = 5
random_state = 3333

cache = DataFrameCache()
LEARNERS = [
    (RandomForestClassifier, {"n_estimators": 100, "random_state": random_state}),
    (SVC, {"random_state": random_state, "gamma": "auto"}),
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

            batch_scores = cross_validate(df, predict=batch_column, model=learner[0], **learner[1])
            batch_value = sum(batch_scores) / len(batch_scores)
            batch_results.append([classifier_name, method, dataset, str(batch_value)])

            true_scores = cross_validate(df, predict=true_column, model=learner[0], **learner[1])
            true_value = sum(true_scores) / len(true_scores)
            true_results.append([classifier_name, method, dataset, str(true_value)])

with open(args.output_path1, 'w') as output_file:
    for line in batch_results:
        output_file.write(",".join(line) + "\n")

with open(args.output_path2, 'w') as output_file:
    for line in true_results:
        output_file.write(",".join(line) + "\n")
