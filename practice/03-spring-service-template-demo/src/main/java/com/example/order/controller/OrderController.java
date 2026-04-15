package com.example.order.controller;

import com.example.order.domain.Order;
import com.example.order.service.OrderService;

public class OrderController {
    private final OrderService orderService;

    public OrderController(OrderService orderService) {
        this.orderService = orderService;
    }

    public Order getOrder(String orderId) {
        return orderService.getOrder(orderId);
    }
}
