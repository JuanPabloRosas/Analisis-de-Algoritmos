file <- read.csv('archivo2.txt', sep = ' ', header= FALSE)
plot(file$V1,file$V2, xlim=c(0,1), ylim=c(0,1))
points(file$V3,file$V4)
segments(file$V1, file$V2, file$V3, file$V4)

