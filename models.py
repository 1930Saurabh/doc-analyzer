from pydantic import BaseModel, Field

class Experience(BaseModel):
    company: str
    role: str
    start_date: str | None = None
    end_date: str | None = None
    responsibilities: list[str] = Field(default_factory=list)

class Project(BaseModel):
    title: str
    year: int | None = None
    description: str
    skills: list[str] = Field(default_factory=list)
    outcome: str | None = None

class Education(BaseModel):
    institution: str | None = None
    degree: str | None = None
    level: str | None = None
    period: str | None = None
    year: int | None = None
    percentage: float | None = None

class Candidate(BaseModel):
    name: str
    email: str | None = None
    phone: str | None = None
    summary: str | None = None
    experience: list[Experience] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    skills: list[str] = Field(default_factory=list)
    certificates: list[str] = Field(default_factory=list)
    links: dict = Field(default_factory=dict)

