listaInt x = map (read . (:"")) x :: [Int]


main = do
 print (listaInt "0123456789")