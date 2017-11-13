library(MASS)
library(ISLR)

#读取Boston 数据集
fix(Boston)
names(Boston)
attach(Boston)

#用lm()函数拟合一个简单线性回归模型
lm.fit = lm(medv~lstat, data = Boston)
lm.fit
summary(lm.fit)
#取得系数估计值的置信区间
confint(lm.fit)

#给定lstat值之后预测medv值时的置信区间和预测区间
predict(lm.fit, data.frame(lstat =(c(5,10,15))),interval = "confidence")

predict(lm.fit, data.frame(lstat =(c(5,10,15))),interval = "prediction")

#绘制medv,lstat的散点图和最小二乘回归直线
plot(lstat,medv,pch = '+')
abline(lm.fit)
abline(lm.fit,lwd=3,col ='red')

#多元线性回归
lm.fit = lm(medv~lstat+age, data = Boston)
summary(lm.fit)
#快速与所有的预测变量进行回归
lm.fit = lm(medv~., data = Boston)
summary(lm.fit)

#预测变量的非线性变化
#建立medv对lstat和lstat^2的回归函数，从结果可以看到p值有了很大的改善
lm.fit2 = lm(medv~lstat+I(lstat^2))
summary(lm.fit2)

lm.fit = lm(medv~lstat, data = Boston)
anova(lm.fit,lm.fit2)

#5阶多项式拟合--poly()函数
lm.fit5=lm(medv~poly(lstat,5))
summary(lm.fit5)

#定性预测变量
fix(Carseats)
names(Carseats)

#构建含有交互项的多元回归模型
lm.fit = lm(Sales~.+Income:Advertising+Price:Age,data = Carseats)
summary(lm.fit)

attach(Carseats)
contrasts(ShelveLoc)  #返回R虚拟变量的编码

fix(Auto)





