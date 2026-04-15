package com.example.order.service;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import com.example.order.domain.Order;
import com.example.order.repository.OrderRepository;
import java.util.Optional;
import org.junit.jupiter.api.Test;

class OrderServiceTest {

    @Test
    void returns_order_when_found() {
        OrderRepository repository = id -> Optional.of(new Order(id, "CREATED"));
        OrderService service = new OrderService(repository);

        Order order = service.getOrder("order-1");

        assertEquals("order-1", order.getId());
        assertEquals("CREATED", order.getStatus());
    }

    @Test
    void throws_when_order_missing() {
        OrderRepository repository = id -> Optional.empty();
        OrderService service = new OrderService(repository);

        IllegalArgumentException error =
            assertThrows(IllegalArgumentException.class, () -> service.getOrder("missing"));

        assertEquals("Order not found: missing", error.getMessage());
    }
}
