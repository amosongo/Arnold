library(randomForest)
data("iris")
str(iris)
table(iris$Species)

#data partitioning
set.seed(123)#random sed enables this analysis to be repeateable
ind<- sample(2, nrow(iris), replace = T, prob = c(0.7, 0.3)) # partitioning the data into 70/ 30
traindata<-iris[ind==1,]
testdata<- iris[ind==2,]

#RandomForest
library(randomForest)
set.seed(222)
attach(iris) 
rf<-randomForest(Species~.,data = traindata, 
                 ntree = 200,
                 mtry = 2,
                 importance=T,
                 proximity=T)
print(rf)
attributes(rf)
rf$confusion

#prediction & confusion matrix - train data
library(caret)
pred1<-predict(rf, traindata)
head(pred1)
head(traindata$Species)
confusionMatrix(pred1, traindata$Species)

#prediction & confusion matrix - test data
pred2<-predict(rf, testdata)
confusionMatrix(pred2, testdata$Species)

#Error rate of Random Forest
plot(rf)

#Tune mtry
t<-tuneRF(traindata[, -4], traindata[,5],
       stepFactor = 1,
       plot = T,
       ntreeTry = 200,
       trace = T,
       improve = 0.05)

#No. of nodes for the trees
hist(treesize(rf), main = "No. of nodes for the trees",
     col = 'green')

#Variable importance
varImpPlot(rf)
varImpPlot(rf,
           sort = T,
           n.var = 3,
           main = 'Random Forest var importance')
importance(rf)#quantittive values
varUsed(rf)#finds which preditrs are actually used
#partial dependece plot, they show given a var what prediction class of the pred values
partialPlot(rf, traindata, Petal.Length, 'setosa')
partialPlot(rf, traindata, Petal.Length, 'versicolor')
partialPlot(rf, traindata, Petal.Length, 'virginica')

#Extract Single tree
getTree(rf, 1, labelVar = T)

#Multidimensional scalling plot of proximity matrix
MDSplot(rf, traindata$Species)
