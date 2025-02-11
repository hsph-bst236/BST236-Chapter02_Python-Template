# Data cleaning script
# This script processes raw data into analysis-ready format

library(tidyverse) 
library(here)

getwd()
here() # project root directory
dirname(rstudioapi::getActiveDocumentContext()$path) # current script directory
# Set up project path
here::i_am("src/R/00_clean_data.R")

# Load raw data
raw_data <- read_csv(here::here("data", "boston.csv"), show_col_types = FALSE)

# Plot house prices versus room
ggplot(raw_data, aes(x = RM, y = MEDV)) +
  geom_point() +
  labs(title = "House Prices vs Room Numbers",
	   x = "Room Numbers",
	   y = "House Prices")