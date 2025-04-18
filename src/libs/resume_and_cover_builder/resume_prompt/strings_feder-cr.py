from src.libs.resume_and_cover_builder.template_base import prompt_header_template, prompt_professional_summary_template, prompt_education_template, prompt_working_experience_template, prompt_projects_template, prompt_achievements_template, prompt_certifications_template, prompt_additional_skills_template

prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes, using UK English spelling and terminology. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, and LinkedIn profile. Exclude any information that is not provided.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

- **My information:**  
  {personal_information}
""" + prompt_header_template

prompt_professional_summary = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes, using UK English spelling and terminology. Your task is to create a compelling professional summary that highlights your key qualifications for the job. The summary should:

1. **Summary Paragraph**: Create a concise paragraph (3-4 lines) that demonstrates your relevant skills, experience, and value proposition. Focus on:
   - Your years of relevant experience
   - Key skills that match the job description
   - Notable achievements related to the target role
   - Your unique value proposition
2. **Job Alignment**: Ensure the summary aligns with the job description provided and showcases how your background makes you a strong fit.
3. **Keywords**: Incorporate relevant industry and role-specific keywords to pass ATS screening.

- **My draft summary:**  
  {professional_summary}
  
- **Job Description:**
  {job_description}
""" + prompt_professional_summary_template

prompt_education = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes, using UK English spelling and terminology. Your task is to articulate the educational background for a resume. For each educational entry, ensure you include:

1. **Institution Name and Location**: Specify the university or educational institution's name and location.
2. **Degree and Field of Study**: Clearly indicate the degree earned and the field of study.
3. **Grade**: Include your Grade if it is strong and relevant.
4. **Timeframe**: Include the start and end years of your education.
5. **Relevant Coursework**: Format the provided coursework as 2 crisp bullet points (each 6-8 words) that highlight skills/knowledge directly applicable to the target role.

- **My information:**  
  {education_details}
  
- **Job Description (if available):**
  {job_description}
"""+ prompt_education_template


prompt_working_experience = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes, using UK English spelling and terminology. Your task is to detail the work experience for a resume with a focus on BALANCED presentation of quantifiable impact and soft skills. Follow these guidelines:

1. **Company Name and Location**: Provide the name of the company and its location.
2. **Job Title**: Clearly state your job title.
3. **Dates of Employment**: Include the start and end dates of your employment.
4. **Sentence Length**: Ensure each bullet point is between 12-17 words for optimal readability.
5. **IMPORTANT - BALANCED APPROACH (Quantitative vs. Qualitative)**: 
   - For the most recent job (the Data City), create 5 bullet points:
     * EXACTLY 3 points should include numerical metrics/quantifiable achievements (60%)
     * EXACTLY 2 points should focus on soft skills without numerical metrics (40%)
   - For the second job (Alien Technology Transfer), create 4 bullet points:
     * EXACTLY 2 points should include numerical metrics/quantifiable achievements (50%)
     * EXACTLY 2 points should focus on soft skills without numerical metrics (50%)
   - For other jobs, create 3 bullet points:
     * EXACTLY 2 points should include numerical metrics/quantifiable achievements (67%)
     * EXACTLY 1 point should focus on soft skills without numerical metrics (33%)

6. **Soft Skills Integration**: 
   - Identify key soft skills from the job description (leadership, teamwork, collaboration, communication, etc.)
   - Explicitly showcase these soft skills in the non-numerical bullet points
   - Use action verbs and specific examples to demonstrate these soft skills
   - Avoid vague claims and ensure each soft skill is tied to a specific achievement or responsibility

7. **Keyword Integration**:
   - Identify and prioritize keywords from the job description
   - Incorporate as many relevant keywords as possible across both numerical and soft skill points
   - Flag any remaining keywords that couldn't be integrated into work experience to be added to the additional skills section

- **My information:**  
  {experience_details}
  
- **Job Description:**
  {job_description}
"""+ prompt_working_experience_template


prompt_projects = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to highlight notable side projects. For each project, ensure you include:

1. **Project Name and Link**: Provide the name of the project and include a link to the GitHub repository or project page.
2. **Project Details**: Describe any notable recognition or achievements related to the project, such as GitHub stars or community feedback.
3. **Technical Contributions**: Highlight your specific contributions and the technologies used in the project. 

- **My information:**  
  {projects}
"""+ prompt_projects_template


prompt_achievements = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes, using UK English spelling and terminology. Your task is to list significant achievements. For each achievement, ensure you include:

1. **Award or Recognition**: Clearly state the name of the award, recognition, scholarship, or honor.
2. **Description**: Provide a brief description of the achievement and its relevance to your career or academic journey.
3. **Important Note**: Only include the first 2 achievements from the list provided. Do not include any additional achievements beyond these 2.

- **My information:**  
  {achievements}
"""+ prompt_achievements_template


prompt_certifications = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant certifications based on the provided details. For each certification, ensure you include:

1. **Certification Name**: Clearly state the name of the certification.
2. **Description**: Provide a brief description of the certification and its relevance to your professional or academic career.

Ensure that the certifications are clearly presented and effectively highlight your qualifications.

To implement this:

If any of the certification details (e.g., descriptions) are not provided (i.e., None), omit those sections when filling out the template.

- **My information:**  
  {certifications}

"""+ prompt_certifications_template


prompt_additional_skills = """
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes, using UK English spelling and terminology. Your task is to list additional skills relevant to the job. Follow these guidelines:

1. **Keyword Alignment**: 
   - Review any keywords from the job description that weren't included in the work experience.
   - Prioritize these keywords for inclusion in the additional skills section.
2. **Skill Organization**:
   - Group similar skills into logical categories.
   - List technical skills, soft skills, and languages separately.
3. **Relevance**: Ensure all listed skills are relevant to the target position.

- **My information:**  
  {languages}
  {interests}
  {skills}
  
- **Job Description:**
  {job_description}
"""+ prompt_additional_skills_template
