from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.db import get_db
from database.models.user import User
from datetime import datetime

router = APIRouter()

# ================================
# GET ALL USERS
# ================================
@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()

    return {
        "count": len(users),
        "users": [
            {
                "id": u.id,
                "username": u.username,
                "email": u.email
            }
            for u in users
        ]
    }


# ================================
# GET USER PROFILE
# ================================
@router.get("/{username}")
def get_user_profile(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "created_at": getattr(user, "created_at", None),
        "fetched_at": datetime.now().isoformat()
    }


# ================================
# UPDATE USER EMAIL
# ================================
@router.put("/update/{username}")
def update_user(username: str, email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.email = email
    db.commit()

    return {
        "message": "User updated successfully",
        "username": username,
        "new_email": email
    }


# ================================
# DELETE USER
# ================================
@router.delete("/delete/{username}")
def delete_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {
        "message": f"{username} deleted successfully"
    }


# ================================
# USER COUNT
# ================================
@router.get("/stats/count")
def user_count(db: Session = Depends(get_db)):
    count = db.query(User).count()

    return {
        "total_users": count
    }