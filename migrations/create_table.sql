DROP TABLE IF EXISTS car_purchasing;

CREATE TABLE IF NOT EXISTS car_purchasing(
        id SERIAL PRIMARY KEY,
        age INT NOT NULL,
        annual_salary DECIMAL,
        credit_card_debit DECIMAL,
        net_worth DECIMAL,
        purchase_amount DECIMAL
);