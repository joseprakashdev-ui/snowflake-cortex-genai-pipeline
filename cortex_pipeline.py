"""Snowflake Cortex AI Pipeline for Financial Document Intelligence."""
import os

SNOWFLAKE_SQL_PIPELINE = """
-- 1. Create Staging Table for Regulatory Filings
CREATE OR REPLACE TABLE RAW_FINANCIAL_DISCLOSURES (
    DOC_ID VARCHAR,
    COMPANY_NAME VARCHAR,
    FILING_DATE DATE,
    REPORT_TEXT VARCHAR
);

-- 2. Cortex LLM Automated Analysis View
CREATE OR REPLACE VIEW V_FINANCIAL_CORTEX_INSIGHTS AS
SELECT
    DOC_ID,
    COMPANY_NAME,
    FILING_DATE,
    -- Sentiment extraction (-1.0 to 1.0)
    SNOWFLAKE.CORTEX.SENTIMENT(REPORT_TEXT) AS SENTIMENT_SCORE,
    -- Zero-shot extraction of key regulatory risk factors
    SNOWFLAKE.CORTEX.EXTRACT_ANSWER(
        REPORT_TEXT, 
        'What are the primary commercial loan and credit risk factors mentioned?'
    ) AS EXTRACTED_RISK_FACTORS,
    -- Executive summary using Llama 3 70b
    SNOWFLAKE.CORTEX.COMPLETE(
        'llama3-70b', 
        CONCAT('Summarize this quarterly financial disclosure for risk executives in 3 bullet points: ', REPORT_TEXT)
    ) AS EXECUTIVE_SUMMARY
FROM RAW_FINANCIAL_DISCLOSURES;
"""

print("[*] Snowflake Cortex AI Pipeline SQL Schema Definition Ready.")
if __name__ == "__main__":
    print(SNOWFLAKE_SQL_PIPELINE)
