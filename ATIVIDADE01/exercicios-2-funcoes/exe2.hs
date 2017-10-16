tipotriangulo a b c
 |a == b  && b == c = "Triangulo Equilatero"
 |a /= b && a /= c && b /= c = "Triangulo Escaleno"
 |a == b || a == c || b == c = "Triangulo Isosceles"

 
main = do
 print (tipotriangulo 2 2 3)