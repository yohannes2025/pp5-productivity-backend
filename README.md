# 📅 Productivity App Project Frontend

The **Productivity App** project focuses on developing a **calendar-driven application** designed to help users organize their time efficiently. This **browser-based platform** allows users to create and manage **tasks and habits** effectively.
This application is built to ensure a **seamless user experience** in maintaining daily productivity through a clean, intuitive interface and smart task organization tools.

[View the website here](https://pp5-productivity-frontend.onrender.com/)

---

## Table of Contents

- [📅 Productivity App Project Frontend](#-productivity-app-project-frontend)
  - [Table of Contents](#table-of-contents)
  - [Project Goals](#project-goals)
  - [User Stories for Productivity App](#user-stories-for-productivity-app)
    - [User Story 1: Account Creation \& Login](#user-story-1-account-creation--login)
    - [Acceptance Criteria:](#acceptance-criteria)
    - [User Story 2: Profile Management](#user-story-2-profile-management)
    - [Acceptance Criteria:](#acceptance-criteria-1)
    - [User Story 3: Create Task](#user-story-3-create-task)
    - [Acceptance Criteria:](#acceptance-criteria-2)
    - [User Story 4: Set Due Date](#user-story-4-set-due-date)
      - [Acceptance Criteria:](#acceptance-criteria-3)
    - [User Story 5: Mark Task as Overdue](#user-story-5-mark-task-as-overdue)
      - [Acceptance Criteria:](#acceptance-criteria-4)
    - [User Story 6: Assign/Unassign Task Owners](#user-story-6-assignunassign-task-owners)
      - [Acceptance Criteria:](#acceptance-criteria-5)
    - [User Story 7: Set Task Priority](#user-story-7-set-task-priority)
      - [Acceptance Criteria:](#acceptance-criteria-6)
    - [User Story 8: Categorize Tasks](#user-story-8-categorize-tasks)
      - [Acceptance Criteria:](#acceptance-criteria-7)
    - [User Story 9: Set Task State](#user-story-9-set-task-state)
      - [Acceptance Criteria:](#acceptance-criteria-8)
    - [User Story 10: Task Filtering](#user-story-10-task-filtering)
      - [Acceptance Criteria:](#acceptance-criteria-9)
    - [User Story 11: Responsive Design](#user-story-11-responsive-design)
      - [Acceptance Criteria:](#acceptance-criteria-10)
  - [User Story 12: Search Functionality](#user-story-12-search-functionality)
    - [Acceptance Criteria](#acceptance-criteria-11)
  - [Break Down of User Stories into Tasks](#break-down-of-user-stories-into-tasks)
    - [User Story 1: Account Creation \& Login](#user-story-1-account-creation--login-1)
      - [Tasks:](#tasks)
    - [User Story 2: Profile Management](#user-story-2-profile-management-1)
      - [Tasks:](#tasks-1)
    - [User Story 3: Create Task](#user-story-3-create-task-1)
      - [Tasks:](#tasks-2)
    - [User Story 4: Set Due Date](#user-story-4-set-due-date-1)
      - [Tasks:](#tasks-3)
    - [User Story 5: Mark Task as Overdue](#user-story-5-mark-task-as-overdue-1)
      - [Tasks:](#tasks-4)
    - [User Story 6: Assign/Unassign Task Owners](#user-story-6-assignunassign-task-owners-1)
      - [Tasks:](#tasks-5)
    - [User Story 7: Set Task Priority](#user-story-7-set-task-priority-1)
      - [Tasks:](#tasks-6)
    - [User Story 8: Categorize Tasks](#user-story-8-categorize-tasks-1)
      - [Tasks:](#tasks-7)
    - [User Story 9: Set Task State](#user-story-9-set-task-state-1)
      - [Tasks:](#tasks-8)
    - [User Story 10: Task Filtering](#user-story-10-task-filtering-1)
      - [Tasks:](#tasks-9)
    - [User Story 11: Responsive Design](#user-story-11-responsive-design-1)
      - [Tasks:](#tasks-10)
    - [User Story 12: Search Functionality](#user-story-12-search-functionality-1)
      - [Tasks:](#tasks-11)
  - [User Story 12: Search Functionality](#user-story-12-search-functionality-2)
- [Technologies Used](#technologies-used)
  - [Front-End](#front-end)
  - [Back-End](#back-end)
  - [Tools \& Project Management](#tools--project-management)
- [Design](#design)
  - [Color Scheme](#color-scheme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)
  - [Component-Based Architecture](#component-based-architecture)
  - [Accessibility](#accessibility)
- [Agile Methodology](#agile-methodology)
  - [Version Control](#version-control)
    - [Examples](#examples)
- [Features](#features)
  - [Existing Features](#existing-features)
    - [General Features](#general-features)
    - [Navigation Bar](#navigation-bar)
    - [Home Page Component](#home-page-component)
    - [User Register Component](#user-register-component)
    - [User Login Component](#user-login-component)
    - [Create Task Component](#create-task-component)
    - [Task List Component](#task-list-component)
    - [Not Found Component](#not-found-component)
    - [Protected Route Component](#protected-route-component)
- [Testing](#testing)
  - [Manual Testing](#manual-testing)
  - [Automated Testing](#automated-testing)
  - [Known Issues](#known-issues)
- [Final Frontend Project Scope Reflection](#final-frontend-project-scope-reflection)
  - [Project Background](#project-background)
  - [What Changed](#what-changed)
  - [Final Features Implemented](#final-features-implemented)
  - [Features Postponed](#features-postponed)
  - [Reflection](#reflection)
  - [What’s Next?](#whats-next)
- [Deployment](#deployment)
  - [Render](#render)
  - [Prerequisites](#prerequisites)
  - [Step 1: Build Your React App](#step-1-build-your-react-app)
  - [Step 2: Push Your App to a Git Repository](#step-2-push-your-app-to-a-git-repository)
  - [Step 3: Create a Static Site on Render](#step-3-create-a-static-site-on-render)
  - [Step 4: Configure the Static Site Settings](#step-4-configure-the-static-site-settings)
  - [Step 5: Deploy Your App](#step-5-deploy-your-app)
  - [Step 6: Enable Automatic Deployments](#step-6-enable-automatic-deployments)
  - [Optional: Support Client-Side Routing (React Router)](#optional-support-client-side-routing-react-router)
- [Credits](#credits)
  - [Tutorials \& Code Used](#tutorials--code-used)
  - [Acknowledgments](#acknowledgments)

---

## Project Goals

The Productivity App frontend aims to deliver a user-centric, responsive platform for task management with the following specific objectives (addressing **LO2.2**):

- **Seamless Authentication**: Implement secure user registration and login using JWT, with clear feedback via react-toastify for success/errors and username display in the NavBar to indicate login status (LO4.2, LO4.7).
- **Efficient Task Management**: Enable users to create and view tasks with details like title, description, due date, priority, category, status, and assigned users, with real-time CRUD notifications (LO4.2).
- **Responsive Design**: Deliver a fully responsive UI using React and Bootstrap, ensuring accessibility across desktops, tablets, and mobiles (LO1.9).
- **Advanced Filtering**: Allow task filtering by category and status, with a search bar for title/description queries, enhancing task navigation (LO4.2).
- **Code Quality**: Maintain clean, modular code with ESLint for JavaScript and descriptive commit messages, adhering to best practices (LO1.13, LO3.1, LO3.11).
- **Agile Development**: Use GitHub Issues, Project Boards, MoSCoW prioritization, and milestones to manage development transparently (LO2.3).
- **User Feedback**: Provide immediate visual feedback for all user actions (e.g., task creation, login) using alerts and toasts, improving UX (LO4.2).

---

## User Stories for Productivity App

#### User Story 1: Account Creation & Login

**As a** new user,  
**I want to** create an account and log in,  
**so that** I can access the app and manage my tasks.

#### Acceptance Criteria:

- Allows users to register with a unique email and password.
- Enables the user to log in using an existing account.
- Provides feedback if the registration or login fails (e.g., email already exists, incorrect password).

---

#### User Story 2: Profile Management

**As a** registered user,  
**I want to** manage my profile,  
**so that** I can update my information or change my password.

#### Acceptance Criteria:

- Users can view and edit their profile information (name, profile picture, etc.).
- Users can change their password.
- Upon successful profile updates, the user receives a confirmation message.

---

#### User Story 3: Create Task

**As a** user,  
**I want to** create a task,  
**so that** I can keep track of what I need to do.

#### Acceptance Criteria:

- Provides users with a form to input task details (title, description, due date, priority, category).
- Allows users to attach files to the task.
- Saves the task and displays it in the user’s task list upon submission.

---

### User Story 4: Set Due Date

**As a** user,  
**I want to** set a due date for my tasks,  
**so that** I can manage my deadlines effectively.

#### Acceptance Criteria:

- Users can select a due date from a date picker.
- The due date is displayed on the task list and the task detail view.
- Tasks can be filtered based on due dates.

---

### User Story 5: Mark Task as Overdue

**As a** user,  
**I want to** mark tasks as overdue,  
**so that** I can prioritize tasks that are past their due date.

#### Acceptance Criteria:

- The application automatically marks the task as overdue if the current date exceeds the due date.
- Overdue tasks are visually distinct in the task list (e.g., using color coding).
- Users can manually adjust overdue statuses if necessary.

---

### User Story 6: Assign/Unassign Task Owners

**As a** user,  
**I want to** assign or unassign multiple owners to a task,  
**so that** I can collaborate with others effectively.

#### Acceptance Criteria:

- Users can select multiple users from a list to assign to a task.
- The assigned owners are displayed alongside the task details.

---

### User Story 7: Set Task Priority

**As a** user,  
**I want to** set a priority for each task (low, medium, high),  
**so that** I can focus on what’s most important.

#### Acceptance Criteria:

- Users can choose a priority level from a dropdown menu while creating/editing a task.
- The priority is visible in the task list, and users can filter tasks based on priority.

---

### User Story 8: Categorize Tasks

**As a** user,  
**I want to** categorize my tasks,  
**so that** I can organize them based on different projects or themes.

#### Acceptance Criteria:

- Users can assign categories (e.g., Work, Personal, Study) when creating/editing a task.
- Categories are displayed in the task list and can be used for filtering tasks within the app.

---

### User Story 9: Set Task State

**As a** user,  
**I want to** set the state of my task (open, in progress, done),  
**so that** I can track the status of each task at a glance.

#### Acceptance Criteria:

- Users can change the state of a task easily via dropdown options.
- The current state is clearly indicated in the task list and is updateable.

---

### User Story 10: Task Filtering

**As a** user,  
**I want to** filter my tasks based on due date, priority, category, and state,  
**so that** I can easily find the tasks I'm interested in.

#### Acceptance Criteria:

- The app provides filter options for users based on due date, priority, category, and status.
- Users can apply multiple filters at once.
- The task list updates dynamically to reflect the applied filters.

---

### User Story 11: Responsive Design

**As a** user,  
**I want to** access the application on multiple devices (desktop, tablet, mobile),  
**so that** I can manage my tasks wherever I am.

#### Acceptance Criteria:

- The app is fully responsive and functional across different screen sizes.
- Users should have a consistent experience with easy navigation and task management features.

---

## User Story 12: Search Functionality

**As a user,** I want to be able to search for tasks by keywords in their title or description,  
**so that** I can quickly find the specific tasks I am looking for.

### Acceptance Criteria

- A search bar is displayed at the top of the task list page.
- When I type a keyword into the search bar and press enter (or type continuously), the task list updates to show only tasks whose title or description matches the keyword.
- The search works regardless of letter case (case-insensitive).
- If no tasks match the keyword, a message such as **“No tasks found”** is displayed.
- Clearing the search bar restores the full list of tasks.
- The search query is processed in real time (React captures input, sends request to backend, and updates the task list dynamically).

---

> **Note:**  
> User Story 2 (**Profile Management**), and User Story 5 (**Mark Task as Overdue**), were planned but not implemented due to scope reduction, as detailed in the **Final Frontend Project Scope Reflection**.

---

## Break Down of User Stories into Tasks

### User Story 1: Account Creation & Login

#### Tasks:

1. **Design Registration Form:** Create a form with fields for email and password.
2. **Implement Backend Registration Endpoint:** Create a Django Rest Framework endpoint for user registration.
3. **Handle Form Submission:** Add logic in React to capture user input and send a POST request to the registration endpoint.
4. **Display Error Messages:** Implement error handling for registration (e.g., unique email check).
5. **Design Login Form:** Create a form with fields for email and password.
6. **Implement Backend Login Endpoint:** Create a Django Rest Framework endpoint for user login.
7. **Handle Login Logic:** Add logic in React to capture user input, send a POST request, and handle authentication (using JWT or sessions).
8. **Redirect Upon Successful Login:** Implement redirection to the main dashboard after login.

---

### User Story 2: Profile Management

#### Tasks:

1. **Design Profile Page:** Create a UI layout for user profile information editing.
2. **Implement Backend Endpoint for Profile:** Create endpoints for retrieving and updating user profile data.
3. **Handle Profile Data Fetching:** Use React to fetch and display the user data.
4. **Implement Edit Functionality:** Add logic to capture changes and send PATCH requests to update user data.
5. **Display Success/Error Messages:** Show messages based on the success or failure of profile updates.

---

### User Story 3: Create Task

#### Tasks:

1. **Design Task Creation Form:** Create a user-friendly form for creating tasks (fields for title, description, due date, etc.).
2. **Implement Backend Task Creation Endpoint:** Create a Django REST Framework endpoint to handle task creation.
3. **Handle Form Submission:** Capture task data in React and send it via a POST request to the backend.
4. **Display Confirmation/Errors:** Show confirmation of success or errors during task creation.
5. **Update Task List:** Refresh the task list on the frontend after a successful creation.

---

### User Story 4: Set Due Date

#### Tasks:

1. **Integrate Date Picker:** Add a date picker component to the task creation form.
2. **Send Due Date with Task Creation/Update:** Ensure the due date is included in the requests for task creation or updates.
3. **Display Due Date in Task List:** Update the task list UI to show due dates for each task.

---

### User Story 5: Mark Task as Overdue

#### Tasks:

1. **Define Overdue Logic:** Implement logic in the backend to check if a task is overdue based on the current date and due date.
2. **Update Task Model:** Add an “is_overdue” field to the task model, if necessary.
3. **Display Visual Indicators:** Update UI to visually distinguish overdue tasks (e.g., through color coding).
4. **Implement Filter for Overdue Tasks:** Add functionality to filter the task list by overdue status.

---

### User Story 6: Assign/Unassign Task Owners

#### Tasks:

1. **Design Owner Assignment UI:** Create a UI component to display and select task owners.
2. **Implement Backend Logic for Assignment:** Create endpoints to handle assigning and unassigning owners.
3. **Capture Owner Selection:** Add logic in React to capture selected owners and send a PATCH request upon updates.
4. **Update UI with Assigned Owners:** Display assigned owners within task details.

---

### User Story 7: Set Task Priority

#### Tasks:

1. **Add Priority Field to Task Form:** Include a dropdown for priority selection (low, medium, high) in the task creation form.
2. **Implement Backend For Priority Handling:** Modify task model and backend logic to accept priority as part of the task data.
3. **Display Priority in Task List:** Ensure that priority information is displayed in the task overview.
4. **Implement Filter by Priority:** Enable filtering tasks based on priority level.

---

### User Story 8: Categorize Tasks

#### Tasks:

1. **Create Category Selection Field:** Add a field for categorizing tasks in the task creation form.
2. **Update Backend to Handle Categories:** Modify the task model and backend to allow category assignments.
3. **Display Task Categories:** Ensure categories are visible in both the task list and details.
4. **Implement Filter by Category:** Enable filtering of tasks based on selected categories.

---

### User Story 9: Set Task State

#### Tasks:

1. **Design State Selection UI:** Include a dropdown or buttons for task states (open, in progress, done).
2. **Implement Backend Handling for Task States:** Create logic in Django to update task status.
3. **Update UI Based on Task State:** Ensure the task list reflects the current states visually.
4. **Enable State Change Functionality:** Add functionality to change states easily from the task list.

---

### User Story 10: Task Filtering

#### Tasks:

1. **Design Filter UI:** Create a filter panel with options for due date, priority, category, and state.
2. **Implement Filter Logic in Backend:** Add filtering parameters to the task retrieval endpoint.
3. **Capture Selected Filters in React:** Handle filter selections and dynamically update the task list based on applied filters.

---

### User Story 11: Responsive Design

#### Tasks:

1. **Implement CSS Framework:** Integrate Bootstrap or similar CSS framework for responsive design.
2. **Test UI Across Devices:** Verify that all components function correctly on different screen sizes (desktop, tablet, mobile).
3. **Adjust Layouts:** Modify layouts as necessary to enhance usability on smaller screens.

---

### User Story 12: Search Functionality

#### Tasks:

1. **Add Search Bar UI:** Create a search input field at the top of the task list.
2. **Implement Search Logic in Backend:** Create a search endpoint that filters tasks based on keywords in titles/descriptions.
3. **Capture Search Input in React:** Handle the input from the search bar and send the search request to the backend.
4. **Display Search Results:** Dynamically update the task list to reflect search results.

---

## User Story 12: Search Functionality

**Tasks:**

- Add Search Bar UI: Create a search input field at the top of the task list.
- Implement Search Logic in Backend: Create a search endpoint that filters tasks based on keywords in titles/descriptions.
- Capture Search Input in React: Handle the input from the search bar and send the search request to the backend.
- Display Search Results: Dynamically update the task list to reflect search results.

---

# Technologies Used

### Front-End

- **HTML5** – Semantic markup for structuring content.
- **CSS3** – Responsive styling with modern layout techniques.
- **JavaScript (ES6+)** – Dynamic behavior and logic handling.
- **React.js** – Component-based UI development.
- **JSX** – Syntax extension for writing HTML in JavaScript.
- **Bootstrap** – Styling and responsive UI components.
- **Axios** – HTTP client for API requests.
- **React Router** – Client-side routing for SPA behavior.
- \*\*React Toastify: Real-time notifications for CRUD operations (LO4.2).
- **ESLint** – Code linting to enforce code quality(L03.1).
- **Git & GitHub** – Version control and collaborative development.
- **Render** – Front-End deployment to the cloud.

### Back-End

- **Python 3** – General-purpose programming for logic and data handling.
- **Django** – High-level web framework for building the application structure.
- **Django REST Framework (DRF)** – API creation with full CRUD capabilities.
- **PostgreSQL / SQLite** – Relational database for storing user and content data.
- **djoser / Simple JWT** – Token-based authentication.
- **Git & GitHub** – Back-End version control and project tracking.
- **Render.com** – Deployment of the API to a API deployment cloud platform.
- **Environment Variables** – Securing sensitive credentials and configuration.

### Tools & Project Management

- **VS Code** – Source code editor with extensions for React and Django.
- **Balsamiq** - Wireframe creation for UI planning.
- **Chrome DevTools** - Debugging and responsiveness testing.
- **Github** - Used for project management and version control.
  GitHub's project management and version control features create a robust environment for collaborative software development. By utilizing branching, pull requests, issue tracking, project boards, and documentation tools, teams can effectively manage tasks, maintain code quality, and streamline collaboration, ultimately leading to successful project outcomes.

# Design

The design of this content-sharing platform focuses on accessibility, user experience, responsiveness, and clarity. The following practices and tools were used throughout the design and development phases:

### Color Scheme

The application's color palette is designed to promote readability, engagement, and modern aesthetics. The chosen colors follow accessibility contrast guidelines and reflect a clean, professional tone suitable for content sharing:

- **Primary Button**: #0d6efd (Bootstrap primary, buttons).
- **Success Button**: #198754 (Bootstrap success, actions).
- **Background**: #f8f8f8; – Light Gray (Page background)
- **Text**: #212529 – Dark Charcoal (Primary Text)
- **Navbar**: #DFECC6 – (Light green, navigation background).
  Colors follow WCAG contrast guidelines for accessibility.

These colors are applied consistently across components using Bootstrap’s utility classes and custom CSS variables.

---

### Typography

To ensure readability and a modern look:

- **Font Family**: `"Roboto", sans-serif;` for modern readability.
- **Heading Font Sizes**: Scaled using Bootstrap's heading classes (`h1`–`h6`)
- **Body Font Size**: `1rem` with responsive scaling
- **Font Weight**: Used to distinguish hierarchy (`600` for headings, `400` for body text)

Typography is responsive and consistent across components to maintain design uniformity and accessibility.

---

### Wireframes

Wireframes were designed during the planning phase to define layout, content structure, and user flow. They include:

- **HomePage** – Main landing page
  ![home_wireframe_pc](./src/assets/images/home_page_wireframe_pc.png)
  ![home_wireframe_mobile](./src/assets/images/home_page_wireframe_mobile.png)
  ![home_page_pc](./src/assets/images/home_page_pc.png)
- **Profile** – User profile page
  ![profile_wireframe_pc](./src/assets/images/profile_page_wireframe_pc.png)
  ![profile_wireframe_mobile](./src/assets/images/profile_page_wireframe_mobile.png)
  ![profile_page_pc](./src/assets/images/profile_page_pc.png)
- **Settings** – App and account settings
  ![settings_wireframe_pc](./src/assets/images/settings_page_wireframe_pc.png)
  ![settings_wireframe_mobile](./src/assets/images/settings_page_wireframe_mobile.png)
  ![settings_page_pc](./src/assets/images/settings_page_pc.png)
- **Tasks (Dropdown Menu)**:
  - Create Task
    ![create_task_wireframe_pc](./src/assets/images/create_task_page_wireframe_pc.png)
    ![create_task_wireframe_mobile](./src/assets/images/create_task_page_wireframe_mobile.png)
    ![create_task_page_pc](./src/assets/images/create_task_page_pc.png)
  - Edit Task
    ![edit_task_wireframe_pc](./src/assets/images/edit_task_page_wireframe_pc.png)
    ![edit_task_wireframe_mobile](./src/assets/images/edit_task_page_wireframe_mobile.png)
    ![edit_task_page_pc](./src/assets/images/Edit_task_page_pc.png)
  - Task List
    ![task_list_wireframe_pc](./src/assets/images/task_list_page_wireframe_pc.png)
    ![task_list_wireframe_mobile](./src/assets/images/task_list_page_wireframe_mobile.png)
    ![task_list_page_pc](./src/assets/images/task_list_page_pc.png)

Wireframes were created using Balsamiq and informed the React component structure and routing. All major interface elements were validated against the wireframes before implementation.

### Component-Based Architecture

- Built with React functional components for modularity.

- Functional React Components (**HomePage, Login, Register, CreateTask, TaskList, NotFound, ProtectedRoute**) handle specific UI/logic responsibilities.

- Uses **api.js** for centralized API requests.

### Accessibility

- Semantic HTML and attributes for screen reader compatibility.
- High-contrast colors and responsive typography for readability.
- Keyboard-navigable forms and buttons.
- Bootstrap’s accessible components for consistent UX.

---

# Agile Methodology

To address **LO2.3**, the project adopted agile practices using GitHub:

- **GitHub Issues**: 10 issues created, each tied to a user story (e.g., _“Implement Login Form [Must]”_, _“Add Task Filtering [Should]”_).

  - **Description**: User story, acceptance criteria, tasks.
  - **Labels**: MoSCoW prioritization (7 Must, 3 Should), component (e.g., UI, API).
  - **Assignee**: Developer (self).
  - **Milestone**: Linked to epics (Authentication, Task Management, UI).

- **Project Board**: Kanban board with columns (_Backlog, To Do, In Progress, Done_).

- **Milestones**:

  - **Authentication Epic**: Login, registration, JWT handling, NavBar username (LO4.7).
  - **Task Management Epic**: Task creation, listing, filtering.
  - **UI Epic**: Responsive design, toast notifications (LO4.2).

- **MoSCoW Prioritization**:
  - 7 “Must” features (auth, task CRUD).
  - 3 “Should” features (e.g., filtering).

✅ This ensured transparent, iterative development.

---

## Version Control

- Git & GitHub
- Commit best practices
- ESLint enforced

- The project uses Git on GitHub for version control. To address **LO1.13** and **LO3.11**, commits follow best practices:

- **Subject**: Imperative, <50 characters (e.g., _“Add toast notifications for CRUD”_).
- **Body**: Detailed, explaining _what_ and _why_.

### Examples

- _“Fix ESLint errors in CreateTask.js”_: Resolved linting issues for code quality (LO3.1).
- _“Add username display in NavBar”_: Implemented for login state clarity (LO4.7).
- _“Set up GitHub Issues for agile”_: Added agile tools to resolve LO2.3.
- Removed commented-out code to maintain clean codebase (feedback addressed).

---

# Features

## Existing Features

### General Features

- Create tasks with title, description, due date, priority, category, status, and assigned users.
- View and filter tasks by category and status.
- Search tasks by title/description.
- Real-time toast notifications for CRUD operations (LO4.2).
- Responsive design across devices (LO1.9).
- Username display in NavBar for logged-in users (LO4.7).

### Navigation Bar

- **Component**: `NavBar.js`.
- **Features**:
  - Responsive, collapses to hamburger menu on mobile.
  - Links: Home, Login, Register, Create Task, Task List (protected).
  - Displays username for logged-in users (LO4.7).
  - Uses Bootstrap + react-router-dom.
- **Purpose**: Provides intuitive navigation and login state clarity.

### Home Page Component

- **Component**: `HomePage.js`.
- **Features**:
  - Welcoming headline and subtext.
  - Call-to-action buttons for Login and Register.
  - Responsive Bootstrap layout.
- **Purpose**: Introduces the app and guides users to authenticate.

### User Register Component

- **Component**: `Register.js`.
- **Features**:
  - Form: name, email, password, confirm password.
  - POST request to `/api/register/` via `api.js`.
  - Toast notifications for success/errors (LO4.2).
  - Redirects to `/login` on success.
  - Responsive Bootstrap UI.
- **Purpose**: Enables new user onboarding.

### User Login Component

- **Component**: `Login.js`.
- **Features**:
  - Form: email + password.
  - POST request to `/api/login/` with JWT storage.
  - Toast notifications for success/errors (LO4.2).
  - Redirects to `/tasklist` on success.
  - Responsive Bootstrap UI.
- **Purpose**: Secure user authentication.

### Create Task Component

- **Component**: `CreateTask.js`.
- **Features**:
  - Form: title, description, due date (react-datepicker), priority, category, status, assigned users.
  - POST request to `/api/tasks/`.
  - Toast notifications for success/errors (LO4.2).
  - Responsive Bootstrap UI with Card.
- **Purpose**: Allows task creation with detailed inputs.

### Task List Component

- **Component**: `TaskList.js`.
- **Features**:
  - Displays tasks in table format.
  - Filters: category & status; search by title/description.
  - Toast notifications for updates (LO4.2).
  - Responsive Bootstrap UI.
- **Purpose**: Enables task viewing and management.

### Not Found Component

- **Component**: `NotFound.js`.
- **Features**:
  - Displays 404 message with image (_no-results.png_).
  - Responsive Bootstrap layout.
- **Purpose**: Handles invalid routes gracefully.

### Protected Route Component

- **Component**: `ProtectedRoute.js`.
- **Features**:
  - Restricts access to `/createtask` and `/tasklist`.
  - Redirects unauthenticated users to `/login`.
- **Purpose**: Ensures secure access to task management.

---

# Testing

## Manual Testing

**Authentication**

- Register: Valid/invalid inputs tested (duplicate email, weak password). Toast notifications confirmed (LO4.2).
- Login: Verified credentials, JWT storage, and redirects.
- Logout: Session cleared, redirect to home.
- Protected Routes: Redirects unauthenticated users to `/login`.

**Task Management**

- Create Task: All fields tested, datepicker works, toast confirmed.
- Task List: Verified display, filters, and search.
- Responsiveness: Tested on desktop, tablet, mobile.
- User Feedback: Toast notifications for all CRUD (LO4.2).

**Navigation**

- All NavBar links tested, username displayed (LO4.7).
- Routing & redirects validated.

**Error Handling**

- Error messages confirmed for invalid forms, API failures, 404 routes.

## Automated Testing

- **Component Rendering**: Jest + React Testing Library validated all components.
- **Form Interactions**: Tested input state + submissions.
- **API Integration**: Mocked Axios for `/api/register/`, `/api/login/`, `/api/tasks/`, `/api/users/` (success + errors).
- **Routing**: ProtectedRoute redirects and NavBar links tested.
- ✅ All tests passed → robust frontend.

---

## Known Issues

- Search limited to title/description (planned enhancement).
- File uploads incomplete; postponed.
- Overdue task marking not implemented (needs backend logic).
- Profile management not implemented (needs API + UI).

---

# Final Frontend Project Scope Reflection

## Project Background

The project aimed to build a comprehensive productivity app with task management, user profiles, settings, and a calendar view, inspired by professional tools like Trello and Todoist.

## What Changed

Due to time and resource constraints, the scope was narrowed to focus on core functionality to deliver a polished MVP. This decision prioritized quality over breadth, addressing critical user stories.

## Final Features Implemented

- **Authentication:** Secure login/register with JWT, toast notifications (LO4.2), and NavBar username display (LO4.7).
- **Task Management:** Create and view tasks with due dates, priority, category, status, and assigned users; includes filtering and search.
- **Responsive UI:** Bootstrap-based, mobile-friendly design (LO1.9).
- **API Integration:** Seamless connection to Django backend.

## Features Postponed

- **User Profile View:** Requires additional API endpoints and UI.
- **Settings Page:** Needs backend settings model and UI.
- **Calendar View:** Needs react-calendar or similar integration.
- **File Attachments:** Partially implemented; full functionality postponed.
- **Overdue Task Marking:** Requires backend is_overdue logic integration.

## Reflection

Reducing scope was a strategic choice to ensure a stable, high-quality MVP. This process taught the importance of prioritizing core features, maintainability, and realistic deadlines. Postponed features are planned for a future version 2.0, potentially with react-calendar and enhanced file handling.

## What’s Next?

Future enhancements include:

- Adding profile and settings views.
- Implementing calendar views.
- Enhancing file uploads and overdue task indicators.

This experience strengthened skills in practical product decisions and delivering robust software.

---

# Deployment

## Render

This guide will walk you through the complete process of deploying a React app to Render.com, using its free Static Site Hosting.

## Prerequisites

Before you begin, make sure you have:

- A React app created using create-react-app or another setup
- A GitHub, GitLab, or Bitbucket repository containing your React code
- A **Render.com** account (free signup)

## Step 1: Build Your React App

In your React project directory, **build the app for production**:

`  Bash`

`  npm run build  `

This command creates a build/ folder with all your optimized static files.

## Step 2: Push Your App to a Git Repository

If your app isn’t already pushed to GitHub:

```
   Bash

   git init  git add .
   git commit -m “Initial commit”
   git branch -M main  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
```

Make sure your code is visible on GitHub.

## Step 3: Create a Static Site on Render

Go to [Render.com](https://render.com).

- Log in or create an account.
- Click the **“New”** button and select **“Static Site”**.
- Connect your GitHub/GitLab/Bitbucket account if prompted.
- Select your React project repository.

## Step 4: Configure the Static Site Settings

Fill in the site configuration:

- **Name**: Choose a name for your site.
- **Branch**: main (or whatever branch you’re deploying).
- **Build Command**: npm run build
- **Publish Directory**: buildYou can also optionally set environment variables under the **“Advanced”** settings.

## Step 5: Deploy Your App

Click **“Create Static Site”**.Render will:

1.  Clone your repo.
2.  Install dependencies.
3.  Run npm run build.
4.  Deploy the contents of the build/ folder. After the build, your app will be live at a Render-generated domain like:  
    Live URL: https://pp5-productivity-frontend.onrender.com/

## Step 6: Enable Automatic Deployments

Render automatically redeploys your app on every push to the selected Git branch. No need to manually rebuild and redeploy!

## Optional: Support Client-Side Routing (React Router)

If you’re using **React Router** and want to avoid 404 errors on page refresh:

1.  Create a file named `_redirects ` inside the `public/ ` folder with the following content:

`/* /index.html 200`

2.  Commit and push

```
  Bash
  git add public/_redirects
  git commit -m “Add _redirects for React Router”
  git push`

```

# Credits

## Tutorials & Code Used

- **React Bootstrap:** Documentation for responsive UI components.
- **React Router:** Guides for SPA routing.
- **React Toastify:** Tutorial for implementing notifications.
- **Axios:** Documentation for API request handling.
- **React Datepicker:** Guide for date picker integration.

## Acknowledgments

- **Code Institute Student Care Team:** For their support during late submission.
- **Code Institute Staff:** For providing full-stack development training.
- **Render.com Manual:** Enabled successful deployment.
