Data = read.csv("Data.csv")
MLength = read.csv("FlagellaLengths.csv")

library(gridExtra)
library(mosaic)

#First, plot the distribution of flagella lengths that were calculated by the program
#and lengths I meausred manually, to verify the program is working.
p1 <- ggplot(Data, aes(x = flalength)) + 
  geom_density(fill = "blue", alpha = 0.5) + 
  ggtitle("Calculated")+
  ylim(0,0.4)
p2 <- ggplot(MLength, aes(x = Length)) + 
  geom_density(fill = 'red', alpha = 0.5) + 
  ggtitle("Measured")+
  ylim(0,0.4)
grid.arrange(p1,p2, nrow=1)


#Now, measure Calcium/time as function of length
CaTime.lm <- lm(CaPerTime~flalength, data = Data)
equation = paste("y =", round(CaTime.lm$coefficients[2],1), "x +", round(CaTime.lm$coefficients[1],1), 
                 "\n r-squared =", round(summary(CaTime.lm)$r.squared,2))

p1 = ggplot(Data, aes(x = flalength, y = CaPerTime)) + 
  geom_point() +
  geom_smooth(method = "lm", se=FALSE)+
  xlab("Flagella Length (um)")+
  ylab("Average Calcium Over Time (Intensity/Time)")+
  theme_classic()+
  annotate("text", label = equation, x = 12, y = 1200)+
  ggtitle("Average Calcium over time")

#Now measure Calcium per pulse as a function of flagella length
CaPulse.lm = lm(CaPerPulse~flalength, data = Data)
equation = paste("y =", round(CaPulse.lm$coefficients[2],1), "x +", round(CaPulse.lm$coefficients[1],1),
                 "\n r-squared =", round(summary(CaPulse.lm)$r.squared,2))

p2 = ggplot(Data, aes(x = flalength, y = CaPerPulse))+
  geom_point()+
  geom_smooth(method = "lm", se=FALSE)+
  xlab("Flagella Length (um)")+
  ylab("Average Calcium per Pulse (Intensity/Pulses)")+
  theme_classic()+
  annotate("text", label = equation, x=12, y=100000)+
  ggtitle("Average Calcium per Pulse")

grid.arrange(p1,p2,nrow=1)



