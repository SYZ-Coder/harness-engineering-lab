package com.example.order.repository;

import com.example.order.domain.Order;
import java.util.Optional;

public interface OrderRepository {
    Optional<Order> findById(String id);
}
