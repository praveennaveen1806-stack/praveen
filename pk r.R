study<-data.frame(
  student<-paste("s",1:10,sep=""),
  study_hours=c(1,2,2.5,3,4,5,6,6.5,7,8),marks=c(35,40,45,50,60,68,75,78,85,92),
)
study
sum(study$marks)/10
barplot(study$study_hours,study$marks,type="b",lwd="5",col="blue",main="mark progression")
