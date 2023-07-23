# Sneaker Scraper Project

This is a `sneaker scraper` project that allows you to scrape sneaker details from a website and save them in a tabular form into a MySQL database. The backend is developed using Python Flask, and the frontend is built using React. The SQL database is hosted on the cloud, eliminating the need for local database setup.

## Features

- Scrape sneaker details such as model, shoe size, price, and discount from the target website.
- Save the scraped data in a tabular format into a MySQL database.
- Frontend built using React for a user-friendly interface.
- Backend powered by Python Flask to handle scraping and database operations.
- Cloud-based MySQL database for easy deployment.

## Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/RizanKhan837/swagkicks-hackathon.git
```

2. Navigate to the project's directory:

```bash
cd sneaker-scraper
```

3. Create a virtual environment (recommended) and activate it:

```bash
python -m venv venv
source venv/bin/activate   # For Windows: venv\Scripts\activate
```

4. Install the required Python packages:

```bash
pip install -r requirements.txt
```

5. Navigate to the project's frontend directory:

```bash
cd frontend
```

6. Install frontend dependencies:

```bash
npm install
```

## Usage

1. In a separate terminal, build and start the frontend development server:

```bash
npm run build
npm run dev
```

2. Run the backend server:

```bash
cd ..
flask run
```

* Access the frontend in your browser at `http://localhost:5173`.

* Enter the target website URL from which you want to scrape sneaker details.

* Click on the "submit" button to initiate the scraping process.

* Once the scraping is complete, the scraped data will be displayed in tabular form on the frontend.

* The scraped data will also be saved to the cloud-based MySQL database automatically.


## 🚀 About Me
I am a student of Software Engineering at [Bahria University](https://www.linkedin.com/school/bahria-university/). I am an Android Developer. I am skilled in **Solidity**, **Java**, **Android Development**, **C#**, **Linux**, **Javascript** and **Excel**. I have a strong interest in ***Cyber-Security*** and ***Blockchain***. I am a quick learner and I am always keen to learn new programming languages and technologies.


## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://rizankhan.me/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/rizwanakram837/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/RizanKhan_837)
