listaInt x = map (read . (:"")) x :: [Int]

somaDigitos n = sum $ listaInt $ show n

persistencia n
  |n < 10 = 0
  |otherwise = fazSoma (1) (somaDigitos n)
    where
      fazSoma count soma
        |soma < 10 = count
        |otherwise = fazSoma (count+1) (somaDigitos soma)
  
  
  
main = do
  print (persistencia 923)