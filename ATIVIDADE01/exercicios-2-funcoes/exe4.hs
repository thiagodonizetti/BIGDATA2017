ehprimo :: Integer -> Bool
ehprimo 0 = True
ehprimo 1 = True
ehprimo n = ehprimo' n 2
  where
    ehprimo' n d
       |d > n`div`2 = True
       |n `mod` d == 0 && n /= d = False
       |otherwise = (ehprimo' n (d+1))
     