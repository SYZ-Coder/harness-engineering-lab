package com.example.order.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LegacyOrderService {

    @Autowired
    private OrderRepository orderRepository;

    public Order findById(String orderId) {
        return orderRepository.findById(orderId);
    }
}
