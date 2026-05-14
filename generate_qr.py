import qrcode
import os

# URL do cartão de visitas virtual (GitHub Pages)
url = "https://fabio-sichineli-analista.github.io/business-card/"

# Configuração do QR Code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Criar a imagem com cores personalizadas (preto e dourado aproximado)
img = qr.make_image(fill_color="#D4AF37", back_color="black")
img.save("/home/ubuntu/business-card/assets/qrcode.png")

print(f"QR Code gerado com sucesso para: {url}")
