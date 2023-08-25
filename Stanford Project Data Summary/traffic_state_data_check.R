#install.packages("arrow")
#library('arrow')
#write_parquet(df, sink = '/Users/luominxuan/Desktop/traffic.parquet')

filename <- '/Users/luominxuan/Desktop/tx_statewide.rds'
df <- readRDS(filename)
head(df)
print('Percent of Citation Issued: ')
print(length(df$citation_issued[df$citation_issued == TRUE])/nrow(df))
#print(length(df$search_conducted[df$search_conducted == TRUE])/nrow(df))
print(nrow(df[df$search_conducted == TRUE,])/nrow(df))
print(nrow(df[df$contraband_found == TRUE & df$search_conducted == TRUE,])/nrow(df[df$search_conducted == TRUE,]))

print(length(df$search_conducted[df$search_conducted == TRUE]))
print(length(df$contraband_found[df$contraband_found == TRUE]))
#print(sum(df$citation_issued)/nrow(df))
print('Missing values of columns: ')
print(100*round(colMeans(is.na(df)),3))
colnames(df)
