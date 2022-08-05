
# api_final_yatube

api_final_yatube предоставляет api для создания и редактирования публикаций, комменатриев, подписок на авторов 

## Установка проекта 

Клонировать [репозиторий](https://github.com/Jaraxxsus/api_final_yatube) и перейти в него в командной строке:

git clone git@github.com:Jaraxxsus/api_final_yatube.git
cd yatube_api

**Cоздать и активировать виртуальное окружение:**
python3 -m venv env
source env/bin/activate

**Установить зависимости из файла requirements.txt:**
`python3 -m pip install --upgrade pip
pip install -r requirements.txt`

**Выполнить миграции:**
python3 manage.py migrate

**Запустить проект:**

python3 manage.py runserver

## Примеры:

**GET api/v1/posts/**:
возвращает список постов


**GET api/v1/groups/**:
возвращает список групп 
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
    

