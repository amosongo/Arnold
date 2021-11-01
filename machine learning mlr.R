library(mlr)
library(tidyverse)
library(mclust)
library(ggplot2)
data("diabetes")
diabetesTib<-as_tibble(diabetes)
summary(diabetesTib)
ggplot(diabetesTib,aes(glucose, insulin, col = class))+
  geom_point()
ggplot(diabetesTib,aes(sspg, insulin, col = class))+
  geom_point()
ggplot(diabetesTib,aes(sspg, glucose, col = class))+
  geom_point()

##Task...
diabetesTask<-makeClassifTask(data = diabetesTib, target = 'class')#classification task
#diabetesTask<-makeRegrTask()#creating a regression task
#diabetesTask<-makeClusterTask()#clustering task
#diabetesTask<-makeSurvTask()#survival task

#define a learner/ algorithm (knn algorithm)
knn<-makeLearner("classif.knn",par.vals = list("k"=2))

#list of available MLR algorithms
listLearners()$class
listLearners("classif")$class#specify classification algoithms

#training the model
knnmodel<-train(knn,diabetesTask)

#testing performance (the bad way)
knnPred<-predict(knnmodel, newdata = diabetesTib)

performance(knnPred)#it gives the mean misclassification error 

#cross validation
#the data is split up into a training set: the data given to the algorithm to learn the model on, once the model has been learned
#on the traing set then the rest of the data is passed whih was not used n training the model; test set into the model and allow it 
#to make prediction on that data. its useful for estimating how the model will perform when given newdata.

#hold-out CV
#the data are randomly split into a training set and test set
#a model is trained using only the training set
#predictions are made on the test set
#the predictions are compared to the true values

#k-fold CV
#the data are randomly split k, near equally-sized folds
#each fold is used as the test set once, where the rest of the data make the training set
#for each fold, predictions are made on the test set
#the predictions are compared to the true values

#Leave-one-out CV Cross Validation
#use all of the data except a single case as the training set
#predict the value of the single test case
#repeat until every case has been the test case
#the predictions for each case are compared to the true values


kfold<- makeResampleDesc('RepCV', folds = 10, reps = 50)#RepCV, LOO, CV, HoldOut
kfoldCV<-resample(learner = knn, task = diabetesTask,
                  resampling = kfold)
calculateConfusionMatrix(kfoldCV$pred)#to get a better idea on which classes our model is misclassifying more frequently
