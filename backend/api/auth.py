from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.db import get_db
from database.models.user import User
from database.schemas.user import UserCreate, UserLogin
from utils.auth_utils import hash_password, verify_password, create_token

# ❌ IMPORTANT: prefix यहाँ मत लगाओ
router = APIRouter(tags=["Auth"])


# -------------------------------
# REGISTER
# -------------------------------
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.username == user.username).first()

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists"
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    try:
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {
            "status": "success",
            "message": "User registered successfully",
            "user_id": new_user.id
        }

    except Exception:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Registration failed"
        )


# -------------------------------
# LOGIN
# -------------------------------
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    if not verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )

    token = create_token({"sub": db_user.username})

    return {
        "status": "success",
        "access_token": token,   # ✅ frontend यही लेगा
        "token_type": "bearer"
    }


# -------------------------------
# GET ALL USERS
# -------------------------------
@router.get("/users")
def get_users(db: Session = Depends(get_db)):
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


# -------------------------------
# DELETE USER
# -------------------------------
@router.delete("/delete/{username}")
def delete_user(username: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {
        "status": "success",
        "message": f"{username} deleted successfully"
    }
