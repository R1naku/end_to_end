CREATE TABLE IF NOT EXISTS weather_metrics (
    id SERIAL PRIMARY KEY,
    recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature NUMERIC(4, 2),
    humidity INTEGER CHECK (humidity BETWEEN 0 AND 100),
    pressure NUMERIC(6, 2),
    wind_speed NUMERIC(5, 2)
);

CREATE INDEX IF NOT EXISTS idx_weather_metrics_recorded_at 
ON weather_metrics (recorded_at);