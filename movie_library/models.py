from dataclasses import dataclass, field
from datetime import datetime
from typing import List

@dataclass
class Movie:
    _id: str
    title: str
    director: str
    year: int
    cast: List[str] = field(default_factory=list)
    series: List[str] = field(default_factory=list)
    last_watched: datetime = None
    rating: int = 0
    tags: List[str] = field(default_factory=list)
    description: List[str] = field(default_factory=list)
    video_link: str = None


@dataclass
class User:
    _id: str
    email: str
    password: str
    movies: List[str] = field(default_factory=list)
    