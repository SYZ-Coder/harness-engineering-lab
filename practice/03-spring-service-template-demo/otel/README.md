# OpenTelemetry 接入说明

这个目录展示如何把最小微服务模板继续升级为“可观测的 Harness 样板”。

目标不是在这个 Demo 里完整运行 OTel，而是给出一个足够清楚的接入骨架：

- 运行时通过 Java Agent 注入
- 统一设置 service name
- 指定 OTLP exporter 地址
- 在日志和链路之间建立统一入口

## 推荐接入方式

### 方式 1：Java Agent

启动时添加：

```bash
java ^
  -javaagent:path\\to\\opentelemetry-javaagent.jar ^
  -Dotel.service.name=demo-order-service ^
  -Dotel.exporter.otlp.endpoint=http://localhost:4317 ^
  -jar target/demo-order-service-1.0.0-SNAPSHOT.jar
```

### 方式 2：环境变量

```bash
set OTEL_SERVICE_NAME=demo-order-service
set OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4317
```

## 最小落地建议

先做到三件事：

1. 每个服务有稳定的 `service.name`
2. trace id 能跨服务传递
3. 日志中能关联 trace id

做到这三点，微服务就已经具备最小可观测反馈层。

