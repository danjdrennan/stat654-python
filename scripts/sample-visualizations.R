N <- 100000
# Going to construct two face time series
x <- numeric(N)
y <- numeric(N)

x[1] <- rnorm(1, 0, 5)
y[1] <- rnorm(1, 0, 5)
for(t in 2:N){
    x[t] <- 0.5 * x[t - 1] + rnorm(1, 0, 0.25)
    y[t] <- 0.6 * y[t - 1] + rnorm(1, 0, 1.2)
}

# Plot traceplots
par(mfrow = c(2, 1))
plot(x, type = 'l')
plot(y, type = 'l')

# Plot ACF plots
par(mfrow = c(1, 2))
acf(x)
acf(y)

# Plot histograms
# Thin chains appropriately based on the ACF plot
# The ACF plot shows autocorrelation to about seven samples,
# so taking any subset of the chain which skips at least seven
# samples will suffice to make independent samples.
par(mfrow = c(1, 2))
hist(x[10 * 1:(N/10)], bins = 30, main = "x")
hist(y[10 * 1:(N/10)], bins = 30, main = "y")

# Generate a subsequence for thinning the chain
subseq <- seq(from=100, to = N, 10)
subseq

# Or plot densities instead
par(mfrow = c(1, 2))
plot(density(x[subseq]), main = "x")
plot(density(y[subseq]), main = "y")

# Compute the mean of the posterior samples (after thinning and burning in)
mean(x[subseq])
mean(y[subseq])
