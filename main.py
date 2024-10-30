import os
from PIL import Image, ImageEnhance

def upscale_images_in_folder(folder_path, output_folder):
    # Buat folder output jika belum ada
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Ekstensi gambar yang didukung
    supported_formats = ('.png', '.jpg', '.jpeg', '.jfif', '.webp')

    # Loop untuk semua file di folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Cek apakah file adalah gambar dengan format yang didukung
        if os.path.isfile(file_path) and filename.lower().endswith(supported_formats):
            try:
                # Buka gambar
                img = Image.open(file_path)

                # Dapatkan ukuran gambar
                width, height = img.size

                # Cek jika lebar gambar adalah 1024px
                if width == 1024:
                    # Upscale gambar menjadi 2048px (bisa atur sendiri)
                    new_size = (2048, int(2048 * height / width))
                    upscaled_img = img.resize(new_size, Image.Resampling.LANCZOS)

                    # Meningkatkan kualitas gambar (contoh: meningkatkan kontras)
                    enhancer = ImageEnhance.Contrast(upscaled_img)
                    enhanced_img = enhancer.enhance(1.5)  # Meningkatkan kontras 1.5x

                    # Simpan gambar di folder output sebagai .jpeg
                    output_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpeg")
                    enhanced_img.convert('RGB').save(output_path, format='JPEG', quality=95)
                    print(f"{filename} berhasil di-upscale dan disimpan sebagai JPEG.")
                else:
                    print(f"{filename} tidak berukuran 1024px, dilewati.")
            except Exception as e:
                print(f"Error saat memproses {filename}: {e}")

# Folder input dan output (atur sesuai folder yang ada)
folder_input = 'input'
folder_output = 'output'

# Panggil fungsi untuk upscale gambar
upscale_images_in_folder(folder_input, folder_output)
