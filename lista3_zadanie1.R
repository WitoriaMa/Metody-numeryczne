
pdf("zadanie1(2)_l3.pdf", width = 8, height = 6)
x <- seq(-1, 1, length.out = 200)
y <- abs(x)

plot(x, y, type="l", lwd=2)

for (n in 1:20) {
  plot(x, y, type = "l", lwd = 2,
       main = paste("Aproksymacja |x|, stopień", n),
       xlab = "x", ylab = "y")
  fit <- lm(y ~ poly(x, n, raw=TRUE))
  lines(x, predict(fit), col=n)
}
dev.off()

