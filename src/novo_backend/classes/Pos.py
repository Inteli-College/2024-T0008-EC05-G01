import pydantic

class Pos(pydantic.BaseModel):
	x: float
	y: float
	z: float
	r: float