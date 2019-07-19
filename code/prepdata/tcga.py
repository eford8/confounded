import argparse
import pandas as pd

def maybe_to_int(col):
    try:
        return int(col)
    except:
        return col

def to_sparse_matrix(df):
    df["one"] = 1
    df["MutatedGene"] = df["MutatedGene"].apply(lambda x: str(x) + "_mutation")
    matrix = df.pivot(index="Sample", columns="MutatedGene", values="one").fillna(0)
    small_mx = matrix.loc[:, matrix.columns[matrix.sum() > 2000]]
    return small_mx

parser = argparse.ArgumentParser()
parser.add_argument("rnaseq", help="Path to RNA Seq data")
parser.add_argument("mutations", help="Path to somatic mutations data")
parser.add_argument("cancer_types", help="Path to cancer types data")
parser.add_argument("outfile", help="Path to outfile")
args = parser.parse_args()

mutations = pd.read_csv(args.mutations, sep="\t")
ctypes = pd.read_csv(args.cancer_types, sep="\t")
expression = pd.read_csv(args.rnaseq, sep="\t")

most_mutated = mutations['MutatedGene'].value_counts()[:5].index.tolist()
mutations = mutations[mutations['MutatedGene'].isin(most_mutated)]
mutations_matrix = to_sparse_matrix(mutations)

clinical = ctypes.merge(mutations_matrix, on="Sample", how="left").fillna(0)
clinical = clinical.applymap(maybe_to_int)
all_data = clinical.merge(expression, on="Sample", how="inner").drop_duplicates()

all_data.to_csv(args.outfile, index=False)
