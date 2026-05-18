set.seed(123)
n <- 500
A <- matrix(runif(n*n), n, n)
A[n, ] <- A[n-1, ] + 10**(-8)
x1<- rep(1, n)
b <- A %*% x1
x <- solve(A, b)
x
r <- A %*% x - b
dim(r)
r
# norma<-sqrt(sum(r^2))
# norma
?solve

