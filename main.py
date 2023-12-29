import qrcode
import os

def generate_qr_code(data, folder_path):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    file_name = data.replace('://', '_').replace('/', '_') + ".png"
    file_path = os.path.join(folder_path, file_name)
    img.save(file_path) 

folder_path = "qr_codes" 
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

while True:
    url = input("Введите ссылку (для выхода введите 'exit'): ")
    if url.lower() == 'exit':
        break
    generate_qr_code(url, folder_path)
    print(f"QR-код для '{url}' сохранен в папке '{folder_path}'")