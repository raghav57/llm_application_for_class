import json

from pydantic import ValidationError

from src.schemas.stock_analysis import StockAnalysis


# class ResponseValidator:

#     def validate_stock_analysis(self, response):

#         try:
#             # Convert JSON string into Python dictionary
#             data = json.loads(response)

#             # Validate dictionary using Pydantic
#             validated_data = StockAnalysis.model_validate(data)

#             return validated_data

#         except json.JSONDecodeError as error:

#             raise ValueError(
#                 f"Invalid JSON response: {error}"
#             ) from error

#         except ValidationError as error:

#             raise ValueError(
#                 f"Stock analysis validation failed: {error}"
#             ) from error


# import json

# from pydantic import ValidationError

# from src.schemas.stock_analysis import StockAnalysis



class ResponseValidator:

    def validate_stock_analysis(self, response):

        try:
            # Convert JSON string into Python dictionary
            data = json.loads(response)

            # Validate dictionary using Pydantic
            validated_data = StockAnalysis.model_validate(data)

            return validated_data

        except json.JSONDecodeError as error:

            raise ValueError(
                f"Invalid JSON response: {error}"
            ) from error

        except ValidationError as error:

            raise ValueError(
                f"Stock analysis validation failed: {error}"
            ) from error
