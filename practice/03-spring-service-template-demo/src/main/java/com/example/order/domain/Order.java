package com.example.order.domain;

public final class Order {
    private final String id;
    private final String status;

    public Order(String id, String status) {
        this.id = id;
        this.status = status;
    }

    public String getId() {
        return id;
    }

    public String getStatus() {
        return status;
    }
}
