from pydantic import BaseModel, Field
from typing import Optional, List



class Movie(BaseModel):
	id: Optional[int] = None
	title: str = Field(max_length=50)
	overview: str = Field(max_length=150, min_length=5)
	year: int = Field(le=2023)
	rating: float = Field(ge=1, le=10)
	category: str = Field(max_length=30)

	class Config:
         schema_extra = {
			"example":{
				"id": 0,
                "title": "My movie",
				"overview": "Description of the movie",
				"year": 2023,
				"rating": 10,
				"category": "Familiar"
			}
		 }


# Movie Title: The Shawshank Redemption 
# Overview: Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency. 
# Year: 1994 
# Rating: 9.3/10 
# Category: Drama