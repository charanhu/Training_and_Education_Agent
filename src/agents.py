from crewai import Agent
from model import WATSONX_LLM
from prompt import (
    CURRICULUM_DESIGNER_BACKSTORY,
    CONTENT_CREATOR_BACKSTORY,
    REVIEWER_BACKSTORY,
)


class CourseAgents:
    def curriculum_designer_agent(self):
        return Agent(
            role="Curriculum Designer",
            goal="Design the course structure and objectives",
            backstory=CURRICULUM_DESIGNER_BACKSTORY,
            llm=WATSONX_LLM,
            allow_delegation=False,
            verbose=True,
        )

    def content_creator_agent(self):
        return Agent(
            role="Content Creator",
            goal="Create educational content based on the course design",
            backstory=CONTENT_CREATOR_BACKSTORY,
            llm=WATSONX_LLM,
            allow_delegation=False,
            verbose=True,
        )

    def reviewer_agent(self):
        return Agent(
            role="Reviewer",
            goal="Review the course content and assessment for quality and completeness",
            backstory=REVIEWER_BACKSTORY,
            llm=WATSONX_LLM,
            allow_delegation=True,
            verbose=True,
        )
