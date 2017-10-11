mult3 x = x `mod` 3 == 0

main = do
	print (mult3 9)