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
    items: List[SearchExcerpt]

class Question(BaseModel):
    accepted_answer_id: Optional[int] = None
    answer_count: int
    answers: Optional[List[dict]] = None
    body: str
    bounty_amount: Optional[int] = None
    bounty_closes_date: Optional[datetime] = None
    closed_date: Optional[datetime] = None
    closed_reason: Optional[str] = None
    collectives: Optional[List[dict]] = None
    community_owned_date: Optional[datetime] = None
    content_license: Optional[str] = None
    creation_date: datetime
    is_answered: bool
    last_activity_date: datetime
    last_edit_date: Optional[datetime] = None
    link: str
    locked_date: Optional[datetime] = None
    migrated_from: Optional[dict] = None
    migrated_to: Optional[dict] = None
    owner: Optional[dict] = None
    posted_by_collectives: Optional[List[dict]] = None
    protected_date: Optional[datetime] = None
    question_id: int
    score: int
    tags: List[str]
    title: str
    view_count: int

class SearchQnA(BaseModel):
    items: List[Question]
