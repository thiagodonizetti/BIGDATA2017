exe5 x = x < -1 || (x > 1 && x `mod` 2 == 0)

main = do
   print (exe5 1)