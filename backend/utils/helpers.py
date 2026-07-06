from typing import Any


# ================================
# SUCCESS RESPONSE
# ================================
def success_response(data: Any = None, message: str = "Success"):
    return {
        "status": "success",
        "message": message,
        "data": data
    }


# ================================
# ERROR RESPONSE
# ================================
def error_response(message: str = "Error", code: int = 400):
    return {
        "status": "error",
        "message": message,
        "code": code
    }


# ================================
# PAGINATION
# ================================
def paginate(data: list, page: int = 1, limit: int = 10):
    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(data),
        "data": data[start:end]
    }