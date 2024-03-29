
# Oil and Gas Supply Chain Demand Forecasting Application

## Introduction

This project is focused on developing a demand forecasting application using Machine Learning, specifically the ARIMA (AutoRegressive Integrated Moving Average) model. The app is built with Streamlit, enabling an interactive web interface, and uses Pandas for efficient data handling. Additionally, the application is integrated with a Flask-based webhook to receive and process streaming data.

We use AWS Bedrock as base LLM Foundational Model for this project for data analytical purpose. You can add agent functionality and knowledge base - RAG for this model by using Langchain or use AWS Bedrock Console

for further inquiry check our website at: business.matter.co.id

## Features

- **Demand Forecasting Using ARIMA**: Leverages the ARIMA model for accurate demand forecasting.
- **Streamlit for Interactive UI**: Utilizes Streamlit for building an intuitive and interactive web interface.
- **Data Handling with Pandas**: Employs Pandas DataFrame for efficient data manipulation and analysis.
- **Webhook Integration with Flask**: Includes a Flask webhook for real-time data streaming and processing.
- **Mongo DB Integration**: Use no-SQL database to handle unstructured data streaming.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- Pip package manager
- Pipenv
- MongoDB run Locally/Server
- AWS CLI for Bedrock Integration

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mbahmujono/Pertamina
   ```

2. **Navigate to the project directory**
   ```bash
   cd Pertamina
   ```

3. **Install dependencies and activate the environment**
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```

4. **Update .env**
   ```env
   WEBHOOK_URL = http://localhost:5000/webhook # your localhost URL for webhook
   MONGO_URI = mongodb://localhost:27017/ # your mongodb connection
   MONGO_DB = test # your mongo db
   MONGO_COLLECTION = test # your mongo collection
   ```

   

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run streamlit/app.py
   ```

2. **Launch the Flask server (for webhook)**
   ```bash
   python datastream/datastream.py
   python webhook/app.py
   ```

## Usage

- Navigate to the Streamlit app URL provided in the terminal.
- Upload your dataset or use the real-time data streaming feature through the Flask webhook.
- Configure the ARIMA model parameters as needed.
- View the forecast results and analyses on the Streamlit interface.

## Contributing

Contributions to enhance the functionality or efficiency of this demand forecasting app are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b your-branch`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Contact

For any queries or suggestions, please reach out to Diaz at diaz@matter.co.id .
