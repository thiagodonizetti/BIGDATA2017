divisivel20 x
 |b > 0 = False
 |otherwise = True
  where b = length . filter (>0) $ (map (x `mod`) [1..20])