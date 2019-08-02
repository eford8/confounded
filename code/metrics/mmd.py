import argparse
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel, linear_kernel
from util import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-dirs", nargs="+",
                    help="List of input directories", required=True)
parser.add_argument("-o", "--output-path", help="Path to output file", required=True)
args = parser.parse_args()

def mmd(sample1, sample2, kernel=rbf_kernel):
    """ "the kernel we used is a sum of three Gaussian kernels with
    different scales...We chose the [sigma_i]s to be m/2,m,2m, where m
    is the median of the average distance between a point in the
    target sample to its nearest 25 neighbors, a popular practice in
    kernel-based methods."
    - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5870543/
    """
    k_x_x = kernel(sample1, sample1)
    k_x_y = kernel(sample1, sample2)
    k_y_y = kernel(sample2, sample2)

    n = len(sample1)
    m = len(sample2)

    mean_xx = (1 / n**2) * k_x_x.sum()
    mean_xy = (1 / (m * n)) * k_x_y.sum()
    mean_yy = (1 / m**2) * k_y_y.sum()
    mmd_squared = mean_xx - 2 * mean_xy + mean_yy

    return mmd_squared ** 0.5

def mmd_multi_batch(batches):
    mmds = []
    for i in range(len(batches)):
        for j in range(i+1, len(batches)):
            mmds.append(mmd(batches[i], batches[j]))
    return np.array(mmds).mean()

def calculate_mmd(df, batch_col):
    return mmd_multi_batch(split_into_batches(df, batch_col))

def get_batch_col(dataset):
    if "bladderbatch" in dataset:
        return "batch"
    elif "tcga" in dataset:
        return "CancerType"
    elif "gse" in dataset:
        return "plate"
    else:
        return "Batch"

# Open files
cache = DataFrameCache()

# Make a logger
logger = Logger("MMD")

# Calculate metrics
for inpath in args.input_dirs:
    unadjusted_path = inpath + "/unadjusted.csv"

    unadj = cache.get_dataframe(unadjusted_path)
    dataset = os.path.basename(inpath)

    for method in ["scaled", "combat", "confounded"]:
        adjusted_path = inpath + "/" + method + ".csv"
        df = cache.get_dataframe(adjusted_path)

        print("Calculating MSE for the {} method on the {} dataset".format(dataset, method))
        value = calculate_mmd(df, get_batch_col(dataset))

        # Store metrics in logger
        logger.log(method, dataset, value)

# Save log
logger.save(args.output_path)
