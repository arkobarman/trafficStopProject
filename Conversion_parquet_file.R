install.packages("arrow", dependencies = TRUE)
library('arrow')


df <- readRDS("data/yg821jf8611_tx_statewide_2020_04_01.rds")
write_parquet(df, sink = 'data/traffic.parquet')



