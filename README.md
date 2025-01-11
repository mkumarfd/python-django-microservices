# python-django-microservices
This is Microservices Application

The Product Service and Order Service are independent project.
![image](https://github.com/user-attachments/assets/4291165e-fcd1-4837-a612-5fd55b7bbd7a)

# Creating and Start Server for Product Service
Product Service uses Sqlite3 database

$ django-admin startproject product_service   
$ cd product_service   
$ django-admin startapp products   

$ python manage.py makemigrations   
$ python manage.py migrate   
$ python manage.py runserver 8001   

This runs the ProductService on http://localhost:8001/api/products/   

# Creating and Start Server for Order Service
Order Service uses Postgresql database

$ django-admin startproject order_service   
$ cd order_service   
$ django-admin startapp orders   

$ python manage.py makemigrations   
$ python manage.py migrate   
$ python manage.py runserver 8002   

This runs the OrderService on http://localhost:8002/api/orders/   

![image](https://github.com/user-attachments/assets/b04ecf01-d149-449a-87db-e4d3be9a7f97)   

# Kafka using Docker
https://developer.confluent.io/confluent-tutorials/kafka-on-docker/   

In each microservice I included the Dockerfile - this will create the docker image and container   

# Postman API Test   
![image](https://github.com/user-attachments/assets/a78fe0a2-b89f-4265-bb47-2499dbdcf766)   
![image](https://github.com/user-attachments/assets/9a714704-c7cc-4924-84c0-ab7ff83c9a3b)   
![image](https://github.com/user-attachments/assets/dad2f821-7ec5-4a1f-b30e-ca9dcca06db0) 

# Kafka Consumer program   

I have included the consumer.py program in product_service, which will show all messages produced   
from kafka producer like Product added or order created. Run this program in a separate terminal.

![image](https://github.com/user-attachments/assets/99c0520b-2b98-42ac-ba2f-77d417a28713)   

# API Gateway

If we are building a python django web app which uses the microservices application, to talk   
to each microservices and route the http requests to the correct microservices is done   
using API Gateway, I haven't used the gateway, the one good for django framework is:   

FastAPI + Uvicorn - simple and lightweight API
















