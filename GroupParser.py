#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import vk_api
import time
import codecs


if __name__ == '__main__':
    # Заходим ВКонтакте под своим логином
    vk_session = vk_api.VkApi('login', 'password')
    vk_session.auth()
    vk = vk_session.get_api()

    # Открываем файл для записи результатов
    ff = codecs.open('ids.txt', 'w', encoding='utf8')
    print('Downloading ID')
            # Получаем юзеров - их ФИО, айди, и фотку
    z = vk.groups.getMembers(group_id=85030237,
                                fields='photo_max_orig, has_photo, '
                                       'first_name, last_name')
    data = z["items"] # Присваиваем переменной первую тысячу id'шников
    count = z["count"] // 1000 # Присваиваем переменной количество тысяч участников
    for i in range(1, count+1):  
        data = data + vk.groups.getMembers(group_id=85030237,
                                fields='id, photo_max_orig, has_photo, '
                                       'first_name, last_name', v=5.92, offset=i*1000)["items"]
    print('Peoples count: ' + str(z['count']))
    for x in data:
        if x['has_photo'] == 1:
            # Записываем данные о юзере в файл разделяя черточкой |
            s = str(x['id']) + '|' + str(x['photo_max_orig']) + '|' + str(
                x['first_name']) + ' ' + str(x['last_name']) + '\n'
            ff.write(s)

    ff.close()
    print('Done!')

