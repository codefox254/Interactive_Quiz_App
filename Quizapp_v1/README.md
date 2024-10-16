# Ediary

Ediary is a web application that functions as a personal diary, to-do list manager, and meeting planner. It allows users to securely manage their diary entries, tasks, and meetings while providing rich text formatting, file attachments, calendar integration, and real-time synchronization across devices.

Table of Contents
Features
Installation
Usage
API Documentation
Development
Contributing
License
Features
User Account Management:

Secure login/logout
Password recovery
Profile creation and customization
Diary Entry Management:

Create, read, update, and delete diary entries
Rich text formatting
Attach images or files
To-Do List:

Add, edit, and remove tasks
Set deadlines and reminders
Categorize tasks (e.g., work, personal)
Meeting Planner:

Schedule meetings with date, time, and description
Send meeting invites via email
Sync with external calendars (Google Calendar, Outlook)
Calendar Integration:

Display diary entries and tasks in a calendar view
Import/export calendar data
Daily, weekly, and monthly views
Notifications:

Push notifications for tasks and meetings
Email notifications
Search Functionality:

Search entries by keywords, dates, or categories
Filter and sort search results
Data Backup and Restore:

Backup data to cloud storage
Easy data restoration
Cross-Platform Synchronization:

Sync data across web and Android platforms
Real-time updates
Installation
Prerequisites
Node.js
npm (Node Package Manager)
MongoDB
Firebase (for push notifications)
An email service (e.g., SendGrid)
Backend
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/ediary.git
cd ediary
Install dependencies:

bash
Copy code
npm install
Configure environment variables:
Create a .env file in the root directory and add the following:

plaintext
Copy code
PORT=3000
MONGO_URI=mongodb://localhost:27017/ediary
JWT_SECRET=your_jwt_secret
SENDGRID_API_KEY=your_sendgrid_api_key
Start the server:

bash
Copy code
npm start
Frontend
Navigate to the client directory:

bash
Copy code
cd client
Install dependencies:

bash
Copy code
npm install
Start the development server:

bash
Copy code
npm start
Android App
Open the android directory in Android Studio.
Configure Firebase for push notifications.
Build and run the application on an Android device/emulator.
Usage
Register a new user account.
Log in with your credentials.
Create diary entries, to-do tasks, and schedule meetings.
Use the calendar view to see your schedule.
Set reminders and receive notifications.
Sync data across web and Android platforms.
API Documentation
User Management
POST /api/register: Register a new user
POST /api/login: Authenticate a user
POST /api/password-recovery: Recover password
GET /api/profile: Get user profile
PUT /api/profile: Update user profile
Diary Entries
POST /api/diary-entries: Create a new diary entry
GET /api/diary-entries: Get all diary entries
GET /api/diary-entries/
: Get a specific diary entry
PUT /api/diary-entries/
: Update a diary entry
DELETE /api/diary-entries/
: Delete a diary entry
To-Do List
POST /api/todos: Add a new task
GET /api/todos: Get all tasks
GET /api/todos/
: Get a specific task
PUT /api/todos/
: Update a task
DELETE /api/todos/
: Delete a task
Meetings
POST /api/meetings: Schedule a new meeting
GET /api/meetings: Get all meetings
GET /api/meetings/
: Get a specific meeting
PUT /api/meetings/
: Update a meeting
DELETE /api/meetings/
: Delete a meeting
Calendar
GET /api/calendar: Get calendar data
POST /api/calendar/import: Import calendar data
POST /api/calendar/export: Export calendar data
Notifications
POST /api/notifications/push: Send push notification
POST /api/notifications/email: Send email notification
Development
Branching and Merging
We use GitHub Flow for branching and merging:

Create a new branch for each feature or bug fix.
Push your branch to the repository.
Create a pull request.
Request a review and merge once approved.
Deployment
Ensure all tests pass.
Merge the feature branch into main.
Deploy the main branch to the production server.
Testing
We use Jest and Cypress for testing:

Unit tests with Jest:
bash
Copy code
npm run test
End-to-end tests with Cypress:
bash
Copy code
npm run cypress:open
Contributing
We welcome contributions! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
