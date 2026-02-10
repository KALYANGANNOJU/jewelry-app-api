from pydantic import BaseModel, EmailStr
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    category: Optional[str] = None
    price: float
    discount_price: Optional[float] = None
    metal: Optional[str] = None
    polish: Optional[str] = None
    rating: Optional[float] = 0.0
    image_url: Optional[str] = None

class ProductCreate(ProductBase):
    pass

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        from_attributes = True

class CategoryBase(BaseModel):
    name: str
    image_url: Optional[str] = None

class CategoryResponse(CategoryBase):
    id: int
    
    class Config:
        from_attributes = True

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    
    class Config:
        from_attributes = True