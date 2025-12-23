CREATE TABLE IF NO EXISTS wather-metrics (
    id SERIAL PRIMARY KEY,
    recorded_at TIMESAMP DEFAULT CURRENT_TIMESTAMP,
    temperature NUMERIC(6, 2),
    humidity INTEGER CHECK (humidity BETWEEN 0 AND 100 )
    pressure NUMERIC(6, 2)
    wind_speed NUMERIC(5, 2)
);

CREATE INDEX IF NOT EXISTS ind_weather_metrics_recorded_at

COMMENT ON TABLE weather_metrics IS 'показания'