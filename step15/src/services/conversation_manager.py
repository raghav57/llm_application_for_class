from src.schemas.conversation import (
    ConversationMessage,
    ConversationState
)

from src.config.settings import (
    SUMMARY_TRIGGER_MESSAGES,
    KEEP_RECENT_MESSAGES
)


class ConversationManager:

    def __init__(self, system_prompt, llm_client):

        self.llm = llm_client

        # Initialise conversation state
        self.state = ConversationState(
            messages=[
                ConversationMessage(
                    role="system",
                    content=system_prompt
                )
            ],
            summary=""
        )

    # --------------------------------
    # Add a message to conversation
    # --------------------------------

    def add_message(self, role, content):

        message = ConversationMessage(
            role=role,
            content=content
        )

        self.state.messages.append(message)

        # Check whether summarisation is required
        if role == "assistant":
            self._check_and_summarise()

    # --------------------------------
    # Count conversational messages
    # --------------------------------

    def _get_conversation_messages(self):

        return [
            message
            for message in self.state.messages
            if message.role != "system"
        ]

    # --------------------------------
    # Summarise older conversation
    # --------------------------------

    def _check_and_summarise(self):

        conversation_messages = self._get_conversation_messages()

        if len(conversation_messages) <= SUMMARY_TRIGGER_MESSAGES:
            return

        # Separate older messages and recent messages
        older_messages = conversation_messages[:-KEEP_RECENT_MESSAGES]

        recent_messages = conversation_messages[-KEEP_RECENT_MESSAGES:]

        # Prepare summarisation prompt
        previous_summary = self.state.summary or "No previous summary."

        conversation_text = "\n".join(
            [
                f"{message.role}: {message.content}"
                for message in older_messages
            ]
        )

        summary_prompt = f"""
You are a conversation summarisation assistant.

Create a concise summary of the conversation.

Preserve important information such as:
- User preferences
- Investment horizon
- Risk appetite
- Company-specific information
- Important decisions and concerns

Do not invent information.

Previous summary:
{previous_summary}

Older conversation:
{conversation_text}

Produce an updated summary that preserves important context.
"""

        # Generate updated summary
        updated_summary = self.llm.generate(
            [
                {
                    "role": "user",
                    "content": summary_prompt
                }
            ]
        )

        # Update conversation state
        self.state.summary = updated_summary

        # Retain only the recent messages
        system_message = self.state.messages[0]

        self.state.messages = (
            [system_message] + recent_messages
        )

    # --------------------------------
    # Prepare messages for Ollama
    # --------------------------------

    def get_messages(self):

        messages = []

        # Add original system prompt
        messages.append(
            self.state.messages[0].model_dump()
        )

        # Add conversation summary if available
        if self.state.summary:

            messages.append(
                {
                    "role": "system",
                    "content": (
                        "Summary of earlier conversation:\n"
                        + self.state.summary
                    )
                }
            )

        # Add recent conversation messages
        for message in self.state.messages[1:]:

            messages.append(message.model_dump())

        return messages

    # --------------------------------
    # Access conversation summary
    # --------------------------------

    def get_summary(self):

        return self.state.summary