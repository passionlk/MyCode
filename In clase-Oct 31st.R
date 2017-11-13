IQ <- pnorm(q=130,mean = 100,sd = 15, lower.tail = FALSE)

qnorm(0.15,mean = 100,sd = 15, lower.tail = FALSE)
qnorm(0.85,mean = 100,sd = 15, lower.tail = FALSE)

dunif(10,min = 0, max = 100, log = FALSE)

curve(1/2pi, exp(-x^2/2), xlim = c(-1, 1))       ##Standard Normal Distribution

x<- runif(1000)
x
plot(density(x))
hist(x)
mean(x)
mean(sample(x,50))
mean(sample(x,50))
mean(sample(x,50))

x_bar <- matrix(0,nrow = 300)
for (k in 1:300) {x_bar[k] <- mean(sample(x,15))}
hist(x_bar)
mean(x_bar)
mean(x)
sd(x_bar)/ sqrt(15)


y <- rnorm(100000)
hist(y)
hist(100*y)
hist(100*y +10000)
x <- rnorm(10000)

z <- 10*x + 20*y + 3
hist(z)

################################################################
library(nutshell)
data("dow30")
mean(dow30$Open)
quantile(dow30$Open,probs = c(0,0.25,0.5,0.75,1.0))

summary(dow30)

plot(dnorm, -3, 3, main = "Normal Distribution")

plot(pnorm,-3,3,main = "Cumulative Normal Distribution")
pnorm(-1)
pnorm(1.96, lower.tail = TRUE) - pnorm(-1.96, lower.tail = TRUE)

plot(dbinom(1:100,100,0.3), main = "I love Senceliya, FOREVER")
?dbinom

       