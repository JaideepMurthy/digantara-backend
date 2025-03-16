# Digantara Backend API  

## Overview  
The **Digantara Backend API** is a FastAPI-based project designed to demonstrate efficient **Data Structures & Algorithms (DSA)** implementations. This API provides endpoints for fundamental algorithms and includes logging, storage, and error handling mechanisms to enhance usability.  

## Features  
- **Algorithm Implementations**  
  - **Binary Search**: Searches for an element in a sorted list.  
  - **Quick Sort**: Sorts an array using the divide-and-conquer approach.  
  - **Breadth-First Search (BFS)**: Traverses a graph or tree structure.  

- **Logging & Storage**  
  - Each API call is logged (Algorithm name, Input, Output) to prevent redundant computations.  

- **Error Handling & Edge Cases**  
  - Validates inputs and gracefully handles invalid cases.  

- **User-Friendly API Documentation**  
  - Swagger UI available at [`/docs`](http://127.0.0.1:8000/docs).  
  - ReDoc documentation at [`/redoc`](http://127.0.0.1:8000/redoc).  

- **Deployment & Scalability**  
  - Dockerized for easy deployment.  
  - Configured for cloud deployment using services like **Render** or **Railway**.  

---

## Installation & Setup  

### Prerequisites  
Ensure you have the following installed:  
- **Python 3.8+** → [Download Python](https://www.python.org/downloads/)  
- **Git** → [Download Git](https://git-scm.com/downloads)  
- **Virtual Environment** (Optional but recommended)  

### Clone the Repository  
```sh
git clone https://github.com/JaideepMurthy/digantara-backend.git
cd digantara-backend


## Installation & Setup
python -m venv venv
source venv/bin/activate    On macOS/Linux
venv\Scripts\activate       On Windows

Install Dependencies - pip install -r requirements.txt
Run the API Locally  - uvicorn main:app --host 0.0.0.0 --port 8000 --reload

The API will be available at: http://127.0.0.1:8000
API Documentation: http://127.0.0.1:8000/docs


## Contributing
Feel free to open issues or submit pull requests for improvements.

👨‍💻 Author: Jaideep Murthy
📅 License: MIT