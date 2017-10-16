matrizID n = [[if(y == x) then 1 else 0 | x <- [1.. n]] | y <- [1.. n]]

diagS m = zipWith (!!) m [length m-1, length m-2.. ]

somaDiag m = sum $ diagS m

main = do
 let m = matrizID 3
 print (somaDiag m)
 
 