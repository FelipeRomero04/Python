import qrcode

codeqr = qrcode.QRCode(
    version= 1, #tamanho do qrcode
    error_correction=qrcode.ERROR_CORRECT_M, #Corrije possiveis erros
    border=4,
    box_size=10
) 

codeqr.add_data('youtube.com')
codeqr.make(fit=True)

img = codeqr.make_image(fill_color='yellow', back_color='white')
img.save('png.save')

