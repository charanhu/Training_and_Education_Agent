from dotenv import load_dotenv
import os

load_dotenv()

from crewai import Crew
from tasks import CourseTasks
from agents import CourseAgents

tasks = CourseTasks()
agents = CourseAgents()

print("## Welcome to the Training and Education System")
print("-----------------------------------------------")
course_topic = input("What is the topic of the course?\n")
assessment_topic = input("What is the topic of the assessment?\n")

# Create Agents
curriculum_designer_agent = agents.curriculum_designer_agent()
content_creator_agent = agents.content_creator_agent()
reviewer_agent = agents.reviewer_agent()

# Create Tasks
design_course = tasks.design_course_task(curriculum_designer_agent, course_topic)
create_content = tasks.create_content_task(content_creator_agent, course_topic)
review_course = tasks.review_course_task(reviewer_agent, course_topic)
create_assessment = tasks.create_assessment_task(
    content_creator_agent, assessment_topic
)
review_assessment = tasks.review_assessment_task(reviewer_agent, assessment_topic)

# Create Crew responsible for the course
crew = Crew(
    agents=[curriculum_designer_agent, content_creator_agent, reviewer_agent],
    tasks=[
        design_course,
        create_content,
        review_course,
        create_assessment,
        review_assessment,
    ],
    verbose=True,
)

# Perform tasks and save results to markdown files
course_content = crew.kickoff()

# Save results to markdown files
with open("course_results.md", "w") as file:
    file.write("# Training and Education Results\n\n")
    file.write("## Course Design\n")
    file.write("### Course Topic:\n")
    file.write(f"{course_topic}\n\n")
    file.write("### Course Content:\n")
    file.write(course_content.get("design_course", "No content available") + "\n\n")
    file.write("## Course Content Creation\n")
    file.write(course_content.get("create_content", "No content available") + "\n\n")
    file.write("## Course Review\n")
    file.write(course_content.get("review_course", "No content available") + "\n\n")
    file.write("## Assessment Creation\n")
    file.write(course_content.get("create_assessment", "No content available") + "\n\n")
    file.write("## Assessment Review\n")
    file.write(course_content.get("review_assessment", "No content available") + "\n")

print("\n\n########################")
print("## Results saved to 'course_results.md'")
print("########################\n")
