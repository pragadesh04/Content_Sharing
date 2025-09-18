# Content Sharing & Sales Platform (FastAPI + MongoDB)

This project is an **automation system** for managing **online content sharing (courses, events, workshops)** and **product sales**.  
It is built with **FastAPI**, **MongoDB**, and will integrate with messaging/payment platforms for smoother operations.

---

## 🚧 Development Status

### Currently in Development

- ✅ Admin-side application (course/content creation, participant management, payments, reminders)  
- 🔄 User-side application (registration, payments, joining sessions) → *in progress*  
- 🔮 Future integrations: Telegram Bot API, Payment Gateway, Shipping APIs

---

## ✨ Features (Planned)

### Admin Side (Implemented)

- Admin registration & login (JWT-based authentication)  
- Create, update, delete courses/content  
- View and approve participants  
- Manage payments (status updates)  
- Send Google Meet/Telegram links to participants  
- Send session reminders automatically  

### User Side (In Progress)

- User registration for sessions  
- Submit payment proof / automated payment verification  
- Receive session details & joining links  
- Get reminders via WhatsApp/Telegram/email  

### Future Enhancements

- Product sales workflow (order, address, payment, shipment)  
- Telegram bot integration for reminders & links  
- Payment gateway integration (Razorpay/UPI)  
- Recording and sharing session replays (VOD integration)

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)  
- **Database:** MongoDB  
- **Authentication:** JWT (using python-jose & passlib)  
- **Messaging (planned):** Telegram Bot API, WhatsApp Business API  
- **Payments (planned):** Razorpay / GPay integration  
- **Deployment (future):** Docker + Cloud Hosting

---

## 🚀 Setup Instructions

1. Clone the repo:

   ```bash
   git clone https://github.com/pragadesh04/Content-Sharing.git
   cd Content-Sharing

2. Create a virtual environment & install dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate    # (Windows)
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:

   ```bash

   uvicorn main:app --reload

   ```

4. Access API docs:
   - Swagger UI → `http://127.0.0.1:8000/docs`  
   - ReDoc → `http://127.0.0.1:8000/redoc`  

---

## 📌 Notes

- This is still an early development version.  
- Admin-side endpoints are available, but user-side features are incomplete.  
- Expect frequent updates & breaking changes until v1.0 release.

---

## 📄 License

This project is licensed under the **MIT License** – feel free to use and modify.

---
