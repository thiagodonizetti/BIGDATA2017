bissexto = [ i | i <- [1..2017], ehbissexto i]
ehbissexto x = x `rem` 400 == 0 || (x `rem` 4 == 0 && x `rem` 100 /= 0)