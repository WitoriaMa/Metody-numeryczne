library(polynom)
set.seed(111)
f <- function(x) abs(x)
x_grid <- seq(from = -1, to = 1, length.out = 200)

pdf("wykresy_zadanie_3_2-lab.pdf", width = 8, height = 6)
kolory <- rainbow(20)
for (n in 1:20) {
  plot(x_grid, f(x_grid), col = "black", type = "l", lwd = 2, 
       main = paste("Interpolacja wielomianowa - stopień", n), 
       xlab = "x", ylab = "y")
  x<-seq(-1, 1, length.out = n + 1)
  y<-f(x)
  
  p<-poly.calc(x, y)
  p_f<-as.function(p)
  curve(p_f, from = -1, to = 1, add = TRUE, col = kolory[n], lwd = 2)
  legend("topright", legend = c("f(x) = 1/(1+25x^2)", paste("Wielomian st.", n)), 
         col = c("black", kolory[n]), lty = 1, lwd = 2, bty = "n")
}

dev.off()
print("Utworzono PDF")
