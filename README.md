# Weather API Project

This Weather API project is a Python script that fetches the latest weather forecast for selected cities in different countries. The project utilizes the OpenWeatherMap API to retrieve weather data and then generates visual representations in the form of images and PDFs.

## Features

- Retrieves real-time weather information for specified cities in the United Kingdom, India, and the United States.
- Generates visually appealing weather forecast images with city names, temperatures, and humidity levels.
- Saves the generated images in both PNG and PDF formats for easy sharing and archiving.

## Usage

### Prerequisites

- Python
- Required Python packages: `requests`, `PIL` (Pillow), `json`

### Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather-api-project.git
   cd weather-api-project

2. Install dependencies(Execute in bash):
    pip install requests Pillow

3. Obtain an API key from https://openweathermap.org/ and replace the placeholder in the script with your key(Inside Python code):
    api_key = "your_openweathermap_api_key" 

4.Run the script(Execute in bash):
    python weather_api_script.py

## OUTPUT:
• The script generates weather forecast images and PDFs for cities in the UK, India, and the US.

• Images are saved in the project folder with filenames containing the date and city name (e.g.,    2023-01-01_London.png).

•PDFs are also saved with the same naming convention.

## ACKNOWLEDGEMENTS:
• The project uses the OpenWeatherMap API for weather data.





