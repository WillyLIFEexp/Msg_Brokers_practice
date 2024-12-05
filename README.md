# Msg Brokers Practice
This is a practice for message brokers with RabbitMQ

## :hammer_and_pick: Technologies Used
- **Languages**: Python
- **Message Broker**: RabbitMQ
- **Other Libraries**: 
  - Pytest
  - Pika (for RabbitMQ client interactions)
- **Containerization**: Docker, Docker Compose

## :gear: Prerequisites
- Python 3.8+
- [Docker](https://docs.docker.com/engine/install/) 

## :closed_book: Project Directory Structure
```bash
Msg_Brokers_Practice/
├── consumer/          # Contains consumer codes 
│ ├── consumer.py      # Source code for consumer
│ └── Dockerfile       # Consumer Docker configuration file
├── producer/          # Contains producer code
│ ├── producer.py      # Source code for producer
│ └── Dockerfile       # Producer Docker configuration file 
├── imgs/              # The demo.gif 
├── requirements.txt   # Python dependencies 
├── docker-compose.yml # Docker compose configuration file 
└── README.md          # Documentation for the project
```

## :wrench: Setting up

* Clone the Repo
* Build the containers using the following command.
    ```
    docker-compose up
    ```
* Stop the containers using the following command.
    ```
    docker-compose down
    ```

## :tophat: Demonstration
![](https://github.com/WillyLIFEexp/Msg_Brokers_practice/blob/create_producer_consumer/imgs/demo_1.gif)
