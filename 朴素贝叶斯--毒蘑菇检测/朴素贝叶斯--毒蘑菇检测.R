rm(list = ls())

if(!suppressWarnings(require('klaR'))){
  install.packages('klaR')
  require('klaR')
}

if(!suppressWarnings(require('pROC'))){
  install.packages('pROC')
  require('pROC')
}

require('caret')
library('caret')

mydata <- read.csv("/Users/passionlk/Documents/MSBA/MyCode/朴素贝叶斯--毒蘑菇检测/mushrooms.csv")

str(mydata)
summary(mydata)


set.seed(12)
index <- sample(1:nrow(mydata), size = 0.75*nrow(mydata))
train <- mydata[index,]
test <- mydata[-index,]


prop.table(table(mydata$type))
prop.table(table(train$type))
prop.table(table(test$type))


rfeControls_rf <- rfeControl(functions = rfFuncs,method = 'cv',repeats = 5)

				
fs_nb <- rfe(x = train[,-1],
             y = train[,1],
             sizes = seq(4,21,2),
             rfeControl = rfeControls_rf)
fs_nb
plot(fs_nb, type = c('g','o'))
fs_nb$optVariables


vars <- c('type',fs_nb$optVariables)
fit <- NaiveBayes(type ~ ., data = train[,vars])
fit

pred <- predict(fit, newdata = test[,vars][,-1])
head(pred$class)


freq <- table(pred$class, test[,1])
freq


accuracy <- sum(diag(freq))/sum(freq)
accuracy


modelroc <- roc(as.integer(test[,1]), 
                as.integer(factor(pred$class)))
plot(modelroc, print.auc = TRUE, auc.polygon = TRUE, 
     grid = c(0.1,0.2), grid.col = c('green','red'),
     max.auc.polygon = TRUE, auc.polygon.col = 'steelblue')


