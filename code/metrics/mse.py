import argparse
import numpy as np
from util import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-files", nargs="+",
                    help="List of input files", required=True)
parser.add_argument("-o", "--output-path", help="Path to output file", required=True)
args = parser.parse_args()


def calculate_mse(df1, df2):
    _, genes1 = split_discrete_continuous(df1)
    _, genes2 = split_discrete_continuous(df2)
#    if log_adjust:
#        genes1 = log_scale(genes1)
#        genes2 = log_scale(genes2)
    squared_error = (np.array(genes1) - np.array(genes2))**2
    return squared_error.mean()

# Open files
cache = DataFrameCache()

# Make a logger
logger = Logger("MSE")

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
        print("Calculating MSE for the {} x {} dataset".format(dataset, adjuster))
        value = calculate_mse(unadj, df)
        # Store metrics in logger
        logger.log(adjuster, dataset, value)

# Save log
logger.save(args.output_path)
