Data = read.csv("Data.csv")

#Data reformatting
Data$Strain <- gsub("\\\\kym.*","",Data$Sample)
Data$Strain <- gsub(".*\\\\","", Data$Strain)
head(Data)

library(mosaic)


#First, plot the distribution of flagella lengths that were calculated by the program
#and lengths I meausred manually, to verify the program is working.
ggplot(Data, aes(x = flalength)) + 
  geom_density(fill = "blue", alpha = 0.5) + 
  ggtitle("Calculated")+
  ylim(0,0.4)



#Now, measure Calcium/time as function of length
ggplot(Data, aes(x = flalength, y = CaPerTime, color = Strain)) + 
  geom_point() +
  geom_smooth(method = "lm", se=FALSE)+
  xlab("Flagella Length (um)")+
  ylab("Average Calcium Over Time (Intensity/Time)")+
  theme_classic()+
  ggtitle("Average Calcium over time")

ggplot(Data, aes(x = Strain, y = CaPerTime/flalength, fill = Strain))+
  geom_violin()


#Now measure Calcium per pulse as a function of flagella length
ggplot(Data, aes(x = flalength, y = CaPerPulse, color = Strain))+
  geom_point()+
  geom_smooth(method = "lm", se=FALSE)+
  xlab("Flagella Length (um)")+
  ylab("Average Calcium per Pulse (Intensity/Pulses)")+
  theme_classic()+
  ggtitle("Average Calcium per Pulse")


ggplot(Data, aes(x = Strain, y = CaPerPulse/flalength, fill = Strain))+
  geom_violin()



