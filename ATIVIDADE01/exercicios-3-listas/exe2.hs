divisivel20 x
 |b > 0 = False
 |otherwise = True
  where b = length . filter (>0) $ (map (x `mod`) [1..20])

div20 x
 |divisivel20 x = x
 |otherwise = div20 (x+1)
 
main = do
 print(div20 1)