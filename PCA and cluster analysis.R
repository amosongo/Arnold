data(iris)
attach(iris)

#principal component analysis
mypr<-prcomp(iris[,-5], scale = T)
summary(mypr)
plot(mypr, type = "l")
biplot(mypr, scale = 0)

#extracting components
str(mypr)
mypr$x
iris2<-cbind(iris,mypr$x[,1:2])
head(iris2)

#ploting using ggplot
library(ggplot2)
ggplot(iris2, aes(PC1, PC2, col = Species, fill = Species))+
  stat_ellipse(geom = 'polygon', col = 'black', alpha=0.5)+
  geom_point(shape = 21, col = 'black')

#correlation btwn var and principal comp
cor(iris[,-5], iris2[,6:7])


# cluster analysis kmeans, hirechial, clustering based n statistical models and density based clustering
#scaling data... normalizes the data by subtracting mean / standard dev
irisScaled<-scale(iris[,-5])
head(irisScaled)

#kmeans clustering 
fitk<-kmeans(irisScaled, 3)
fitk
str(fitk)
plot(iris)
plot(iris, col =fitk$cluster)
#choosing k
k<-list()
for (i in 1:10){
  k[[i]]<-kmeans(irisScaled, i)
}
k
betweenss_totss <- list()
for (i in 1:10) {
  betweenss_totss[[i]]<-k[[i]]$betweenss/ k[[i]]$totss
}

plot(1:10, betweenss_totss, type = 'b', 
     ylab = 'betweenss/ total ss', xlab = 'clusters k')# select the shoulder part of the plot

for(i in 1:4){
  plot(iris, col = k[[i]]$cluster)
}

#hirechical clustering
d<- dist(irisScaled)
?hclust
fitH<- hclust(d, 'ward.D2')
plot(fitH)

#visualize cutting of the tree
rect.hclust(fitH, k=3, border='red')
clusterss<-cutree(fitH, 3)
clusterss
plot(iris, col = clusterss)

#model based clustering: gives no flexibility to the no. of clusters selected or how group membership is assigned
library(mclust)
fitM<- Mclust(irisScaled)
plot(fitM)

#density based clustering, it identifie dense regions in the observations and uses that information to assign clusters
library(dbscan)
kNNdistplot(irisScaled, k = 3)# look for the elbow on the far right of the plot corresponding to the y axis
abline(h=0.7, col='red', lty=2)
fitD<- dbscan(irisScaled, eps = 0.7, minPts= 5)
fitD
plot(iris, col= fitD$cluster)
