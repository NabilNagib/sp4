# Superheroes Flask Application

This repository contains a Flask application for managing superheroes and their powers. The application includes three main files: `app.py`, `models.py`, and `seed.py`, all located inside the `server` folder. The application uses an SQLite database named `superheroes.db`.

Click the link below to visit the site.

[Superheroes](https://superheroes-nabil-nagib.onrender.com/)

## Setup and Running Instructions

## 1. Prerequisites

### Install Python

Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/).

Verify the installation by running:

```bash
python --version
```

### Install Visual Studio Code

* Visual Studio Code, official website: [VisualStudio.com](https://code.visualstudio.com/download)

## 2. Clone the Repository

Copy and paste the below to the Terminal

git clone <https://github.com/Moringa-SDF-PTO5/superheroes-nabil-nagib.git>

After Cloning open VSCode, click Terminal and select New terminal and type:

```bash
cd server
```

## 3. Create a Virtual Environment

Create and activate a virtual environment to manage dependencies:

Mac/Linux users;

```bash
python -m venv venv

source venv/bin/activate  
```

Windows users:

```bash
python -m venv venv

venv\Scripts\activate
```

## 4. Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 5. Set Up the Database

Initialize the database and run migrations:

```bash
flask db init
flask db migrate -m "migration"
flask db upgrade
```

## 6. Seed the Database

Seed the database with initial data:

```bash
python server/seed.py
```

## 7. Run the Flask Application

Start the Flask application:

```bash
export FLASK_APP=server/app.py
python app.py
```

## Application Features

### app.py

This file sets up the Flask application, configures the database, and defines the API routes. The routes include:

* GET /heroes: Returns a list of all heroes.
* GET /heroes/<int:id>: Returns details of a specific hero by ID.
* GET /powers: Returns a list of all powers.
* GET /powers/<int:id>: Returns details of a specific power by ID.
* PATCH /powers/<int:id>: Updates the description of a specific power.
* POST /hero_powers: Creates a new HeroPower.

### models.py

This file defines the database models and their relationships:

* Hero: Represents a superhero with id, name, and super_name.
* Power: Represents a power with id, name, and description.
* HeroPower: Represents a relationship between Hero and Power with id, strength, hero_id, and power_id.

### seed.py

This file seeds the database with initial data for heroes, powers, and hero_powers. The file does the following:

* Clears the existing data.
* Adds predefined powers to the database.
* Adds predefined heroes to the database.
* Associates heroes with powers and strengths.

## License

Copyright © 2024 Nabil Nagib

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
