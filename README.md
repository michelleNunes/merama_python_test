# merama_python_test

## Introduction
You will be required to create a project from scratch to try and get information from the [MercadoLibre API](https://developers.mercadolibre.com.mx/en_us/). For that you will have to fork this project and work in a personal branch.
It is not required to the project to actually work as you will have to develop it with mock credentials, we will review the code itself for the final score.

## Techologies
You will be required to use the following techonogies:
* Docker
* Python 3.9.7
* RabbitMQ
* Redis
* Credstash

## Architecture
You will need to use the following architecture for the project:
* The data you need to download will be [Items](https://developers.mercadolibre.com.mx/en_us/items-and-searches) using the following endpoint */users/$USER_ID/items/search?search_type=scan* to get the list of items and */items/$ITEM_ID* to get the whole information of the item.
* You will need to get items separatelly and publish them into a rabbitmq queue with the following structure
  {
    "data": (The actual data you are getting),
    "created_at": (The created at value of the item),
    "updated_at": (The updated at value of the item).
    "id": (The item id)
  }
* To be able to get the information from MercadoLibre you will need to get credentials using credstash and store them on Redis so you dont need to get the credentials every time.
* It will be required too to include both unit and integration testing.

## Evaluation
You will be evaluated by the following criteria:
* Use of all the above techologies.
* Structure of the project.
* Using coding best practices.
* Including testing to the project.
