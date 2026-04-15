package com.example.order.service;

import org.springframework.stereotype.Service;

@Service
public class LegacyOrderService {

    private final OrderRepository orderRepository;

    public LegacyOrderService(OrderRepository orderRepository) {
        this.orderRepository = orderRepository;
    }

    public Order findById(String orderId) {
        return orderRepository.findById(orderId);
    }
}
