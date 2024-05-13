print("hello R")
m = "Hii"
print(m)

choice =3
x <- switch(choice,
            "one",
            "two",
            "three"
            )
print(x)


y = c("TRUTH","HELLO","WHTA")
if("TRUTH" %in% y){
  print("Truth is found")
} else {
  print("Truth is not found")
}




choice = 2
x <- switch(choice,
            "1" = "First",
            "3" = "second",
            "5"="third",
            "4" = "fourth"
)
print(x)

v1 <- 10
v2 <- 20
print(v1,v2)
cat(v1,v2)





x <- list(1, "a", c(1,2,3), 1+4i)
x[2]
x[[2]]


student = factor(c(1,2,2,2,1,1,2), ordered = TRUE, levels = c(2,1), labels = c("she","he"))
student

as.numeric(student)
num = as.numeric(student)
num
1+num



val<-factor(c("r1","r2","r1","r2","r2","r3","r1"),ordered = TRUE,levels = c("r3", "r2","r1"), labels = "h",'a','n')
val

as.numeric(val)




x <- 1:10 # range operator special behavior as dtypes integer
class(x)
x <- as.list(x)
x
class(x)



print(3:12)
print(8.5:4.5)
print(-12:1)
print(c(1, 1:3, c(5, 8), 13))

print(10.45:5)
a = c(10:20)
a



print(seq.int(3, 12))
print(seq.int(3, 12, 0.5))
print(seq.int(0.1, 0.01, -0.01))
print(seq.int(2,100,2))
print(seq.int(99,90,-2))



print(seq_len(10))

print(seq.int(10,20))


v = c(45,56,66,34,23,100,450)
print(v)
seq_along(v)
print(seq_len(length(v)))

v = 10
print(seq_along(10))


print(seq_len(10))


v = c(45,56,66,34,23,100,450)
print(v)
seq_along(v)

print(seq_len(v))

rep(1:5, 3)

M <- matrix(c(3:14), nrow = 4)
print(M)
