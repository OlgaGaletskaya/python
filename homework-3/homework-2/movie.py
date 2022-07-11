from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Generator, List, Tuple

@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        result = []
        for release in self.dates:
            release_date = release[0]
            while release_date <= release[1]:
                result.append(release_date)
                release_date += timedelta(days=1)
        return result

if __name__ == "__main__":
    m = Movie('sw', [
      (datetime(2020, 1, 1), datetime(2020, 1, 7)),
      (datetime(2020, 1, 15), datetime(2020, 2, 7))
    ])

    for d in m.schedule():
        print(d)