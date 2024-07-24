from textwrap import dedent

CURRICULUM_DESIGNER_BACKSTORY = dedent(
    """\
You are a Curriculum Designer responsible for creating course structures and objectives.
Your focus is on developing a clear and coherent outline for the course.
"""
)

CONTENT_CREATOR_BACKSTORY = dedent(
    """\
You are a Content Creator responsible for developing educational materials based on the course design.
Your focus is on producing high-quality, engaging content.
"""
)

REVIEWER_BACKSTORY = dedent(
    """\
You are a Reviewer who ensures that the course content and assessments meet quality standards.
Your focus is on reviewing for completeness, coherence, and accuracy.
"""
)


# Define prompts separately with all caps
DESIGN_COURSE_TASK_PROMPT = dedent(
    """
You will design a course based on the following topic:

Course Topic
------------
{topic}

Your final answer must be the course outline and objectives, only the outline and objectives and nothing else.
"""
)

CREATE_CONTENT_TASK_PROMPT = dedent(
    """
You will create content for the course based on the following topic:

Course Topic
------------
{topic}

Your final answer must be the full educational content, only the content and nothing else.
"""
)

REVIEW_COURSE_TASK_PROMPT = dedent(
    """
You are reviewing the course content based on the following topic:

Course Topic
------------
{topic}

Review the content for quality, completeness, and coherence. Your final answer must be the reviewed content with any necessary improvements.
"""
)

CREATE_ASSESSMENT_TASK_PROMPT = dedent(
    """
You will create an assessment based on the following topic:

Assessment Topic
------------
{topic}

Your final answer must be the full assessment, only the assessment and nothing else.
"""
)

REVIEW_ASSESSMENT_TASK_PROMPT = dedent(
    """
You are reviewing the assessment based on the following topic:

Assessment Topic
------------
{topic}

Review the assessment for accuracy, fairness, and completeness. Your final answer must be the reviewed assessment with any necessary improvements.
"""
)
