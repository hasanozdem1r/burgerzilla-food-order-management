from models import CustomerOrm
from pydantic import BaseModel,Field


class Customer(BaseModel):
    c_email:str=Field(...,required=True,description="Email",regex="^.+@.+$")
    c_full_name:str=Field(...,required=True,description="Full Name",regex="\w*\d*\s*")
    c_address:str=Field(...,required=True,description="Address")
    c_city:str
    c_postal_code:int
    c_phone_number:str

    # the Config class is used to provide configurations to Pydantic
    class Config:
        # allow reading arbitrary object with attributes
        orm_mode = True



if __name__=='__main__':
    customer_obj=CustomerOrm(
        c_email="hasan@hasan.com",
        c_full_name="Hasan Ozdemir",
        c_address="XYZ Str, KLM",
        c_city="KLM",
        c_postal_code=12345,
        c_phone_number="0123456789"
    )
    if Customer.from_orm(customer_obj):
        print("VALID")