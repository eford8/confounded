# Load packages ---------
if (!require("pacman")) install.packages("pacman"); library(pacman)
p_load("tidyverse", "Rtsne")
source("functions.R")

IN_DIR = "../data/input/"
OUT_DIR = "../data/output/"

# Functions ----------
continuous_cols <- function(df) {
  df %>%
    select_if(function (col) !is.whole(col) & is.numeric(col))
}

# Load data --------------------
set.seed(0)
unadjusted <- read_csv(paste(c(IN_DIR, "/mnist/noisy.csv"), collapse = ""))
combat <- read_csv(paste(c(IN_DIR, "/mnist/noisy_combat.csv"), collapse = ""))
scaled <- read_csv(paste(c(IN_DIR, "/mnist/noisy_scale.csv"), collapse = ""))
confounded <- read_csv(paste(c(IN_DIR, "/mnist/noisy_confounded.csv"), collapse = ""))

titles <- list(
  unadjusted = "Unadjusted",
  scale = "Scale Adjustment",
  combat = "ComBat",
  confounded = "Confounded"
)

dfs <- list(
  mutate(unadjusted, dataset=titles$unadjusted),
  mutate(combat, dataset=titles$combat),
  mutate(scaled, dataset=titles$scale),
  mutate(confounded, dataset=titles$confounded)
)

# PCA and tSNE function -----------
dim_reduce_df <- function(my_df) {
  continuous <- my_df %>% continuous_cols()
  pca <- prcomp(continuous)$x
  ndim <- min(nrow(continuous), ncol(continuous), 100) # Restrict to at most 100 PCs for tsne
  tsne <- pca[, 1:ndim] %>%
    Rtsne() %>%
    .$Y
  batch <- factor(my_df$Batch)
  vals <- list(
    dataset = my_df$dataset,
    Batch = batch,
    PC1 = pca[, "PC1"],
    PC2 = pca[, "PC2"],
    Dim1 = tsne[, 1],
    Dim2 = tsne[, 2]
  )
  as_tibble(vals)
}

pca_list <- lapply(dfs, dim_reduce_df)
combined <- do.call("rbind", pca_list)
combined$dataset <- factor(combined$dataset, levels = titles)

# ? --------------------
combined %>% ggplot(aes(x = PC1, y = PC2, color = Batch)) +
  geom_point() +
  facet_wrap(~dataset, nrow=2) +
  labs(title = "MNIST PCA")
ggsave(paste(c(OUT_DIR, "/mnist_pca.pdf"), collapse = ""))
combined %>% ggplot(aes(x = Dim1, y = Dim2, color = Batch)) +
  geom_point() +
  facet_wrap(~dataset, nrow = 2) +
  labs(title = "MNIST t-SNE")
ggsave(paste(c(OUT_DIR, "/mnist_tsne.pdf"), collapse = ""))
