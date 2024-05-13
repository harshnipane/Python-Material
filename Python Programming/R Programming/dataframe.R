df=readf = read.csv("76_attributes_heartdiseases.csv")
summary(df)
df


df1=readf = read.csv("sample1.txt" ,sep ="|")
df1
summary(df1)

df1=readf = read.csv("sample2.txt" ,skip=2,sep ="|")
df1

df1=readf = read.csv("sample2.txt" ,skip=1,sep ="|")


mtcars.head(10)

head(mtcars)

mtcars[mtcars$mpg > 20,]
mtcars[mtcars$cyl > 4,]

mtcars[mtcars$mpg > 20,c('mpg')]


mtcars[mtcars$hp > 100, c('cyl')]


mtcars[(mtcars$mpg > 20) & (mtcars$cyl != 6), c('wt','cyl','mpg')]


mtcars[(mtcars$cyl > 6) & (mtcars$mpg > 15), c('hp')]

mtcars[(mtcars$cyl > 4)& (mtcars$mpg !=14), c('hp')]

head(iris)



M1 = matrix(c(1234,2235,67,85),nrow=2)
m1_df <- as.data.frame(M1)
colnames(m1_df) = c('roll_no','marks_mod1')
m1_df


M2 = matrix(c(1234,2235,75,68),nrow=2)
m2_df <- as.data.frame(M2)
colnames(m2_df) = c('roll_no','marks_mod2')
m2_df


merge(m1_df,m2_df,by = "roll_no")
