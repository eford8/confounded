if (!require("pacman")) install.packages("pacman"); library(pacman)
p_load(tidyverse)

IN_FILE <- "../data/input/tcga/tcga.csv"
OUT_DIR <- "../data/input/"
MEDIUM <- paste0(OUT_DIR, "/tcga_medium/medium.csv")
SMALL <- paste0(OUT_DIR, "/tcga_small/small.csv")

get_group <- function(df, colname, value) {
  colname <- enquo(colname)
  df %>%
    filter(!! colname == value)
}

sample_stratified <- function(data, strategy, group_col = "group") {
  group_col <- sym(group_col)
  result <- list()
  groups <- unique(unlist(select(data, !!group_col)))
  for (g in groups) {
    chunk <- data %>% filter(!!group_col == g)
    n <- ceiling(strategy(chunk))
    result[[g]] <- sample_n(chunk, n)
  }
  bind_rows(result)
}

sample_log <- function(data, group_col = "group") {
  sample_stratified(data, function(data) {
    log(nrow(data))
  }, group_col)
}

sample_sqrt <- function(data, group_col = "group", scale = 1) {
  sample_stratified(data, function(data) {
    sqrt(nrow(data)) * scale
  }, group_col)
}

tcga <- read_csv(IN_FILE)
tcga %>% group_by(CancerType) %>% summarize(count=ceiling(sqrt(n()))) %>% arrange(desc(count)) %>% ungroup()

set.seed(0)
sample_sqrt(tcga, group_col = "CancerType", scale = 2) %>% write_csv(MEDIUM)
sample_log(tcga, "CancerType") %>% write_csv(SMALL)
