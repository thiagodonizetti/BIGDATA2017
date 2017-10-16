produtoescalar (vx, vy, vz) (wx, wy, wz) = vx * wx + vy * wy + vz * wz


main = do
   print( produtoescalar (1,2,3) (2,3,1))