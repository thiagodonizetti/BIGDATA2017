bissexto = [ i | i <- [1..2017], ehbissexto i]
ehbissexto x = x `rem` 400 == 0 || (x `rem` 4 == 0 && x `rem` 100 /= 0)

main = do
   let metade = length bissexto `div` 2
   print ((take metade bissexto, drop metade bissexto))