library(tidyverse)
library(nycflights13)
library(dplyr)
attach(flights)
q8<- flights%>%
  count(tailnum) %>%
  filter(month == c(7,8,9))

target<-c("UA","AA","DL")
filter(flights, carrier %in% target)

target21<-c(7,8,9)
filter(flights, month %in% target21)

q23<- flights%>%
  count(tailnum) %>%
  filter(arr_delay>=1&&minute>30)
q23


target21<-c(7,8,9)
filter(flights, month %in% target21)

target2<-c("HOU","IAH")
filter(flights, dest %in% target2)

q4<- flights%>%
  count(carrier, tailnum, origin, dest, dep_time) %>%
  filter(n<1)

flights %>%
  select(dep_time) %>% 
  summarise_all(funs(sum(is.na(.))))

flights%>%
  select(carrier,time_hour,origin)%>%
  filter(Date > "2015-09-04" & Date <"2015-09-18")

tytyt<-flight %>%
  count(carrier,origin,dep_time,arr_time) %>%
  filter(between(time_hour, strptime('01/Jan/2013:00:00:00',format='%d/%b/%Y:%H:%M:%S'), time_hour <=strptime('31/Dec/2013:06:00:00',format='%d/%b/%Y:%H:%M:%S')))

flo12<-flights %>%
  select("carrier", "dep_time", "dep_delay", "tailnum")
  na.omit(dep_delay) %>%
  arrange(dep_delay()) %>%
  head()
flo12


library(tidyverse)
fli<-flights %>% drop_na(dep_delay)
ty<-arrange(flights[,c("dep_delay","carrier","tailnum")], desc(dep_delay))
tail(ty,n=15)

flo<-flights %>%
  na.omit(dep_delay) %>%
  arrange(dep_delay, tailnum, carrier) %>%
  head()