"""
Database Schemas

Define your MongoDB collection schemas here using Pydantic models.
These schemas are used for data validation in your application.

Each Pydantic model represents a collection in your database.
Model name is converted to lowercase for the collection name:
- User -> "user" collection
- Product -> "product" collection
- BlogPost -> "blogs" collection
"""

from pydantic import BaseModel, Field
from typing import Optional, List

# Example schemas (you can keep these for reference):

class User(BaseModel):
    """
    Users collection schema
    Collection name: "user" (lowercase of class name)
    """
    name: str = Field(..., description="Full name")
    email: str = Field(..., description="Email address")
    address: str = Field(..., description="Address")
    age: Optional[int] = Field(None, ge=0, le=120, description="Age in years")
    is_active: bool = Field(True, description="Whether user is active")

class Product(BaseModel):
    """
    Products collection schema
    Collection name: "product" (lowercase of class name)
    """
    title: str = Field(..., description="Product title")
    description: Optional[str] = Field(None, description="Product description")
    price: float = Field(..., ge=0, description="Price in rupees")
    category: str = Field(..., description="Product category")
    in_stock: bool = Field(True, description="Whether product is in stock")

# Housekeeping app schemas

class Service(BaseModel):
    """
    Housekeeping services offered
    Collection name: "service"
    """
    name: str = Field(..., description="Service name, e.g., Deep Cleaning")
    description: str = Field(..., description="Short description of the service")
    price_inr: int = Field(..., ge=0, description="Starting price in INR")
    unit: str = Field(..., description="Unit for pricing, e.g., per BHK, per visit")
    category: str = Field(..., description="Category, e.g., Cleaning, Pest Control")
    popular: bool = Field(False, description="Mark as popular service")

class Booking(BaseModel):
    """
    Customer booking/inquiry details
    Collection name: "booking"
    """
    customer_name: str = Field(..., description="Customer full name")
    phone: str = Field(..., description="Indian phone number")
    email: Optional[str] = Field(None, description="Customer email")
    address: str = Field(..., description="Service address")
    city: str = Field(..., description="City")
    pincode: str = Field(..., description="PIN code")
    service_id: Optional[str] = Field(None, description="Selected service id")
    service_name: str = Field(..., description="Selected service name")
    preferred_date: str = Field(..., description="Preferred date (YYYY-MM-DD)")
    preferred_time: str = Field(..., description="Preferred time slot, e.g., Morning")
    notes: Optional[str] = Field(None, description="Additional notes")
    source: str = Field("web", description="Source of booking")
