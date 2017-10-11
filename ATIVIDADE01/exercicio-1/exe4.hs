mult35 x = x `mod` 3 == 0 && x `mod` 5 == 0

main = do
   print (mult35 5)