from PIL import Image
import colorsys

def pixel_data_to_png(data_file, output_image="reconstructed_image.png"):
 """
 Преобразует текстовый файл с данными о пикселях в PNG-изображение.

 Args:
  data_file: Путь к текстовому файлу с данными о пикселях.
  output_image: Имя выходного PNG-файла (по умолчанию "reconstructed_image.png").
 """

 with open(data_file, "r") as f:
  lines = f.readlines()

 # Определяем ширину и высоту изображения на основе количества строк в файле
 width = int(len(lines) ** 0.5)
 height = width

 image = Image.new("RGB", (width, height))
 pixels = image.load()

 # Восстанавливаем пиксели из файла
 for y in range(height):
  for x in range(width):
   index = y * width + x
   h, s, v = map(float, lines[index].strip().split(","))
   r, g, b = colorsys.hsv_to_rgb(h, s, v)
   pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255))

 image.save(output_image)

# Пример использования
data_file = "pixel_data.txt"
pixel_data_to_png(data_file) # Сохранит изображение в "reconstructed_image.png"
