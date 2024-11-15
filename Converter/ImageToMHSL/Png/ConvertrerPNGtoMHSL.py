from PIL import Image
import colorsys

def png_to_pixel_data(image_path, output_file="pixel_data.txt"):
 """
 Преобразует PNG-изображение в набор данных о пикселях и записывает их в текстовый файл.

 Args:
  image_path: Путь к PNG-файлу.
  output_file: Имя выходного текстового файла (по умолчанию "pixel_data.txt").
 """

 image = Image.open(image_path).convert('RGB')
 width, height = image.size

 with open(output_file, "w") as f:
  for y in range(height):
   for x in range(width):
    r, g, b = image.getpixel((x, y))
    h, s, v = colorsys.rgb_to_hsv(r / 255, g / 255, b / 255)
    f.write(f"{h:.2f},{s:.2f},{v:.2f}\n")

# Пример использования
image_path = "image.png"
png_to_pixel_data(image_path) # Сохранит данные в "pixel_data.txt"
