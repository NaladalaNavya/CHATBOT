# 🍔 AI-Powered Food Ordering Assistant (FastAPI + Dialogflow)

This project is a conversational food ordering system built using **FastAPI** and integrated with **Dialogflow**. It enables users to interact with a chatbot to place, modify, and track food orders using natural language.


## 🚀 Features

- 🧠 **NLP Integration**: Uses Dialogflow to interpret user intents like adding, removing, completing, or tracking an order.
- 🛒 **Order Management**:
  - Add multiple food items with quantities.
  - Remove specific items from an ongoing order.
  - Complete and place the order to the backend.
- 🔍 **Order Tracking**: Retrieve the status of your order using the order ID.
- 🧾 **Session Handling**: Manages individual user sessions using Dialogflow context session IDs.
- 💾 **Database Integration**:
  - Stores order details and item-wise quantities.
  - Tracks order status (`in progress`, etc.).
  - Calculates total price of the order.

## 🛠 Tech Stack

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/)
- **NLP Platform**: [Dialogflow](https://dialogflow.cloud.google.com/)
- **Language**: Python
- **Database**: (Connected via a `db_helper` module)
- **Utility**: Custom `generic_helper` module for session and formatting utilities

## 📦 Project Structure

```
.
├── main.py               # FastAPI application entry point
├── db_helper.py          # DB functions: insert, fetch, track orders
├── generic_helper.py     # Utility functions (e.g., session extraction, formatting)
├── requirements.txt      # Python dependencies
├── .gitignore
└── README.md
```

## 📌 Sample Conversation Flow

User: I want 2 burgers and 1 coke.
Bot: So far you have: 2 burgers, 1 coke. Do you need anything else?

User: Remove coke.
Bot: Removed coke from your order! Here is what is left in your order: 2 burgers.

User: Place my order.
Bot: Awesome. We have placed your order.
     Here is your order id #123.
     Your order total is $12. You can pay at the time of delivery!

## 📈 Future Enhancements

- Payment gateway integration
- Real-time order updates
- Admin dashboard for restaurant view
- User authentication

## 📬 License

This project is open-source and available under the [MIT License](LICENSE).

## 🙌 Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [Dialogflow](https://cloud.google.com/dialogflow)
