
# Example: read exported CSV and run a simple regression in R
df <- read.csv('exports/data_for_r.csv')
model <- lm(y ~ x1 + x2, data=df)
summary(model)
