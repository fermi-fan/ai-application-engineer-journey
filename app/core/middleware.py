from __future__ import annotations

import time
import uuid
import logging
from typing import Callable

from fastapi import Request, Response

logger = logging.getLogger("http")


async def request_logging_middleware(request: Request, call_next: Callable) -> Response:
    t0 = time.perf_counter()

    # Prefer incoming request id if present
    request_id = request.headers.get("X-Request-ID") or uuid.uuid4().hex
    request.state.request_id = request_id

    status_code = 500
    try:
        response: Response = await call_next(request)
        status_code = response.status_code
        return response
    finally:
        latency_ms = int((time.perf_counter() - t0) * 1000)

        # Ensure response carries request id (even if exception happens, may not be available)
        try:
            # response may not exist if exception before response creation
            if "response" in locals():
                response.headers["X-Request-ID"] = request_id
        except Exception:
            pass

        logger.info(
            "http.request",
            extra={
                "extra": {
                    "request_id": request_id,
                    "method": request.method,
                    "path": request.url.path,
                    "query": request.url.query,
                    "status_code": status_code,
                    "latency_ms": latency_ms,
                    "client": request.client.host if request.client else None,
                }
            },
        )
