rm(list =ls())


dnorm(x=c(10, 20, 30), mean = 124, sd=20)
curve(dnorm(x,   mean = 124, sd=20), xlim =c(0, 200))
abline( v = 124 )
barplot(dbinom(x=0:5,size =5, prob=0.4))
barplot(dbinom(x=0:5,size =5, prob=0.4),names.arg = 0:5, xlab = 'x', ylab = 'y')


pnorm(q=90, mean = 124, sd=20, lower.tail = TRUE)
?abline
abline(v=124, lty=2)

??lower.tail
