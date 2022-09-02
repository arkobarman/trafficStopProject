install.packages("arrow")
library('arrow')

df <- readRDS("C:/Users/tejes/OneDrive/Desktop/traffic_stop.rds")
write_parquet(df, sink = 'C:/Users/tejes/OneDrive/Desktop/traffic.parquet')



