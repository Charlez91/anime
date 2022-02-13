from dataclasses import dataclass

@dataclass
class Anime:
    """
    class to model anime data
    """
    mal_id: int
    url: str
    title: str
    image_url: str
    synopsis: str
    type: str
    airing_start: str
    episodes: int
    members: int