listaInt x = map (read . (:"")) x :: [Int]

somaDigitos n = sum $ listaInt $ show n
main = do
  print (somaDigitos 123)