divisivel20 x
 |b > 0 = True
 |otherwise = False
  where b = length . filter (>0) $ (map (1 `mod`) [1..20])