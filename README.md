# Snowflake Cortex AI Financial Intelligence Pipeline

[![Snowflake](https://img.shields.io/badge/Snowflake-Cortex%20AI-29B5E8.svg)](https://www.snowflake.com/)
[![Snowpark](https://img.shields.io/badge/Snowpark-Python-blue.svg)](https://docs.snowflake.com/developer-guide/snowpark/python/index)

Production-ready ELT and Generative AI pipeline utilizing **Snowflake Cortex LLM Functions** (`COMPLETE`, `EXTRACT_ANSWER`, `SENTIMENT`) to automate regulatory disclosure analysis directly inside the data warehouse.

## 🚀 Key Features
- **In-Warehouse Inference**: Run LLMs directly where financial data lives without moving PII outside Snowflake.
- **Automated Streams & Tasks**: Triggers LLM analysis whenever new quarterly reports are staged via Snowpipe.
- **Zero Data Egress**: Fully compliant with BFSI strict governance boundaries.

## 🛠 Tech Stack
- Snowflake Cortex AI (Mistral, Llama 3)
- Snowpark Python API
- Snowflake Streams & Tasks
