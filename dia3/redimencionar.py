from PIL import Image

# Abra a imagem
# imagem = Image.open('sua_imagem.jpg')
imagem = Image.open('/home/v/Desktop/Bike./dia3/Leao.jpg')

# Obtenha as dimensões da imagem
largura, altura = imagem.size

# Imprima as dimensões
print("Largura da imagem:", largura)
print("Altura da imagem:", altura)
