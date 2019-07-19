install.packages(c("pacman", "dplyr", "readr", "stringr", "tibble", "ggplot2", "gridExtra", "png", "magick", "colorspace", "pracma", "kableExtra", "Rtsne", "argparse", "docstring"))

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("bladderbatch")
BiocManager::install("sva")
