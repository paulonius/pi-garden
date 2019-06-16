CREATE TABLE climate (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	sample_date TIMESTAMP,
	temperature DECIMAL(3,1),
	humidity_percent DECIMAL(3,1),
	external_temp DECIMAL(3,1),
	external_humidity_percent DECIMAL(3,1),
	PRIMARY KEY (id),
	INDEX (sample_date)
);

CREATE TABLE soil (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	sample_date TIMESTAMP,
	probe TINYINT NOT NULL,
	moisture_percent DECIMAL(3,1),
	conductivity DECIMAL(6,2),
	PRIMARY KEY (id),
	INDEX (sample_date)
);

CREATE TABLE water (
	id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
	sample_date TIMESTAMP,
	height_mm SMALLINT(4),
	distance_to_water_mm SMALLINT(4),
	pump_working BOOLEAN,
	PRIMARY KEY (id),
	INDEX (sample_date)
);