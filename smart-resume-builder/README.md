# Smart Resume Builder

## Overview
The Smart Resume Builder is a web application built with Django Rest Framework for the backend and React for the frontend. It allows users to create, customize, and manage their resumes efficiently while leveraging AI-powered features for content generation and optimization.

## Features
1. **User Authentication & Profile Management**
   - Sign up/Login with JWT Authentication
   - Social authentication (Google, LinkedIn)
   - Profile management (name, bio, skills, experience, etc.)
   - Role-based access (Admin/User)

2. **Resume Templates & Customization**
   - Pre-designed, ATS-friendly resume templates
   - Drag-and-drop resume sections (Education, Work Experience, Skills, etc.)
   - Customizable colors, fonts, and layouts

3. **AI-Powered Resume Content Generation**
   - AI-based suggestions for work experience and skills (using OpenAI API or Hugging Face models)
   - Auto-complete sections with relevant job-specific descriptions
   - Grammar and spell-checking

4. **Resume Parsing & Importing**
   - Upload existing resumes (PDF/DOCX) and extract content
   - AI-based resume analysis and improvement suggestions

5. **PDF & DOCX Resume Exporting**
   - Download resume as PDF, DOCX, or Image (PNG/JPG)
   - One-click resume sharing via email or social media

6. **Job-Specific Resume Optimization**
   - AI-driven resume scoring based on job descriptions
   - Keyword optimization for Applicant Tracking Systems (ATS)
   - Auto-highlighting relevant skills & achievements

7. **Cover Letter Generator**
   - AI-generated custom cover letters based on job descriptions
   - Customizable sections & templates

8. **Resume Analytics & Tracking**
   - Track how many times a resume was viewed/downloaded
   - Insights on which sections get the most attention (heatmaps)

9. **API for Resume Management**
   - RESTful API to create, update, delete, and retrieve resumes
   - Token-based authentication for API security

10. **Admin Dashboard**
    - Manage users and resumes
    - View analytics on resume generation trends
    - Approve or remove AI-generated suggestions

## Installation

### Backend
1. Navigate to the `backend` directory.
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

### Frontend
1. Navigate to the `frontend` directory.
2. Install the required packages:
   ```
   npm install
   ```
3. Start the development server:
   ```
   npm start
   ```

## Docker Setup
To run the application using Docker, use the following command:
```
docker-compose up --build
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.