View(MSEE)
MSEE$`Exp Site`<-as.factor(MSEE$`Exp Site`)
MSEE$`Main treatment`<-as.factor(MSEE$`Main treatment`)
MSEE$`Sub treatment`<-as.factor(MSEE$`Sub treatment`)
MSEE$Treatment<-as.factor(MSEE$Treatment)
library(dplyr)
data1<- MSEE %>% 
  filter(Treatment=="Closed")
data1<-data1 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data1) # germination capacity for closed

data1 %>%
  ggplot(aes(x=))

data2<- MSEE %>% 
  filter(Treatment=="Opened")
data2<-data2 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data2) # germination capacity for Opened

data3<- MSEE %>% 
  filter(`Exp Site` =="KEFRI/Kibwezi")
data3<-data3 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data3) # germination capacity for KEFRI/ KBZ

data4<- MSEE %>% 
  filter(`Exp Site` =="Kituku")
data4<-data4 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data4) # germination capacity for Kituku

data5<- MSEE %>% 
  filter(`Main treatment` =="Melia_nuts_stored")
data5<-data5 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data5) # germination capacity for Melia nuts

data6<- MSEE %>% 
  filter(`Main treatment` =="Melia_seeds_stored")
data6<-data6 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data6) # germination capacity for Melia seeds

data7<- MSEE %>% 
  filter(`Sub treatment` =="Cold_storage_at_negative_20???")
data7<-data7 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data7) # germination capacity for Cold storage at negative 20???

data8<- MSEE %>% 
  filter(`Sub treatment` == "Room_temp_at_20???±2???")
data8<-data8 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data8) # germination capacity for Room temp' at Temp' at 26??? ± 2???

data9<- MSEE %>% 
  filter(`Sub treatment` =="Temp_at_4???")
data9<-data9 %>%
  select(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`)
View(data9) # germination capacity for Room temp' at Temp' at 26??? ± 2???

attach(MSEE)
str(MSEE)
library(ggplot2)
par(mfrow = c(2,6), pty = "s")
ggplot(data = MSEE, aes(x = `Exp Site`)) +
  geom_line(aes(y=`Initial_germination_capacity_28/5/2020`), color = 'blue')+
  geom_line(aes(y=`First_germination_capacity_9/7/2020`), color = 'red')+
  geom_line(aes(y=`Second_germination_capacity_6/8/2020`), color = 'blue')
  
  

ggplot(data = MSEE, mapping = aes(x = `Exp Site`, y = `Initial_germination_capacity_28/5/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Exp Site`, y = `First_germination_capacity_9/7/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Exp Site`, y = `Second_germination_capacity_6/8/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Exp Site`, y = `Third_germination_capacity_11/9/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Exp Site`, y = `Fourth_germination_capacity_13/11/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Exp Site`, y = `Fifth_germination_capacity_1/2/2021`)) +
  geom_boxplot()+
  coord_flip()






ggplot(data = MSEE, mapping = aes(x = `Sub treatment`, y = `Initial_germination_capacity_28/5/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Sub treatment`, y = `Initial_germination_capacity_28/5/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Sub treatment`, y = `Germination_capacity_11/9/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Sub treatment`, y = `Germination_capacity_13/11/2020`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Sub treatment`, y = `Germination_capacity_1/2/2021`)) +
  geom_boxplot()+
  coord_flip()
ggplot(data = MSEE, mapping = aes(x = `Sub treatment`, y = `Germination_capacity_15/3/2021`)) +
  geom_boxplot()+
  coord_flip()

barplot(`Germination_capacity_1/2/2021`)


library(tidyverse)
attach(MSEE)
data7 %>%
  pivot_longer(`Initial_germination_capacity_28/5/2020`:`Seventh_germination_capacity_12/10/2021`, names_to = "Germination", values_to = "Capacity") %>%
  ggplot(aes(x = Capacity))+
  geom_bar()+
  facet_wrap(vars(Germination), ncol = 3)+
  labs(x = "Germination capacity")

longi<-MSSE_data_tomorrow
longi$ExpSite<-as.factor(longi$ExpSite)
longi$Maintreatment<-as.factor(longi$Maintreatment)
longi$Subtreatment<-as.factor(longi$Subtreatment)
longi$Treatment<-as.factor(longi$Treatment)
longi$Germination<-as.factor(longi$Germination)
str(longi)
library(lattice)
xyplot(Germ_Capacity~Germination|ExpSite, groups = Maintreatment, data = longi, type = 'b')

fig_a <- ggplot(longi, aes(Germination, Germ_Capacity))
fig_b<- fig_a+geom_line(aes(color = Subtreatment, group = id))+
  geom_point()+
  facet_wrap(~ExpSite, labeller = label_both)+
  stat_summary(aes(group = ExpSite, Color = paste(Treatment)), geom = 'line', fun.y = mean, size = 3)
fig_b

fig_c<- fig_a+
  stat_summary(aes(group = Treatment, Color = Treatment), geom = 'line', fun = mean, size = 3)
fig_c