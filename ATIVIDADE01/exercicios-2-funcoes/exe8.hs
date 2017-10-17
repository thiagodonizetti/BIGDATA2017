coefBin n k = fatorial n `div` ( (fatorial k) * fatorial(n-k))

fatorial :: Integer -> Integer
fatorial 0 = 1
fatorial 1 = 1
fatorial n = fatorial' n 1
   where 
     fatorial' n r
       |n == 1 = r
       |otherwise = fatorial' (n-1) (n*r)

 

trianguloPascal i j
  |j > i + 1 = error "Indices invalid"
  |otherwise = if j > i`div`2 then coefBin (i) (abs(j-i)) else coefBin i j
  
  

  
main = do
 print (trianguloPascal 10 6)