# Event-Driven Trading System

![Trading System Banner](https://via.placeholder.com/1200x300.png?text=Event-Driven+Trading+System)

Welcome to the Event-Driven Trading System! This project implements an event-driven trading platform using Python, simulating the core components of a trading system with real-time events like price updates, trade orders, and executions.

---

## PROJECT OVERVIEW

### Key Components:
- **Event**: A base class for all events in the system.
- **EventDispatcher**: The central dispatcher that manages events and sends them to listeners.
- **Exchange**: Simulates a cryptocurrency exchange that generates random price updates.
- **Trader**: Represents a trader who places buy/sell orders and sets stop-loss orders.
- **TradeEngine**: Executes trades and stores trade history.
- **Events**: Key events like `TradeOrderEvent`, `TradeExecutedEvent`, and `TradeNotificationEvent` are dispatched and processed.

---

## FEATURES ✨

- **Price Updates** : The `Exchange` class sends random price updates for cryptocurrency symbols.
- **Trade Orders** : The `Trader` class can place buy/sell orders which are handled by the `TradeEngine`.
- **Stop-Loss** : Traders can set stop-loss orders to sell automatically if the price drops below a certain threshold.
- **Event System** : The `EventDispatcher` class listens to and handles various events (e.g., price updates, trade notifications).
- **Trade History** : The `TradeEngine` stores and displays a history of executed trades.

---
