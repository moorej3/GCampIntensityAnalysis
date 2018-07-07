files <- list.files(pattern = "_backward",recursive = T)

#Find average power of each kymograph
library(OpenImageR)
library(WaveletComp)
Name <- character()
avg <- numeric()
for(file in files){
  Im <- readImage(file)
  ImS <- colSums(Im)/ncol(Im)
  ImD <- data.frame(ImS)
  ImWa <- analyze.wavelet(ImD,
                        "ImS",
                        loess.span = 0,
                        dt = 1,
                        dj = 1/250,
                        lowerPeriod = 16,
                        upperPeriod = 128,
                        make.pval = T,
                        n.sim = 10)
  avg <- c(avg, max(ImWa$Power.avg))
  Name <- c(Name, file)
}


#Plotting
Data <- data.frame(avg, Name)
Data$Strain <- gsub("/kym.*","", Data$Name)
Data$Strain <- gsub(".*/","", Data$Strain)
head(Data)

library(ggplot2)

ggplot(Data, aes(x = Strain, y = avg)) + 
  geom_boxplot()+
  geom_jitter(width = 0.1)











