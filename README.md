Amazon Sales Dashboard

📋 Project Overview

The Amazon Sales Dashboard is a dynamic web application that provides insights into Amazon sales data. It enables users to explore key metrics, visualize trends, and analyze customer reviews interactively.

This project showcases my skills in data analysis, Python, Flask, SQL, and data visualization.

🚀 Features

	1.	Interactive Dashboard:
		•	Top-rated products and their details.
		•	Correlation between discounts and product ratings.
		•	Sentiment analysis on customer reviews.
		•	Dynamic filtering by category and rating.
	2.	Key Performance Indicators (KPIs):
		•	Total products.
		•	Average product rating.
		•	Maximum discount offered.
	3.	Visualizations:
		•	Bar charts for top-rated products.
		•	Scatter plots for discount percentage vs. rating.
		•	Sentiment analysis distribution.
	4.	Additional Features:
		•	Pagination for large datasets.
		•	Backend caching for faster performance.

🛠️ Technologies Used

	•	Python: Backend logic and data manipulation.
	•	Flask: Web framework for building the application.
	•	MySQL: Database for storing and querying Amazon sales data.
	•	SQLAlchemy: ORM for seamless database interaction.
	•	Plotly: Interactive visualizations for charts and plots.
	•	TextBlob: Sentiment analysis on customer reviews.
	•	Bootstrap: Responsive and aesthetic frontend.

🔧 Installation Guide

Step 1: Clone the Repository

	git clone https://github.com/Sanjyot789/AmazonSalesData.git
	cd AmazonSalesData

Step 2: Create a Virtual Environment

	python -m venv env
	source env/bin/activate   

Step 3: Install Dependencies

	pip install -r requirements.txt

Step 4: Set Up the Database

Import the database schema and data using the provided SQL file:

	mysql -u root -p < amazon.sql

Step 5: Run the Application

	python app.py

Step 6: Access the Dashboard

Open your browser and navigate to:

	http://127.0.0.1:5000/

📂 Project Structure

	amazon-sales-dashboard/
	├── app.py               # Main Flask application
	├── templates/           # HTML templates for the frontend
	│   ├── index.html       # Homepage with filters
	│   ├── dashboard.html   # Dashboard page with visualizations
	├── requirements.txt     # Python dependencies
	├── environment.yml      # Conda environment file
	├── Amazon_sales_data.sql# MySQL database export
	└── README.md            # Project documentation

📸 Screenshots

Homepage

![image](https://github.com/user-attachments/assets/e07e8411-fe2b-45b9-8892-845ccc8fcbd9)

Dashboard

![image](https://github.com/user-attachments/assets/c75dea41-61a8-410d-9da6-fbf19ed7d0b7)

![image](https://github.com/user-attachments/assets/5b0322b0-126e-4e84-b880-fdb7d4cbba2a)


💡 Future Enhancements

	1.Machine Learning Models:
		Predict sales trends based on historical data.
		Product recommendation system.
	2.Advanced Filters:
		Price range sliders.
		Time-based analysis for trends.
	3.Deployment:
		Host the app on Heroku, AWS, or Render for public access.

