Проект представляет собой API для системы опросов пользователей.

Документация доступна после разворачивания проекта по ссылке:\
`/api/docs/` или в директории проекта `/docs/Quiz API.pdf`
 

**ВАЖНО**: обязательно измените файл `.env.prod` и `.env.prod.db` для передачи в качестве переменных среды нужных параметров
перед применением 

Проект подготовлен для deploy с помощью Docker. Для этого выполните действия:
2. Сборка обзазов и запуск контейнеров:\
`docker-compose -f docker-compose.prod.yml up -d --build`
3. Миграция в БД:\
`docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput`
4. Сборка static файлов:\
`docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear`
5. Создание суперпользователя: \
`docker-compose -f docker-compose.prod.yml exec web python manage.py createsuperuser`\
Создание суперпользователя позволит использовать API в качестве администратора.

C API реализована авторизация в системе по токену. Для его получения отправьте POST запрос с параметрами `username` и 
`password` на `/api-token-auth/`. Результатом будет токен, который надло установить в header запроса при использовании
API в качестве администратора системы.
