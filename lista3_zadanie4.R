pdf("zadanie4_l3.pdf", width = 8, height = 6)
f <- function(x) 1/(1+25*x^2)
x<-seq(-1, 1, length.out = 500)
y<-f(x)
plot(x, y, type = "l", lwd = 3, col = "black",
     main = "Interpolacja wielomianem sklejanym dla f(x)=1/(1+25x^2)",
     xlab = "x", ylab = "y")
for (n in 1:20) {
  plot(x, y, type = "l", lwd = 2, main = paste("Interpolacja wielomianem sklejanym, stopień", n),  xlab = "x", ylab = "y")
  x1 <- seq(-1, 1, length.out = n)
  y1 <- f(x1)
  sp <- spline(x1, y1, xout = x)
  lines(sp$x, sp$y, col = n)
}

dev.off()

