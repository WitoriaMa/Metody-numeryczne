x<-1:7
y<-40 + 10*x + 5*x^2 + 3*x^3 + 2*x^4 + x^5 + x^6
fit<-lm(y ~ poly(x, 6, raw = TRUE))
x1<-seq(1, 7, length.out = 200)
y1<-predict(fit, newdata = data.frame(x = x1))
plot(x, y, pch = 19, col = "black",
     main = "Aproksymacja wielomianem 6 stopnia",
     xlab = "x", ylab = "y")
lines(x1, y1, col = "red", lwd = 2)


x <- 1:10
y <- 40 + 10*x + 5*x^2 + 3*x^3 + 2*x^4 + x^5 + x^6
fit <- lm(y ~ poly(x, 6, raw = TRUE))
x1<- seq(1, 10, length.out = 200)
y1 <- predict(fit, newdata = data.frame(x = x1))
plot(x, y, pch = 19, col = "black",
     main = "Aproksymacja wielomianem 6 stopnia",
     xlab = "x", ylab = "y")
lines(x1, y1, col = "red", lwd = 2)
#jest gorzej
