 # mmo-DoorDash-Copycat

A Python-based FastAPI application that emulates DoorDash's delivery fee calculation service. This project offers three endpoints for calculating delivery fees, estimating delivery time, and checking the service status.

## API Endpoints

1. **GET /** - Welcome message
2. **POST /calculate-fee/** - Calculate delivery fee based on distance and weight
3. **GET /estimate-time/{distance_km}** - Estimate delivery time based on distance
4. **GET /status/** - Check the service status

## Prerequisites

- Python 3.8 or higher
- YAML
- Markdown

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/mmo-doordash-copycat.git
    ```

2. Navigate to the project directory:
    ```bash
    cd mmo-doordash-copycat
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8080
    ```

2. Access the application:
    - Go to `http://localhost:8080` for the welcome message.
    - Use `/calculate-fee/` to calculate fees, `/estimate-time/{distance_km}` to estimate delivery times, and `/status/` to check the status.

## Docker Support

The project includes a `Dockerfile` for easy deployment. To build and run the Docker image:

1. Build the Docker image:
    ```bash
    docker build -t doordash/delivery-fee-service .
    ```

2. Run the Docker container:
    ```bash
    docker run -d -p 8080:8080 doordash/delivery-fee-service
    ```

## Testing

The project includes test cases for integration and functionality testing. Run the tests using Pytest:

```bash
pytest tests
```

## Contributing

Feel free to contribute to this project! If you have any suggestions, issues, or pull requests, please open an issue or submit a pull request.

## License

This project is licensed under [MIT License](LICENSE).