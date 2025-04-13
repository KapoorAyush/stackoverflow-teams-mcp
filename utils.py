from pydantic import BaseModel
from typing import List, Optional, Union


class SearchResultBase(BaseModel):
    """Base class for all search result models."""

    title: str
    snippet: str
    tags: List[str]
    owner: dict  # Using dict instead of UserSummaryResponseModel for simplicity
    creationDate: str
    score: int
    webUrl: str


class QuestionSearchResult(SearchResultBase):
    """Question search result model."""

    type: str = "question"
    questionId: int
    answerCount: int
    hasAcceptedAnswer: bool
    viewCount: int


class AnswerSearchResult(SearchResultBase):
    """Answer search result model."""

    type: str = "answer"
    answerId: int
    parentQuestionId: int
    isAccepted: bool


class ArticleSearchResult(SearchResultBase):
    """Article search result model."""

    type: str = "article"
    articleId: int
    viewCount: int
    articleType: str
    readTimeInMinutes: Optional[int] = None


class PaginatedSearchResults(BaseModel):
    """Paginated search results container."""

    totalCount: int
    pageSize: int
    page: int
    totalPages: int
    sort: Optional[str]  # Referencing SearchSortParameter
    items: List[Union[QuestionSearchResult, AnswerSearchResult, ArticleSearchResult]]
    type: str
