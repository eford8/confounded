import argparse
import numpy as np
import os
from util import *

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-dirs", nargs="+",
                    help="List of input directories", required=True)
parser.add_argument("-o", "--output-path", help="Path to output file", required=True)
args = parser.parse_args()

def calculate_mse(df1, df2):
    _, genes1 = split_discrete_continuous(df1)
    _, genes2 = split_discrete_continuous(df2)

    squared_error = (np.array(genes1) - np.array(genes2))**2

    return squared_error.mean()

# Open files
cache = DataFrameCache()

# Make a logger
logger = Logger("MSE")

# Calculate metrics
for inpath in args.input_dirs:
    unadjusted_path = inpath + "/unadjusted.csv"

    unadj = cache.get_dataframe(unadjusted_path)
    dataset = os.path.basename(inpath)

    for method in ["scaled", "combat", "confounded"]:
        adjusted_path = inpath + "/" + method + ".csv"
        df = cache.get_dataframe(adjusted_path)

        print("Calculating MSE for the {} method on the {} dataset".format(dataset, method))
        value = calculate_mse(unadj, df)

        # Store metrics in logger
        logger.log(method, dataset, value)

# Save log
logger.save(args.output_path)
