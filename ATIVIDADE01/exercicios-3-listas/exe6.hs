collatz x
 | even x =  fromInteger x`div`2
 | otherwise = 3*x+1
 
main = do
   print (collatz 2)