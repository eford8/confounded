import argparse
import numpy as np
from sklearn.metrics.pairwise import rbf_kernel, linear_kernel
from util import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-files", nargs="+",
                    help="List of input files", required=True)
parser.add_argument("-o", "--output-path", help="Path to output file", required=True)
args = parser.parse_args()

def mmd(sample1, sample2, kernel=rbf_kernel):
    # TODO: update the kernel to reflect the DMResNet paper:
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
    batches = split_into_batches(df, batch_col)
#    if log_adjust:
#        batches = tuple([log_scale(batch) for batch in batches])
    return mmd_multi_batch(batches)

# Open files
cache = DataFrameCache()

# Make a logger
logger = Logger("MMD")

# Calculate metrics
for inpath in args.input_files:
    unadj_path, adj_paths = list(get_dataset_path_dict(inpath).items())[0]
    unadj = cache.get_dataframe(unadj_path)
    dataset = no_extension(unadj_path)
    for path in [unadj_path] + adj_paths:
        df = cache.get_dataframe(path)
        no_ext = no_extension(path)
        if no_ext == dataset:
            adjuster = "unadjusted"
        else:
            adjuster = no_ext.replace(dataset, "").lstrip("_")
        print("Calculating MMD for the {} x {} dataset".format(dataset, adjuster))
        if "bladderbatch" in dataset:
            batch_col = "batch"
        elif "tcga" in dataset:
            batch_col = "CancerType"
        elif "gse" in dataset:
            batch_col = "plate"
        else:
            batch_col = "Batch"
        value = calculate_mmd(df, batch_col)
        # Store metrics in logger
        logger.log(adjuster, dataset, value)

# Save log
logger.save(args.output_path)
