# На технічному співбесіді претенденти на посаду одержують оцінку за тест.
# У наступний тур співбесіди проходять кандидати, які здали тест на 83 бали включно або вище.
# Реалізуйте оператор контролю виконання так, щоб він привласнив логічній змінній is_next
# значення True, якщо кількість набраних балів буде більшою або дорівнює 83. В іншому
# випадку значення змінної дорівнює False

a = int(input('Ведіть скільки у вас балів: '))

if a >= 83:
    print('True')
else:
    print('False - не добре')
