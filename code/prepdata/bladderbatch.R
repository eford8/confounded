library(pacman)
library(argparse)
library(dplyr)
library(readr)

parser <- ArgumentParser()
parser$add_argument("outfile", help = "Path to the output file")
args <- parser$parse_args()

library(bladderbatch)
data(bladderdata)

clin_df <- bladderEset %>%
  pData() %>%
  as_tibble(rownames = "id")

gene_df <- bladderEset %>%
  exprs() %>%
  t() %>%
  as_tibble(rownames = "id")

all <- inner_join(clin_df, gene_df, by = "id")

write_csv(all, args$outfile)
