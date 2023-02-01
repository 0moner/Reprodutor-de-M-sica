import pygame
pygame.init()

print('escolha uma opção :')

print('-=' * 15)

print('''[ 1 ] Opção 1
[ 2 ] Opção 2
[ 3 ] Opção 3 
[ 4 ] Opção 4''')

print('-=' * 15)

opção = int(input('escolha uma opção > '))

if opção == 1:
    pygame.mixer.music.load('suamusica.mp3')

elif opção == 2:
     pygame.mixer.music.load('suamusica2.mp3')
    
elif opção == 3:
    pygame.mixer.music.load('suamusica3.mp3')

elif opção == 4:
    pygame.mixer.music.load('suamusica4.mp3')

else:
    print('Opção inválida ...')

pygame.mixer.music.play()

input('Curte o som ae meu bom!')
