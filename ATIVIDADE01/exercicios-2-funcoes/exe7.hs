coefBin n k = fatorial n `div` ( (fatorial k) * fatorial(n-k))

fatorial :: Integer -> Integer
fatorial 0 = 1
fatorial 1 = 1
fatorial n = fatorial' n 1
   where 
     fatorial' n r
       |n == 1 = r
       |otherwise = fatorial' (n-1) (n*r)

 

main = do
 print (coefBin 10 6)