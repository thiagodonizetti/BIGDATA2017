matrizID n = [[if(y == x) then 1 else 0 | x <- [1.. n]] | y <- [1.. n]]

main = do
 print (matrizID 3)