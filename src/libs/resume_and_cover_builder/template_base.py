"""
This module is used to store the global configuration of the application.
"""
# app/libs/resume_and_cover_builder/template_base.py



prompt_cover_letter_template = """
- **Template to Use**
```
<section id="cover-letter">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 20px;">
        <div>
            <p>[Your Name]</p>
            <p>[Your Address]</p>
            <p>[City, State ZIP]</p>
            <p>[Your Email]</p>
            <p>[Your Phone Number]</p>
        </div>
        <div style="text-align: right;">
            <p>[Company Name]</p>
        </div>
    </div>
    <div>
    <p>Dear [Recipient Team],</p>
    <p>[Opening paragraph: Introduce yourself and state the position you are applying for.]</p>
    <p>[Body paragraphs: Highlight your qualifications, experiences, and how they align with the job requirements.]</p>
    <p>[Closing paragraph: Express your enthusiasm for the position and thank the recipient for their consideration.]</p>
    <p>Sincerely,</p>
    <p>[Your Name]</p>
    <p>[Date]</p>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the cover letter, without any explanations or additional text and also without ```html ```
"""
prompt_header_template = """
- **Template to Use**
```
<header>
  <h1>[Name and Surname]</h1>
  <div class="contact-info"> 
    <p class="fas fa-map-marker-alt">
      <span>[Your City, Your Country]</span>
    </p> 
    <p class="fas fa-phone">
      <span>[Your Prefix Phone number]</span>
    </p> 
    <p class="fas fa-envelope">
      <span>[Your Email]</span>
    </p> 
    <p class="fab fa-linkedin">
      <a href="[Link LinkedIn account]">LinkedIn</a>
    </p> 
  </div>
</header>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_professional_summary_template = """
- **Template to Use**
```
<section id="professional-summary">
    <h2>Professional Summary</h2>
    <p class="summary-paragraph">[Concise paragraph of 3-4 lines summarizing your key qualifications, experience, and value proposition for the target role. Make sure to incorporate keywords from the job description.]</p>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_education_template = """
- **Template to Use**
```
<section id="education">
    <h2>Education</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><strong>[University Name]</strong></span>
          <span class="entry-location">[Location] </span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Degree] in [Field of Study] | Grade: [Your Grade]</span>
          <span class="entry-year">[Start Year] – [End Year]  </span>
      </div>
      <ul class="compact-list">
          <li>[Relevant coursework point (6-8 words)]</li>
          <li>[Relevant coursework point (6-8 words)]</li>
      </ul>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```"""


prompt_working_experience_template = """
- **Template to Use**
```
<section id="work-experience">
    <h2>Work Experience</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><strong>[Company Name]</strong></span>
          <span class="entry-location">[Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Your Job Title]</span>
          <span class="entry-year">[Start Date] – [End Date] </span>
      </div>
      <ul class="compact-list">
          <li>[Responsibility with measurable impact and numbers] </li>
          <li>[Key achievement with quantifiable results] </li>
          <li>[Project or initiative with measurable outcome] </li>
          <li>[Technical skill or business contribution] </li>
          <li>[Strategic initiative or leadership example] </li>
      </ul>
    </div>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><strong>[Company Name]</strong></span>
          <span class="entry-location">[Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Your Job Title]</span>
          <span class="entry-year">[Start Date] – [End Date] </span>
      </div>
      <ul class="compact-list">
          <li>[Responsibility with measurable impact] </li>
          <li>[Key project or achievement] </li>
          <li>[Notable contribution or skill demonstrated]</li>
          <li>[Significant accomplishment or impact]</li>
      </ul>
    </div>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><strong>[Company Name]</strong></span>
          <span class="entry-location">[Location]</span>
      </div>
      <div class="entry-details">
          <span class="entry-title">[Your Job Title]</span>
          <span class="entry-year">[Start Date] – [End Date] </span>
      </div>
      <ul class="compact-list">
          <li>[Responsibility with measurable impact] </li>
          <li>[Key project or achievement] </li>
          <li>[Notable contribution or skill demonstrated]</li>
      </ul>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```"""


prompt_projects_template = """
- **Template to Use**
```
<section id="side-projects">
    <h2>Side Projects</h2>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><i class="fab fa-github"></i> <a href="[Github Repo or Link]">[Project Name]</a></span>
      </div>
      <ul class="compact-list">
          <li>[Describe any notable recognition or reception]</li>
          <li>[Describe any notable recognition or reception]</li>
      </ul>
    </div>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><i class="fab fa-github"></i> <a href="[Github Repo or Link]">[Project Name]</a></span>
      </div>
      <ul class="compact-list">
          <li>[Describe any notable recognition or reception]</li>
          <li>[Describe any notable recognition or reception]</li>
      </ul>
    </div>
    <div class="entry">
      <div class="entry-header">
          <span class="entry-name"><i class="fab fa-github"></i> <a href="[Github Repo or Link]">[Project Name]</a></span>
      </div>
      <ul class="compact-list">
          <li>[Describe any notable recognition or reception]</li>
          <li>[Describe any notable recognition or reception]</li>
      </ul>
    </div>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""


prompt_achievements_template = """
- **Template to Use**
```
<section id="achievements">
    <h2>Achievements</h2>
    <ul class="compact-list">
      <li><strong>[Award or Recognition or Scholarship or Honor]:</strong> [Describe]</li>
      <li><strong>[Award or Recognition or Scholarship or Honor]:</strong> [Describe]</li>
    </ul>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_certifications_template = """
- **Template to Use**
```
<section id="certifications">
    <h2>Certifications</h2>
    <ul class="compact-list">
      <li><strong>[Certification Name]:</strong> [Describe]</li>
      <li><strong>[Certification Name]:</strong> [Describe]</li>
    </ul>
</section>
```
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""

prompt_additional_skills_template = """
- **Template to Use**
'''
<section id="skills-languages">
    <h2>Additional Skills</h2>
    <div class="two-column">
      <ul class="compact-list">
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
      </ul>
      <ul class="compact-list">
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li>[Specific Skill or Technology]</li>
          <li><strong>Languages:</strong> </li>
      </ul>
    </div>
</section>
'''
The results should be provided in html format, Provide only the html code for the resume, without any explanations or additional text and also without ```html ```
"""
