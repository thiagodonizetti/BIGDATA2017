ehtriangulo a b c 
 |abs(b - c) < a  && a < (b + c) = "Triangulo"
 |abs(a - c) < b  && b < (a + c) = "Triangulo"
 |abs(a - b) < c  && c < (a + b) = "Triangulo"
 |otherwise = "Nao"
 
main = do
 print (ehtriangulo 1 2 3)
 
 
 

