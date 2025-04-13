from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime


# https://api.stackexchange.com/docs/types/search-excerpt
class SearchExcerpt(BaseModel):
    body: str
    creation_date: datetime
    excerpt: str
    item_type: Literal["question", "answer"]
    last_activity_date: datetime
    score: int
    title: str

    # Optional fields
    answer_count: Optional[int] = None
    answer_id: Optional[int] = None
    closed_date: Optional[datetime] = None
    community_owned_date: Optional[datetime] = None
    equivalent_tag_search: Optional[List[str]] = None
    has_accepted_answer: Optional[bool] = None
    is_accepted: Optional[bool] = None
    is_answered: Optional[bool] = None
    locked_date: Optional[datetime] = None
    question_id: Optional[int] = None
    question_score: Optional[int] = None
    tags: Optional[List[str]] = None


class SearchExcerpts(BaseModel):
    each_item: List[SearchExcerpt]
