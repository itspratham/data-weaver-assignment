# data-weaver-assignment
1. Install rabbitmq on your system based on OS.
2. Create virtual environment and install requirement.txt using pip install -r requirements.txt.
3. Open three command prompts.

# 1st Command prompt:
1. python manage.py runserver
2. Open postman.
3. Hit API: http://127.0.0.1:8000/api/my-data/ to populate the data to queue using form-data in postman by passing {file: "file_path"}
4. Close the command prompt.

# 2nd Command Prompt:
1. python manage.py makemigrations new_app1
2. python manage.py migrate
3. python manage.py runserver
4. python consumer.py (this command will consume all the data and populate it the table created)
5. python manage.py runserver
6. Do not close this prompt.

# 3rd Command Prompt
1. python manage.py runserver 8002
2. On postman these APIs
    1. http://127.0.0.1:8002/api/products -- give request body as per method.
    2. http://127.0.0.1:8002/api/products/<<int:pk>> -- give request body as per method.
    3. http://127.0.0.1:8002/api/products/score --- to calculate the score as per the assignment
