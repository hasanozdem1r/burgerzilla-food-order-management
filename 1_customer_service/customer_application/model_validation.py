"""
This script is used to validate models
Hasan Özdemir 02-19-2022
"""
# path : # path : root/1_customer_service/customer_application/model_validation.py
from pydantic import BaseModel, Field


class Customer(BaseModel):
    c_email: str = Field(..., required=True, description="Email", regex="^.+@.+$")
    c_full_name: str = Field(
        ..., required=True, description="Full Name", regex="\w*\d*\s*"
    )
    c_address: str = Field(..., required=True, description="Address")
    c_city: str
    c_postal_code: int
    c_phone_number: str

    # the Config class is used to provide configurations to Pydantic
    class Config:
        # allow reading arbitrary object with attributes
        orm_mode = True


if __name__ == "__main__":
    customer_obj = {
        "c_email":"hasan@hasan.com",
        "c_full_name":"Hasan Ozdemir",
        "c_address":"XYZ Str, KLM",
        "c_city":"KLM",
        "c_postal_code":12345,
        "c_phone_number":"0123456789",
    }
    if Customer(**customer_obj):
        pass
