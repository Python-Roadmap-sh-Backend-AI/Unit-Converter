# Unit Converter

Click here for the web app that was deployed using vercel - https://unit-converter-3qmlv4jtm-gamidukaveen-2497s-projects.vercel.app

## Overview

Unit Converter is a web-based application built using Python and Flask that allows users to convert values between different units of measurement. The application provides separate conversion sections for Length, Weight, and Temperature units, enabling users to easily enter a value, select the source and target units, and view the converted result.

The project was developed to demonstrate fundamental backend development concepts such as handling HTTP requests, processing form data, implementing business logic, and rendering dynamic content using Flask templates.

---

## Features

* Convert between multiple Length units:

  * Millimeter (mm)
  * Centimeter (cm)
  * Meter (m)
  * Kilometer (km)
  * Inch (in)
  * Foot (ft)
  * Yard (yd)
  * Mile (mi)

* Convert between multiple Weight units:

  * Milligram (mg)
  * Gram (g)
  * Kilogram (kg)
  * Ounce (oz)
  * Pound (lb)

* Convert between Temperature units:

  * Celsius (°C)
  * Fahrenheit (°F)
  * Kelvin (K)

* User-friendly web interface

* Server-side conversion processing using Flask

* Dynamic result display after form submission

---

## Technologies Used

* Python
* Flask
* HTML
* CSS
* Jinja2 Templating Engine

---

## Project Structure

```text
unit_converter/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── length.html
│   ├── weight.html
│   └── temperature.html
│
└── static/
    └── style.css
```

### File Descriptions

#### app.py

The main Flask application file. It contains:

* Application initialization
* Route definitions
* Form handling logic
* Unit conversion calculations
* Rendering of HTML templates

#### templates/

Contains all HTML pages used by the application.

* `index.html` – Home page containing navigation links.
* `length.html` – Length conversion form and result display.
* `weight.html` – Weight conversion form and result display.
* `temperature.html` – Temperature conversion form and result display.

#### static/

Contains static assets such as CSS stylesheets.

* `style.css` – Styling for the user interface.

---

## How the Application Works

### 1. User Opens a Conversion Page

The user navigates to one of the conversion pages, such as Length Converter.

The Flask application receives a GET request and returns the corresponding HTML page.

```text
Browser → Flask Route → HTML Page
```

---

### 2. User Enters Conversion Data

The user:

* Enters a numeric value
* Selects a source unit
* Selects a target unit
* Clicks the Convert button

Example:

```text
Value: 10
From: Kilometer
To: Millimeter
```

---

### 3. Form Submission

The browser sends the entered data to the Flask server using an HTTP POST request.

Example form data:

```python
{
    "value": "10",
    "from_unit": "kilometer",
    "to_unit": "millimeter"
}
```

---

### 4. Flask Processes the Data

The submitted values are accessed using:

```python
value = float(request.form["value"])
from_unit = request.form["from_unit"]
to_unit = request.form["to_unit"]
```

---

### 5. Conversion Logic

For Length and Weight conversions, the application uses a base-unit approach.

For Length conversions, Meter is used as the base unit:

```python
length_units = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1,
    "kilometer": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34
}
```

Each value represents how many meters are contained in one unit.

The conversion is performed in two steps:

1. Convert the source value to meters.
2. Convert the meter value to the target unit.

Formula:

```python
base_value = value * length_units[from_unit]
result = base_value / length_units[to_unit]
```

Example:

```text
10 km → mm
```

Convert to meters:

```text
10 × 1000 = 10000 m
```

Convert to millimeters:

```text
10000 ÷ 0.001 = 10000000 mm
```

Result:

```text
10 km = 10,000,000 mm
```

---

### 6. Displaying the Result

After the conversion is completed, Flask sends the calculated result back to the HTML template.

The result is displayed using Jinja templating:

```html
{{ result }}
```

The user then sees the converted value on the page without needing a database or additional storage.

---

## Learning Objectives

This project demonstrates:

* Flask application structure
* Routing and URL handling
* GET and POST requests
* HTML forms
* Server-side form processing
* Python dictionaries
* Dynamic HTML rendering with Jinja2
* Unit conversion algorithms
* Separation of frontend and backend logic

---

Thank You!

```
```
