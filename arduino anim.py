import time
fname = input("Введите имя конечного файла: ")
fna = fname + '.ino'
f = open(fna, "w")
dela = 0.005
def pre_setup(a, b, c):
    f.write('//connect SCK to A5, SDA to A4' + '\n')
    f.write('int inv = ' + a + ';' + '\n')
    f.write('int anim_delay = ' + c + ';' + '\n')
    f.write('#include <Wire.h>' + '\n')
    f.write('#include <OLED_SH1106.h>' + '\n')
    f.write('#include "'+ b + '"' + '\n')
    f.write('//go to https://duino.ru/media/image-converter/index.html' + '\n')
    f.write('OLED_SH1106 display(-1);' + '\n')
    f.write('   ' + '\n')
    print('pre_setup создан')
    time.sleep(dela)


def _setup():
    f.write('void setup(){' + '\n')
    f.write('  display.begin(SH1106_SWITCHCAPVCC, 0x3c);' + '\n')
    f.write('  display.clearDisplay();' + '\n')
    f.write('}' + '\n')
    print('setup создан')
    time.sleep(dela)

def _loop(a):
    f.write('void loop(){' + '\n')
    for i in range(a):
        numb = str(i)
        f.write('   frame' + numb + '();' + '\n')
    f.write('}' + '\n')
    f.write('   ' + '\n')
    print('loop создан')
    time.sleep(dela)

def _frames(a, b):
    for i in range(a):
        numb = str(i)
        f.write('void frame' + numb + '() {' + '\n')
        f.write('    display.clearDisplay();' + '\n')
        f.write('    display.drawBitmap(0, 0, ' + b + numb + ', 128, 64, WHITE);' + '\n')
        f.write('    display.display();' + '\n')
        f.write('    if (inv == 0) {' + '\n')
        f.write('      display.invertDisplay(true);' + '\n')
        f.write('    }' + '\n')
        f.write('    delay(anim_delay);' + '\n')
        f.write('' + '\n')
        f.write('  }' + '\n')
        f.write('     ' + '\n')
        print('frame', i, 'создан')
        time.sleep(dela)

def res_file():
    print('Готово!')
    print('Результат находится в файле ' + fna)
    time.sleep(5)

def final():
    print("Схема подключения дисплея")
    time.sleep(dela)
    print("Сверху - пины дисплея")
    time.sleep(dela)
    print("Снизу - пины Arduino")
    time.sleep(dela)
    print("VDD GND SCK SDA")
    time.sleep(dela)
    print("||| ||| ||| |||")
    time.sleep(dela)
    print("3V3 GND  A5  A4")
    time.sleep(dela)
    
num = int(input("Введите количество кадров: "))
inv = input("Включить инверсию цветов?" + '\n' + "0 - Нет" + '\n' + "1 - Да" + '\n' + "(По умолчанию 'нет')")
name = input("Введите название кадров(по умолчанию 'image'): ")
lib = input("Введите название и расширение файла с кадрами(по умолчанию 'image.h'): ")
delay_ = input("Введите задержку между кадрами(по умолчанию 25): ")
if (delay_ == ""):
    delay_ = '25'
if (inv == ""):
    inv = "0"
if (lib == ""):
    lib = 'image.h'
pre_setup(inv, lib, delay_)
_setup()
_loop(num)
if (name == ""):
    name = 'image'
_frames(num, name)
final()
res_file()
