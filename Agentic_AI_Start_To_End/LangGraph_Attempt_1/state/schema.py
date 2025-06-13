from typing import TypedDict, Optional

class CodeState(TypedDict):
    full_code: str
    part_to_convert: Optional[str]
    converted_code: Optional[str]
    passed_tests: Optional[bool]
