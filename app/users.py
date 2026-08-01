from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.database import get_connection
from app.security import hash_password, verify_password
from app.auth import create_access_token


router = APIRouter()



class UserRegister(BaseModel):

    name: str
    email: str
    password: str



class UserLogin(BaseModel):

    email: str
    password: str




@router.post("/register")
def register(user: UserRegister):

    conn = get_connection()

    cursor = conn.cursor()


    hashed_password = hash_password(user.password)


    try:

        cursor.execute("""
        INSERT INTO users
        (name, email, password)
        VALUES (?, ?, ?)
        """,
        (
            user.name,
            user.email,
            hashed_password
        ))


        conn.commit()


    except Exception:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )


    finally:

        conn.close()



    return {
        "message": "User registered successfully"
    }




@router.post("/login")
def login(user: UserLogin):

    conn = get_connection()

    cursor = conn.cursor()


    cursor.execute("""
    SELECT *
    FROM users
    WHERE email = ?
    """,
    (user.email,))


    db_user = cursor.fetchone()


    conn.close()


    if not db_user:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )



    if not verify_password(
        user.password,
        db_user[3]
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid password"
        )



    token = create_access_token(
        {
            "user_id": db_user[0],
            "email": db_user[2]
        }
    )


    return {
        "access_token": token,
        "token_type": "bearer"
    }