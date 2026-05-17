pdf("zadanie3_l3.pdf", width = 8, height = 6)
f <- function(x) abs(x)
x<-seq(-1, 1, length.out = 500)
y<-f(x)
plot(x, y, type = "l", lwd = 3, col = "black",
     main = "Interpolacja wielomianem sklejanym dla |x|",
     xlab = "x", ylab = "y")
for (n in 1:20) {
  plot(x, y, type = "l", lwd = 2, main = paste("Interpolacja wielomianem sklejanym"),  xlab = "x", ylab = "y")
  x1 <- seq(-1, 1, length.out = n)
  y1 <- f(x1)
  sp <- spline(x1, y1, xout = x)
  lines(sp$x, sp$y, col = n)
}

dev.off()
