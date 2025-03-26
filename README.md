# Real-Time Notification System

This project is a Django application built with Django Rest Framework that implements a real-time notification system using Server-Sent Events (SSE). It features two primary models, **Item** and **Order**, and a **Notification** model to store changes and their read status.

## Tasks Completed Given By Deepa
- **Models & CRUD Endpoints**: Created Item and Order models. Any create, update, or delete on these models triggers a notification.
- **Notification Model**: Stores a message, timestamp, and read flag.
- **SSE Endpoint**: Streams notifications in real time.
- **Mark Read Endpoint**: Marks all notifications as read.
- **Deployment**: Deployed on Render; exposed externally via Ngrok.

## Endpoints
- **Items**:  
  `GET/POST /api/items/`  
  `GET/PUT/PATCH/DELETE /api/items/<id>/`
- **Orders**:  
  `GET/POST /api/orders/`  
  `GET/PUT/PATCH/DELETE /api/orders/<id>/`
- **SSE**:  
  `GET /api/sse/`
- **Mark Notifications Read**:  
  `POST /api/notifications/mark-read/`

## Assumptions
- Endpoints are public (no authentication) for demonstration.
- In-memory queue is used for SSE
- Ngrok is used for external access, Earlier before Deployment  But We have hosts the application on Render can Access the endpoint with URl Mention 

**Live URL:**  
[https://sse-6q8w.onrender.com]