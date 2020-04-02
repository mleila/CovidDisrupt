# CovidDisrupt
Early Warning System of Operations Disruptions from COVID-19.

Discovery of COVID-19 cases leads to local responses that may lead to supply chain disruptions. This application allows users to recive a message once a case has been found in a specific region of interest.

# Installtion
Use the following command to install the package to your local python environment. The installation will add all necessary binaries to your path.

`pip install CovidDisrupt`

# Configuration
Create a `config.json` and `secrets.json` from their templates.
```bash
mv secrets.template.json secrets.json
mv config.template.json config.json
```
Add your AWS credentials and News API key to the config and secrets json files.


# Usage
## Ingestion
For now, NewsApi is the only supported API. To ingest data to s3 use the following command
```bash
ingest_data \
    --topic 'covid' \
    --keywords 'corona OR covid OR coronavirus' \
    --start-date '2020-02-26' \
    --end-date '2020-03-29'
```
## Processing
Process ingested data to prepare it for analysis.
```bash
process_data --topic 'covid'
```
## Modelling
Train ML models, or run inference pipleines, on the data using AWS SageMaker (BlazingText) and AWS Comprehend
```bash
model_data --topic 'covid' --words 50
```
