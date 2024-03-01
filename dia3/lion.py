from PIL import Image

# Abra a imagem
# imagem = Image.open('leao.jpg')
imagem = Image.open('/home/v/Desktop/Bike./dia3/Leão.jpg')

# Converta para escala de cinza
imagem_pb = imagem.convert('L')

# Salve a imagem em preto e branco
imagem_pb.save('/home/v/Desktop/Bike./dia3/Leão.jpg')

#print("Imagem em preto e branco salva com sucesso!")
