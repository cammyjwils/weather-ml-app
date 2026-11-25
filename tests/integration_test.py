import unittest
from app import app, weather_classes  # Import your Flask app instance and its class labels


class TestModelAppIntegration(unittest.TestCase):

	def setUp(self):
		app.testing = True
		self.client = app.test_client()
		
	def test_model_app_integration(self):
		# Valid test input that should work with the trained model
		form_data = {
			'temperature': '275.15',   # Kelvin
			'pressure': '1013',        # hPa
			'humidity': '85',          # %
			'wind_speed': '3.6',       # m/s
			'wind_deg': '180',         # degrees
			'rain_1h': '0',            # mm
			'rain_3h': '0',            # mm
			'snow': '0',               # mm
			'clouds': '20'             # %
		}

		response = self.client.post('/', data=form_data)
	
		html_text = response.data.decode('utf-8').lower()

		# Ensure that the result page (response.data) should include a weather prediction
		self.assertIn('the weather is', html_text)

		# Ensure that the result page should include a prediction time
		self.assertIn('prediction time', html_text)

		# Use the app's own labels so renaming a class doesn't break the test
		valid_classes = weather_classes
		found = any(weather in html_text for weather in valid_classes)
		
		# Ensure that classification is in valid classes, provide an error message if not.
		self.assertTrue(found, "Prediction is not one of the valid weather classes")
		

if __name__ == '__main__':
	unittest.main()
