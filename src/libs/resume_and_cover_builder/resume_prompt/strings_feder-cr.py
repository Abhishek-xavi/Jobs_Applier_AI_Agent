from src.libs.resume_and_cover_builder.template_base import prompt_header_template, prompt_professional_summary_template, prompt_education_template, prompt_working_experience_template, prompt_projects_template, prompt_achievements_template, prompt_certifications_template, prompt_additional_skills_template

prompt_header = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a professional and polished header for the resume. The header should:

1. **Contact Information**: Include your full name, city and country, phone number, email address, and LinkedIn profile. Exclude any information that is not provided.
2. **Formatting**: Ensure the contact details are presented clearly and are easy to read.

- **My information:**  
  {personal_information}
""" + prompt_header_template

prompt_professional_summary = """
Act as an HR expert and resume writer specializing in ATS-friendly resumes. Your task is to create a compelling professional summary that highlights your key qualifications for the job. The summary should:

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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to articulate the educational background for a resume. For each educational entry, ensure you include:

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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to detail the work experience for a resume with a focus on quantifiable impact. Follow these guidelines:

1. **Company Name and Location**: Provide the name of the company and its location.
2. **Job Title**: Clearly state your job title.
3. **Dates of Employment**: Include the start and end dates of your employment.
4. **Impactful Achievements**: 
   - For the most recent job (the Data City), create 5 bullet points that highlight your contributions.
   - For the second job (Alien Technology Transfer), create 4 bullet points that highlight your contributions.
   - For other jobs, create 3 bullet points that highlight your contributions.
   - Include quantifiable metrics (numbers, percentages, dollar amounts) in most points to demonstrate impact.
   - Show specific outcomes of your work rather than just listing responsibilities.
   - Vary your approach - not every bullet needs numbers, but they should all show impact.

- **My information:**  
  {experience_details}
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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list significant achievements. For each achievement, ensure you include:

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
Act as an HR expert and resume writer with a specialization in creating ATS-friendly resumes. Your task is to list additional skills relevant to the job. For each skill, ensure you include:

1. **Skill Category**: Clearly state the category or type of skill.
2. **Specific Skills**: List the specific skills or technologies within each category.
3. **Proficiency and Experience**: Briefly describe your experience and proficiency level.

- **My information:**  
  {languages}
  {interests}
  {skills}
"""+ prompt_additional_skills_template
