from pydantic import BaseModel, Field, ConfigDict


class UserEntrySchema(BaseModel):

    model_config = ConfigDict(extra='forbid')

    OverallQual: int = Field(
        ...,
        ge=1, le=10,
        description="Overall material and finish quality of the house (1: Very Poor to 10: Very Excellent)"
    )

    GrLivArea: int = Field(
        ...,
        gt=0,
        description="Above grade (ground) living area in square feet"
    )

    TotalBsmtSF: float = Field(
        ...,
        ge=0,
        description="Total square feet of the basement area"
    )

    FullBath: int = Field(
        ...,
        ge=0,
        description="Number of full bathrooms above ground"
    )

    TotRmsAbvGrd: int = Field(
        ..., 
        gt=0, 
        description="Total number of rooms above ground (excluding bathrooms)"
    )

    YearBuilt: int = Field(
        ...,
        description="Original construction year of the house"
    )

    GarageCars: int = Field(
        default=0, 
        ge=0, 
        description="Size of the garage in terms of car capacity"
    )
    
    GarageArea: int = Field(
        default=0, 
        ge=0, 
        description="Total area of the garage in square feet"
    )