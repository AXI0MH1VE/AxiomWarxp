-- Initial migration: Tables for God Protocol
CREATE TABLE agents (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    status VARCHAR(50) DEFAULT 'active'
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    agent_id INTEGER REFERENCES agents(id),
    amount DECIMAL(10,2)
);
