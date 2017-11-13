###########################
#Logistics Regression Test#
###########################

library(ISLR)
names(Smarket)
summary(Smarket)
attach(Smarket)
plot(Volume)


#cor()计算预测变量两两之间相关系数 
#因为Direction变量是定性的，所以必须把这一列减掉
cor(Smarket[,-9])

#用广义线性模型glm预测Direction
glm.fit = glm(Direction ~ Lag1+Lag2+Lag3+Lag4+Lag5+Volume, data = Smarket,family = binomial)
summary(glm.fit)
glm.probs = predict(glm.fit,type = "response")
glm.probs[1: 10]

contrasts(Direction)

coef(glm.fit)

#预测市场给定变量值下市场上涨的概率
glm.probs = predict(glm.fit,type = 'response')
glm.probs[1:10]

#先创建1250个Down元素组成的向量，再将>0.5的转变为Up
glm.pred = rep('Down', 1250)
glm.pred[glm.probs > 0.5] ='Up'

#使用table()函数观察正确预测的天数比例
table(glm.pred,Direction)

mean(glm.pred != Direction)

train= (Year<2005)
Smarket.2005 =Smarket[!train,]
Direction.2005 = Direction[!train]
#如果只使用Lag1,Lag2 来进行预测，则准确率提高到56%
glm.fit = glm(Direction~Lag1+Lag2, data = Smarket,family = binomial,subset = train)
glm.probs = predict(glm.fit, Smarket.2005, type = 'response')
glm.pred = rep('Down',252)
glm.pred[glm.probs>0.5] = 'Up'
table(glm.pred,Direction.2005)
mean(glm.pred != Direction.2005)

################################
# Linear Regression Test(LDA)  #
################################

# lda()在MASS函数包中
library(MASS)
lda.fit= lda(Direction~Lag1+Lag2, data = Smarket, subset = train)
lda.fit

plot(lda.fit)

lda.pred = predict(lda.fit,Smarket.2005)
names(lda.pred)
lda.class = lda.pred$class
table(lda.class, Direction.2005)



###################
# KNN Algorithm   #
###################

#knn()算法储存在class 库中
#以下先生成训练集和测试集
library(class)
train.X = cbind(Lag1, Lag2)[train ,]  #train已经定义为2005年以前的数据
test.X = cbind(Lag1, Lag2)[!train,]
train.Direction = Direction[train]

set.seed(8)
knn.pred = knn(train.X,test.X, train.Direction, k=1)
table(knn.pred,Direction.2005)

#使用更高的K值，让函数不那么光滑，提高预测准确性
set.seed(8)
knn.pred = knn(train.X,test.X, train.Direction, k=3)
table(knn.pred,Direction.2005)

#Caravan(大篷车)保险数据的应用
dim(Caravan)
attach(Caravan)
summary(Purchase)

#为解决数据量度不一致的问题，首先将所有的数据进行标准化
standardized.X = scale(Caravan[,-86]) #第86列为定性数据Purchase,注意排除

var(standardized.X[,1]) #测试标准化后的数据，标准差为1

#将前1000个观测设置为测试集，其余设置为训练集
test = 1:1000
train.X = standardized.X[-test, ]
test.X = standardized.X[test, ]
train.Y = Purchase[-test]
test.Y = Purchase[test]

set.seed(8)
knn.pred = knn(train.X,test.X, train.Y, k=1)
mean(test.Y != knn.pred)  #直接可以用mean()函数求两个数组之前逻辑运算的"比率"
mean(test.Y != 'No')      #直接可以用mean()函数求数组值逻辑运算的"比率"

#作为比较，对数据做逻辑斯蒂回归预测
glm.fit = glm(Purchase~., data = Caravan, family = binomial, subset=-test)
glm.probs=predict(glm.fit,Caravan[test ,], type = 'response')
glm.pred=rep('No', 1000)
glm.pred[glm.probs>0.5] = 'Yes'
table(glm.pred,test.Y)

glm.pred=rep('No', 1000)
glm.pred[glm.probs>0.25] = 'Yes'
table(glm.pred,test.Y)






