
# api_final_yatube

api_final_yatube предоставляет api для создания и редактирования публикаций, комменатриев, подписок на авторов, регистрации и промотра сообществ.

## Установка проекта 

Клонировать [репозиторий](https://github.com/Jaraxxsus/api_final_yatube) и перейти в него в командной строке:

```
git clone https://github.com/Kaliendos/api_final_yatube.git
cd yatube_api
```

**Cоздать и активировать виртуальное окружение:**
```
python3 -m venv env
source env/bin/activate
```

**Установить зависимости из файла requirements.txt:**
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

**Выполнить миграции:**
```
python3 manage.py migrate
```

**Запустить проект:**
```
python3 manage.py runserver
```
## Примеры:

**Post api/v1/jwt/create/**:
Создает jwt-токен

**GET api/v1/posts/**:
возвращает список постов:
```
response:
 {
        "id": 1,
        "author": "DartWaidor",
        "text": "Был пост 1 , а стал пост 111",
        "pub_date": "2022-08-03T11:06:39.346403Z",
        "image": null,
        "group": null
    },
    {
        "id": 2,
        "author": "DartWaidor",
        "text": "пост2",
        "pub_date": "2022-08-03T11:06:56.934611Z",
        "image": null,
        "group": null
    },
```

**GET api/v1/groups/**:
возвращает список групп 
```
response:
 {
        "id": 1,
        "title": "Группа 1",
        "description": "О группе 1",
        "slug": "group1"
    },
    {
        "id": 2,
        "title": "Группа 2",
        "description": "О группе 2",
        "slug": "group2"
    }
```
    
 **Более подробно см. в технической докуентации проекта по адресу /redoc/**
