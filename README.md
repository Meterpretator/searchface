## Аналог Findface для небольших городов
***ВСЕ СКРИПТЫ ЗАПУСКАТЬ ЧЕРЕЗ python3***
Система состоит из нескольких скриптов - скачивает фото юзеров из профилей ВК в рамках одного указанного города, и создает базу биометрических данных этих лиц, связывая их с аккаунтами ВК.

Скрипты протестированы на Parrot OS и требуют установки модулей Python которые есть в разделах import у скриптов

Для того чтобы скрипты заработали клонируйте этот репозиторий и удалите из подкаталогов файлы README.MD - иначе они будут мешать работе скриптов

Скачайте этот файл https://cloud.mail.ru/public/2KGj/2pWSDbXZt и бросьте в папку с проектом

***Скрипт выдает ошибку с эти файлом***
Скачать нужно этот https://github.com/JeffTrain/selfie/raw/master/shape_predictor_68_face_landmarks.dat файл


1) VkIdsParser_1.py - впишите в скрипт ваш логин пароль ВК (с выключенной двухфакторной авторизацией)

Также поменяйте параметры аккаунтов которые надо парсить - пол, возраст, город

По итогам работы скрипта вы получите файлик ids.txt со списком ID ВК

1.1) vkIDparser.py скрипт для парса id из групп. 
В строках

z = vk.groups.getMembers(group_id=id группы,

data = data + vk.groups.getMembers(group_id=id группы,

Отредачить group_id=id группы. Узнать id можно, например, здесь https://regvk.com/id/

2) DownloadPhotosToJpg_2.py - впишите в скрипт ваш логин пароль ВК (с выключенной двухфакторной авторизацией)

скрипт берет данные из списка ids.txt и скачивает в папку jpg по нескольку фото с каждого аккаунта 

Имена файлов ссответствуют id ВК

3) JpgToNpy_3.py - Производит процесс сбора биометрических параметров лиц с фото в папке jpg и сохраняет их в паку npy в виде мелких файликов

При больших объемах фоток скрипт может работать достаточно долго (часы, дни)

Тем не менее его можно выключить в любой момент а при следующем запуске он начнет с того места где остановился

4) FindIntoNpy_4.py - скрипт пытается найти среди файлов .npy в папке npy биометрию схожую с 1.jpg

Файл 1.jpg с искомым лицом нужно предварительно поместить в корневую директорию проекта

Данный скрипт ищет очень медленно из-за того что ему нужно перебрать все файлы .npy

Не рекомендуется использовать данный способ для поиска - только для проверки корректности создания .npy

5) NpyToEmbeddingsBin_5.py - скрипт берет все файлы .npy из папки npy и создает на их основе файл embeddings.bin

Созданный файл по сути содержит биометрию всех ранее распознанных лиц и все файлы с папок jpg и npy после его создания уже не нужны

Помимо этого создается файл associations.txt в котором хранятся соответствия номеру записи в эмбединге и имени файла .npy из которого она была взята

6) FinfFaceInEmbeddingsBin_6.py - пытается найти в базе лицо схожее с лицом на 1.jpg

Файл 1.jpg с искомым лицом нужно предварительно поместить в корневую директорию проекта

В отличии от скрипта номер 4 работает очень быстро. 
