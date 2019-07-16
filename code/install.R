install.packages(c("pacman", "dplyr", "readr", "stringr", "tibble", "argparse", "docstring"))

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("bladderbatch")
BiocManager::install("sva")
