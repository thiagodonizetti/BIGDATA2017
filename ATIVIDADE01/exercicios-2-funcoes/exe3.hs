multEtiope :: Integer -> Integer -> Integer
multEtiope 1 x = x
multEtiope y 1 = y
multEtiope 0 _ = 0
multEtiope _ 0 = 0
multEtiope m n = multEtiope' m n 0
   where 
       multEtiope' m n r
         |m == 1 = n + r
         |odd m = multEtiope' (m`div`2) (n*2) (r+n)
         |otherwise = multEtiope' (m`div`2) (n*2) r
		 
main = do
   print (multEtiope 14 12)