
# Load Libraries
library(ggplot2)
library(reshape2)

# Read arguments from command line as a list # 
# ------------------------------------------ #
args <- commandArgs(trailingOnly = TRUE)

input_file = args[1]
output_file = args[2]

# Load data and Preprocess #
# ------------------------ #
df = read.csv(input_file)

# Parse dates
dates = as.POSIXct(df[['date']], format="%Y-%m-%d %H:%M:%S")
df['date'] = dates

df_melt = melt(df, id.vars = 'date')

# Produce figure #
# -------------- #
png(filename=output_file,  width=800, height=600)

  ggplot(df_melt, aes(x = date, y = value, group=variable)) + 
    geom_line() + 
    facet_wrap(~ variable, scales = 'free_y', ncol = 1)

dev.off()
