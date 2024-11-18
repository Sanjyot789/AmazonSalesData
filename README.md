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

📊 Dataset

	•	Source: Amazon sales dataset containing over 1,000+ product records, including ratings, reviews, prices, and discounts.
	•	Data Fields:
	•	product_name
	•	category
	•	rating
	•	discount_percentage
	•	review_content
	•	And more…

🔧 Installation Guide

1.	Clone the Repository:

	git clone https://github.com/your_username/amazon-sales-dashboard.git
	cd amazon-sales-dashboard


	2.	Create a Virtual Environment:

python -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate


	3.	Install Dependencies:

pip install -r requirements.txt


	4.	Set Up the Database:
	•	Import the database schema and data using the provided SQL file:

mysql -u root -p < Amazon_sales_data.sql


	5.	Run the Application: python app.py


6.	Access the Dashboard:
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

Dashboard

💡 Future Enhancements

	1.	Machine Learning Models:
	•	Predict sales trends based on historical data.
	•	Product recommendation system.
	2.	Advanced Filters:
	•	Price range sliders.
	•	Time-based analysis for trends.
	3.	Deployment:
	•	Host the app on Heroku, AWS, or Render for public access.

🤝 Contributing

Contributions are welcome! If you find a bug or want to suggest a feature:
	1.	Fork the repository.
	2.	Create a new branch.
	3.	Submit a pull request.
