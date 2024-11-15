*(EN description)*
This project has two modes:
1) convert Png image to image dataset into MHSL (MarkedHueSaturationBrightness) table
2) converting an MHSL table into a PNG image.

1.1 The first utility (/Converter/ImageToMHSL) converts the image (which should be in the same package with the program and called image.png) into a set of pixel data in the following format {*hue*, *saturation*, *brightness*}. the output file called Pixel_data.txt will contain all the pixel data. 
2.1 The second utility (/Converter/MHSLToimage) converts the pixel data (contained in pixel_data.txt) into an image (reconstructed_image.png). All input and output files are saved in one folder with the utility.

3.1 After running the first and second scripts, your image will take up 10% less space without losing quality

Used libraries:
PIL,
colorsys,
OS


*(RU description)*
Данный проект имеет два режима:
1) преобразование PNG изображения в набор данных изображения в таблицу MHSL (MarkedHueSaturationBrightness)
2) преобразование MHSL таблицы в изображение PNG.

1. Первая утилита (/Converter/ImageToMHSL) преобразует изображение (которое должно находится в одной паке с программой и называтся image.png) в набор данных о пикселях в следующем формате {*цветовой тон*, *насыщенность*, *яркость*}. выходной файл по названием Pixel_data.txt будет содержать все данные о пикселях. Все входные и выходные файлы сохраняются в одну папку с утилитой.
2. Вторая утилита (/Converter/MHSLToimage) преобразует данные о пикселях (которые содержатся в pixel_data.txt) в изображение (reconstructed_image.png). Все входные и выходные файлы сохраняются в одну папку с утилитой.

После выполнения первого и второго скрипта ваше изображение станет занимать на 10% меньше места без потери качества

Задействованные библиотеки:
PIL,
colorsys,
OS
