Event-Driven Trading System

This project implements an event-driven trading system using Python. It simulates the basic components of a trading platform, where events like price updates, trade orders, and trade executions are dispatched and handled through listeners. The system is composed of several classes that handle different events and interactions between the trader, trade engine, and exchange.

Project Overview

Key Components:
Event: A base class for all events in the system.
EventDispatcher: A central dispatcher that manages the events and dispatches them to the appropriate listeners.
Exchange: Simulates a stock or cryptocurrency exchange that generates random price updates and dispatches them to listeners.
Trader: Represents a trader who places buy/sell orders and can set stop-loss orders. The trader receives notifications about trades and price updates.
TradeEngine: Processes buy/sell orders and stores the trade history. It executes trades based on incoming orders.
Events: Events like TradeOrderEvent, TradeExecutedEvent, and TradeNotificationEvent are dispatched and handled as part of the system’s operation.
Features

Price Updates: The Exchange class sends random price updates for cryptocurrency symbols.
Trade Orders: The Trader class can place buy/sell orders, which are handled by the TradeEngine.
Stop-Loss: Traders can set stop-loss orders to automatically sell if the price drops below a certain threshold.
Event System: The EventDispatcher class listens to and handles various events, such as price updates and trade notifications.
Trade History: The TradeEngine stores and displays a history of executed trades.