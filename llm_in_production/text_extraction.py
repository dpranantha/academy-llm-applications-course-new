import pydantic


class DigitFeature(pydantic.BaseModel):
    quotes: list[str] | None = pydantic.Field(
        default=None,
        description="The exact sentences that contain the value. This property is None if the feature was not found in the description.",
    )
    value: int | None = pydantic.Field(
        default=None,
        description="The exact integer value in the sentences. This property is None if the feature was not found in the description",
    )


class StringFeature(pydantic.BaseModel):
    thoughts: str = pydantic.Field(
        description="Here you write your thought and reasoning about your observations that will help you determine the value."
    )
    quotes: list[str] = pydantic.Field(
        description="The exact sentences or fragments where you got the answer from. \
            This property can contain indirect evidence if the value is inferred."
    )
    value: str | None = pydantic.Field(
        description="The exact value in the sentences or inferred context. This property is None if the feature was not found in the description."
    )

    @pydantic.model_validator(mode="after")
    def validate_quotes_and_thoughts(self) -> "StringFeature":
        if (
            self.value is not None
            and len(self.quotes) == 0
            and not self.thoughts.strip()
        ):
            raise ValueError(
                "If there are no quotes, the `thoughts` field must explain the inference clearly."
            )
        return self


class BooleanFeature(pydantic.BaseModel):
    quotes: list[str] | None = pydantic.Field(
        default=None,
        description="The exact sentences that contain the value. This property is None if the feature was not found in the description.",
    )
    value: bool | None = pydantic.Field(
        default=None,
        description="Whether the house has this feature. This property is None if the feature was not found in the description",
    )
