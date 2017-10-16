collatz x
 | even x =  fromInteger x`div`2
 | otherwise = 3*x+1

applyCollatz x
 |x == 1 = []
 |collatz x == 1 = [1]
 |otherwise = collatz x : applyCollatz (collatz x)

collatzLen x = length $ applyCollatz x


maxColl  = maximum[collatzLen i | i<- [1..1000000]]

main = do
  print maxColl