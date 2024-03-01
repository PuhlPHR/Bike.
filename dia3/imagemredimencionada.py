from PIL import Image

# Abra a imagem
#imagem = Image.open('sua_imagem.jpg')
imagem = Image.open('/home/v/Desktop/Bike./dia3/Leao.jpg')

# Especifique as dimensões desejadas para a imagem reduzida
largura_desejada = 375
altura_desejada = 215

# Redimensione a imagem
imagem_redimensionada = imagem.resize((375, 215), Image.ANTIALIAS)

# Salve a imagem redimensionada
imagem_redimensionada.save('leao_redimensionada.jpg')

print("Imagem redimensionada salva com sucesso!")

