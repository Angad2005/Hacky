# MindTric 🧠✨

> A website for creating awareness and helping people with various psychological problems.

This project is a web application designed to offer support and information on mental well-being. It also serves as a technical demonstration of integrating multiple backend services and APIs, showcasing a robust implementation of CORS between different resources.

---

## 🚀 Key Features

-   **Mental Health Awareness:** Provides resources and information to help users understand various psychological issues.
-   **AI-Powered Assistance:** Integrates Google's Generative AI to offer interactive support.
-   **Multi-Service Architecture:** Demonstrates a real-world use case of running Django and Flask services together.
-   **API & CORS Implementation:** Showcases the correct way to handle API communication and manage Cross-Origin Resource Sharing (CORS) between a primary backend and microservices.

---

## 🛠️ Tech Stack

-   **Backend:** Python, Django, Flask
-   **Frontend:** HTML, CSS, JavaScript
-   **APIs:** Google Generative AI, Google API Services

---

## 📋 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:

-   Python 3.8+
-   `pip` (Python package installer)
-   Basic knowledge of how to work with APIs and environment variables.

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Angad2005/Hacky.git](https://github.com/Angad2005/Hacky.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Hacky
    ```

3.  **Install the required dependencies:**
    ```sh
    pip install django flask flask-cors google-generativeai
    ```

4.  **Set up Environment Variables:**
    This project requires API keys to function correctly. Create a `.env` file in the root directory and add your keys there.

    ```
    API_KEY_GOOGLE=your_google_api_key_here
    ```
    *Note: Ensure the `.env` file is listed in your `.gitignore` file to prevent exposing your secret keys.*

---

## ▶️ Usage

Since this project uses both Django and Flask, you will likely need to run both servers.

1.  **To run the Django server:**
    ```sh
    python manage.py runserver
    ```
    The application will be available at `http://127.0.0.1:8000/`.

2.  **To run the Flask microservice:**
    (Assuming your Flask app file is named `app.py`)
    ```sh
    python app.py
    ```
    The Flask service will likely run on a different port, such as `http://127.0.0.1:5000/`.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---
