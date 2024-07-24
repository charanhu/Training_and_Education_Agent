from crewai import Task
from prompt import (
    DESIGN_COURSE_TASK_PROMPT,
    CREATE_CONTENT_TASK_PROMPT,
    REVIEW_COURSE_TASK_PROMPT,
    CREATE_ASSESSMENT_TASK_PROMPT,
    REVIEW_ASSESSMENT_TASK_PROMPT,
)


class CourseTasks:
    def design_course_task(self, agent, topic):
        return Task(
            description=DESIGN_COURSE_TASK_PROMPT.format(topic=topic),
            agent=agent,
            expected_output="Course outline and objectives",
        )

    def create_content_task(self, agent, topic):
        return Task(
            description=CREATE_CONTENT_TASK_PROMPT.format(topic=topic),
            agent=agent,
            expected_output="Full educational content",
        )

    def review_course_task(self, agent, topic):
        return Task(
            description=REVIEW_COURSE_TASK_PROMPT.format(topic=topic),
            agent=agent,
            expected_output="Reviewed course content",
        )

    def create_assessment_task(self, agent, topic):
        return Task(
            description=CREATE_ASSESSMENT_TASK_PROMPT.format(topic=topic),
            agent=agent,
            expected_output="Full assessment",
        )

    def review_assessment_task(self, agent, topic):
        return Task(
            description=REVIEW_ASSESSMENT_TASK_PROMPT.format(topic=topic),
            agent=agent,
            expected_output="Reviewed assessment",
        )
