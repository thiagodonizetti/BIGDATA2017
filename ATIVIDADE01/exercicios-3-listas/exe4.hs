fib = 1 : 2 : prox fib
 where 
    prox (x : t@(y:_)) = (x+y) : prox t

somafib = sum[x | x <- takeWhile(<= 4000000) fib, x `mod` 2 == 0]

main = do
 print(somafib)
   