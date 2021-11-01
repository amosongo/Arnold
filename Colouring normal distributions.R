Study_hours<-c(0,2,4,5,5,6,7)
Score<-c(32,55,72,80,82,93,98)
study<-data.frame(Score,Study_hours)
plot(Score,Study_hours)
p<-lm(Score~Study_hours, data=study)
summary(p)

meani=157
sdi=15
lb=8000
x<-seq(-4,4,length = 100)*sdi + meani
hx<-dnorm(x,meani,sdi)
plot(x,hx, type = "n", xlab = "box weight",ylab="", main = "Normal distribution", axes = F)
i<- x>lb
lines(x,hx)
polygon(c(lb,x[i]),c(0,hx[i]), col = "red")
area<-pnorm(lb,meani,sdi)
result<-paste("P( weight = ", signif(area, digits = 3))
mtext(result, 3)
axis(1, at=seq(40, 460, 20), pos = 0)


mu<-32.4
sig<-4.863
xi<-160
x<-seq(mu-3.5*sig,mu+3.5*sig,length.out = 100)
p_x<-dnorm(x,mean=mu,sd=sig)
plot(x,p_x,type="l", xlab = "Accidents", ylab ="")
box<-qnorm(0.05, mean = mu, sd=sig)
x<-seq(box,157, length.out = 50)
xx<-c(box,x,157)
px<-c(0,dnorm(x,mean=mu, sd=sig),0)
polygon(xx, px, col = "red")
text(x=box+25, y=0.002, labels=paste("box = ", round (box,1), "%"))

mu<-157
sig<-15
xi<-160
x<-seq(mu-3.5*sig,mu+3.5*sig,length.out = 100)
p_x<-dnorm(x,mean=mu,sd=sig)
plot(x,p_x,type="l", xlab = "Weights", ylab ="")
box<-qnorm(0.58, mean = mu, sd=sig)
x<-seq(box,mu+3.5*sig, length.out = 50)
xx<-c(box,x,mu+3.5*sig)
px<-c(0,dnorm(x,mean=mu, sd=sig),0)
polygon(xx, px, col = "red")