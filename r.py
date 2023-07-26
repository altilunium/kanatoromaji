import cutlet
import pyperclip
katsu = cutlet.Cutlet()
print("kanatoromaji v23.7.26")

while True:
	i = input(">: ")
	o = katsu.romaji(i)
	pyperclip.copy(o)
	print(o)
