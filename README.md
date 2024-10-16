# 🛠️ open_scripts

**open_scripts** is a Python Django application designed to host various apps for different use cases. The project aims to streamline and automate tasks by integrating multiple functionalities under one platform.

## 📦 Current Apps

### 1. 💬 LinkedIn App

The first app in this project helps generate LinkedIn contributions based on user details. It leverages a Large Language Model (LLM) to craft thoughtful and engaging LinkedIn posts, making it easier for users to share insights and updates effectively.

## ⚙️ Why Django?

I chose Django as the framework for this project because of its simplicity and robust features:

-   📝 **Ease of Use**: Django provides a clean and straightforward way to build web applications, reducing the complexity of development.
-   🖊️ **Quick Form Creation**: With Django, creating forms to capture user input is intuitive and efficient.
-   🗄️ **ORM Functionalities**: Django's ORM (Object-Relational Mapping) makes it easy to work with databases without writing complex SQL queries.
-   🚀 **Fast Deployment**: Django allows for quick and easy deployment, making it possible to get your app up and running in no time.

## 🏃‍♂️ Getting Started

1. **Clone the repository**:
    ```bash
    git clone https://github.com/akshatsingh1718/open_scripts.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd open_scripts
    ```
3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **API credentials in .env**:
   Copy example.env to .env file and set your api credentials in it.
    ```bash
    cp example.env .env
    ```
5. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

## 🏗️ Tech used

-   `langchain`
-   `Open Ai`
-   `tailwind-css`

## 🌱 Future Plans

-   ➕ Add more apps to extend the capabilities of **open_scripts**, including features for automation, data processing, and more.

## 🤝 Contributing

Feel free to submit issues or pull requests to improve the project.
