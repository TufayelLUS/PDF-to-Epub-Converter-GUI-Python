from typing import Any

class ImagingCore:
    def __getitem__(self, index: int) -> float: ...
    def __getattr__(self, name: str) -> Any: ...

class ImagingFont:
    def __getattr__(self, name: str) -> Any: ...

class ImagingDraw:
    def __getattr__(self, name: str) -> Any: ...

class PixelAccess:
    def __getitem__(self, xy: tuple[int, int]) -> float | tuple[int, ...]: ...
    def __setitem__(
        self, xy: tuple[int, int], color: float | tuple[int, ...]
    ) -> None: ...

class ImagingDecoder:
    def __getattr__(self, name: str) -> Any: ...

class ImagingEncoder:
    def __getattr__(self, name: str) -> Any: ...

class _Outline:
    def close(self) -> None: ...
    def __getattr__(self, name: str) -> Any: ...

def font(image: ImagingCore, glyphdata: bytes) -> ImagingFont: ...
def outline() -> _Outline: ...
def __getattr__(name: str) -> Any: ...
