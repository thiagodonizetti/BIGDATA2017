matrizID n = [[if(y == x) then 1 else 0 | x <- [1.. n]] | y <- [1.. n]]

diagP m = zipWith (!!) m [0..]

somaDiag m = sum $ diagP m

main = do
 let m = matrizID 6
 print (somaDiag m)
 
 