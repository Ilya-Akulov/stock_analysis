from dataclasses import dataclass, field
from typing import Optional, List


@dataclass
class BaseParser:
    date_from: Optional[str] = None
    date_to: Optional[str] = None

    # Токены акций взятые с сайта https://fin-plan.org/
    stock_tokens: List[str] = field(default_factory=lambda: ['SBER', 'YNDX',
                                                             'ROSN', 'PIKK',
                                                             'NVTK', 'MTLR',
                                                             'AVAZ'])
