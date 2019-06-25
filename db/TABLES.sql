CREATE TABLE climate (
	id SERIAL,
	sample_date TIMESTAMP WITH TIME ZONE,
	temperature NUMERIC(3,1),
	humidity_percent NUMERIC(3,1),
	external_temperature NUMERIC(3,1),
	external_humidity_percent NUMERIC(3,1),
	PRIMARY KEY (id)
);

CREATE TABLE soil (
	id SERIAL,
	sample_date TIMESTAMP WITH TIME ZONE,
	probe INTEGER NOT NULL,
	moisture_percent NUMERIC(3,1),
	conductivity NUMERIC(6,2),
	PRIMARY KEY (id)
);

CREATE TABLE water (
	id SERIAL,
	sample_date TIMESTAMP WITH TIME ZONE,
	height_mm INTEGER,
	distance_to_water_mm INTEGER,
	pump_working BOOLEAN,
	PRIMARY KEY (id)
);