from instance.config import app_config, config_ini


class TestAppConfig(object):
    def test_app_config_should_contain_all_targets(self):
        assert None is not app_config['development']
        assert None is not app_config['testing']
        assert None is not app_config['staging']

    def test_app_config_contains_keys(self):
        assert None is not app_config['development'].DEBUG
        assert None is not app_config['development'].CSRF_ENABLED
        assert None is not app_config['development'].SECRET
        assert None is not app_config['development'].SQLALCHEMY_DATABASE_URI

    def test_development_has_debug_enabled(self):
        assert True is app_config['development'].DEBUG

    def test_testing_has_testing_enabled(self):
        assert True is app_config['testing'].TESTING

    def test_production_has_no_debug_or_testing(self):
        assert False is app_config['production'].DEBUG
        assert False is app_config['production'].TESTING


class TestConfigIni(object):
    def test_config_ini_exists(self):
        assert None is not config_ini

    def test_config_ini_has_needed_sections(self):
        assert None is not config_ini['SENSORS']
        assert None is not config_ini['URLS']

    def test_config_ini_has_sonar_pins(self):
        assert None is not config_ini['SENSORS']['SonarTrigger']
        assert None is not config_ini['SENSORS']['SonarEcho']

    def test_config_ini_has_pump_pin(self):
        assert None is not config_ini['SENSORS']['Pump']
