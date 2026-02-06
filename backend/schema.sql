CREATE TABLE financial_uploads (
    id SERIAL PRIMARY KEY,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    raw_data JSONB
);
