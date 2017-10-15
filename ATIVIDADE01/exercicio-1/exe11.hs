concatStrings s t = s ++ ' ' : t

main = do
  print (concatStrings "ola" "mundo")