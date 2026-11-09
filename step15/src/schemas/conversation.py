from pydantic import BaseModel, Field
from typing import Literal


class ConversationMessage(BaseModel):
    role: Literal["system", "user", "assistant"]

    content: str = Field(
        min_length=1,
        description="Text content of the conversation message"
    )


class ConversationState(BaseModel):
    messages: list[ConversationMessage] = Field(
        default_factory=list,
        description="Messages maintained during the conversation"
    )

    summary: str = Field(
        default="",
        description="Summary of older conversation history"
    )