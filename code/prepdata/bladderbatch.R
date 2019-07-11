if (!require("pacman")) install.packages("pacman"); library(pacman)
p_load("tidyverse", "argparse")

parser <- ArgumentParser()
parser$add_argument("outfile", help = "Path to the output file")
args <- parser$parse_args()

if (!requireNamespace("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install("bladderbatch")
library(bladderbatch)
data(bladderdata)

clin_df <- bladderEset %>%
  pData() %>%
  as.tibble(rownames = "id")
gene_df <- bladderEset %>%
  exprs() %>%
  t() %>%
  as.tibble(rownames = "id")

all <- inner_join(clin_df, gene_df, by = "id")

write_csv(all, args$outfile)
