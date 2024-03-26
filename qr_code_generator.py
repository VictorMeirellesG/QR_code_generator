import qrcode

def generate_qr_code(link, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")
    image.save(file_name)

link = ""
file_name = ""

generate_qr_code(link, file_name)