from pydantic import BaseModel, Field, computed_field
from typing import Annotated, Literal


class Customer(BaseModel):
    gender : Annotated[Literal['Male', 'Female'] , Field(...,description='Give gender of the customer',title="Gender")]

    Partner : Annotated[Literal['Yes', 'No'] , Field(...,description='Is a partner or not',title="Partner")]

    Dependents : Annotated[Literal['Yes', 'No'] , Field(...,description='Is a dependent or not',title="Dependents")]

    PhoneService : Annotated[Literal['Yes', 'No'] , Field(...,description='Has a phone service or not',title="Phone Service")]

    MultipleLines : Annotated[Literal['Yes', 'No', 'No Phone Service'] , Field(...,description='Has multiple lines service or not',title="Multiple Lines")]

    InternetService : Annotated[Literal['DSL','Fiber Optic', 'No'] , Field(...,description='Subscription for Internet service',title="Internet Service")]

    OnlineSecurity : Annotated[Literal['Yes', 'No', 'No Internet Service'] , Field(...,description='Subscribed for Online Security or not',title="Online Security")]

    OnlineBackup : Annotated[Literal['Yes', 'No', 'No Internet Service'] , Field(...,description='Subscribed for Online Backup or not',title="Online Backup")]

    DeviceProtection : Annotated[Literal['Yes', 'No', 'No Internet Service'] , Field(...,description='Subscribed for Device Security or not',title="Device Protection")]

    TechSupport : Annotated[Literal['Yes', 'No', 'No Internet Service'] , Field(...,description='Subscribed for Technical Support or not',title="Tech Support")]

    StreamingTV : Annotated[Literal['Yes', 'No', 'No Internet Service'] , Field(...,description='Streaming TV or not',title="Streaming TV")]

    StreamingMovies : Annotated[Literal['Yes', 'No', 'No Internet Service'] , Field(...,description='Streaming Movies or not',title="Streaming Movies")]

    Contract : Annotated[Literal['One year', 'Two year', 'Month-to-month'] , Field(...,description='Customer contract with company / Subscription type',title="Contract")]

    PaperlessBilling : Annotated[Literal['Yes', 'No'] , Field(...,description='Paperless Billing or not',title="Paperless Billing")]

    PaymentMethod : Annotated[Literal['Mailed check', 'Credit card (automatic)', 'Electronic check', 'Bank transfer (automatic)'] , Field(...,description='Payment Method',title="Method of payment")]

    SeniorCitizen : Annotated[Literal[0, 1], Field(..., description="is customer a Senior Citizen - 1 for yes and 0 for no", title="Senior Citizen")]

    tenure : Annotated[int, Field(..., description="Total tenure of subscription", gt=0, title="Tenure")]

    MonthlyCharges : Annotated[float, Field(..., description="Amount of monthly charge", gt=0, title="Monthly Charge")]

    TotalCharges : Annotated[float, Field(..., description="Total amount of charges", gt=0, title="Total Charge")]

    
    @computed_field
    @property
    def AverageCharges(self) -> float:
        avg_charges = self.TotalCharges/(self.tenure + 1)
        return avg_charges
    
    @computed_field
    @property
    def ServiceSupport(self) -> int:
        online_security = 1 if self.OnlineSecurity == 'Yes' else 0
        online_backup = 1 if self.OnlineBackup == 'Yes' else 0
        tech_support = 1 if self.TechSupport == 'Yes' else 0
        device_protection = 1 if self.DeviceProtection == 'Yes' else 0

        return online_backup + online_security + tech_support + device_protection
    
    @computed_field
    @property
    def StreamService(self) -> int:
        stream_tv = 1 if self.StreamingTV == 'Yes' else 0
        stream_movies = 1 if self.StreamingMovies == 'Yes' else 0
        
        return stream_movies + stream_tv

    @computed_field
    @property
    def trusted(self) -> int:
        contract = 0 if self.Contract == 'Month-to-month' else 1
        payment = 1 if self.PaymentMethod == 'Credit card (automatic)' or self.PaymentMethod == 'Bank transfer (automatic)' else 0
        
        return contract + payment