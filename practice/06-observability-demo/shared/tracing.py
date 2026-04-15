"""Minimal tracing helpers for the observability demo."""

import uuid


def generate_trace_id():
    return uuid.uuid4().hex


def ensure_trace_id(trace_id=None):
    return trace_id or generate_trace_id()


def make_log(service_name, trace_id, message):
    return "[service={0}] [trace_id={1}] {2}".format(service_name, trace_id, message)
