from pydantic import BaseModel, Field
from typing import Optional, List


class User(BaseModel):
	email:str
	password:str
