# Load packages -----
if (!require("pacman")) install.packages("pacman"); library(pacman)
p_load("tidyverse", "gridExtra", "png", "stringr", "magick", "colorspace", "pracma")

# Load data ---------
df <- read_csv("/data/metrics/mnist_confounded_log.csv") %>% 
  select(ae_loss, disc_loss, iteration) %>% 
  gather("Function", "Loss Function", -iteration) %>% 
  mutate(Function = str_replace(Function, "_loss", "")) %>%
  mutate(Function = str_replace(Function, "ae", "Autoencoder")) %>%
  mutate(Function = str_replace(Function, "disc", "Discriminator")) %>%
  rename(Iteration = iteration)

# Make plots --------
df %>% 
  filter(Iteration > 9000) %>% 
  ggplot(aes(x = Iteration, y = `Loss Function`)) + 
    geom_line() + 
    geom_smooth() + 
    geom_vline(xintercept = 9600, color = "Red", linetype = "longdash") +
    facet_wrap(vars(Function), nrow=2, scales = "free_y") +
    theme_bw(base_size = 18)
ggsave("/data/output/loss_chart.pdf")
