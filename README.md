# Project "AtomicHabit"

### Description

✅ Registration and authorization endpoints are implemented:

✅ Password is hashed, so the user can obtain a token;

✅ The registration endpoint is open to everyone;

✅ Endpoints for the user's habit list and public habit list are implemented;

✅ Endpoints for creating, updating, and deleting habits are implemented;

✅ Access rights are correctly described;

✅ The owner is automatically assigned when creating a habit.

### Endpoints:

✅ To get a list of all habits for the current user: GET /habit/

✅ To get a list of all public habits: GET /habit/public_list/

✅ To create a new habit: POST /habit/

✅ To get details of a habit with ID=1: GET /habit/1/

✅ To update a habit with ID=1: PUT /habit/1/

✅ To partially update a habit with ID=1: PATCH /habit/1/

✅ To delete a habit with ID=1: DELETE /habit/1/

✅ For user registration: POST /logup/

✅ To get a token: GET token/

✅ For administration: GET /admin/

✅ Swagger documentation: GET /docs/

✅ Redoc documentation: GET /redoc/

### Documentation:

✅ Documentation output is configured

### Pagination:

✅ The list of public habits is paginated;

✅ The list of habits is paginated.

### Validation:

✅ Users cannot edit or delete other users' habits;

✅ Users can view public habits and their own habits;

✅ Integration with Telegram is implemented;

✅ Celery beat scheduled task is configured;

✅ CORS is configured.

### Installation and configuration

#### Install dependencies

```shell
pip install -r requirements.txt
```

#### Apply migrations

```shell
python3 manage.py migrate
```

#### Populate the database

```shell
python3 manage.py put_data
```

### Run the Server

```shell
python3 manage.py runserver&celery -A config.celery beat --loglevel=info
```

To receive notifications, you need to send any message to the ```@habit_rabbit_16102023_bot```.

Example of sending user registration data in Postman:

```shell
{
    "email": "test@mail.ru",
    "password": "123456zxcvbnm",
    "tg_id": "<your_telegram_id>"
}
```

### Testing

```shell
pip install coverage
```

For testing, a test user is used. To successfully run tests, you need to specify your Telegram
ID from the chat with the bot.

```shell
self.user = User.objects.create(email='testuser@example.com',
                                        password='testpassword',
                                        tg_id='id_psi')
```

### Run tests with coverage

```shell
coverage run --source='.' manage.py test
```

```shell
coverage report
```

### Code style

In this project, we follow the PEP8 coding style standards, the official coding style standard for the Python language.
We also
use the Flake8 tool for automated code style checking and maintenance.

### Code style checking tools

To check code compliance with coding style standards, we use the Flake8 tool. You can install
Flake8 with the following command:

```shell
pip install flake8
```

### Code style checking

```shell
flake8 --exclude=venv,External\ Libraries,Scratches,Consoles,migrations
```