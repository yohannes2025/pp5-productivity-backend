# Testing

## Table of Contents

- [Testing](#testing)
  - [Manual testing](#manual-testing)
  - [Automated tests](#automated-tests)
  - [Python validation](#python-validation)
  - [Resolved bugs](#resolved-bugs)
    - [Bugs found while testing the API in isolation](#bugs-found-while-testing-the-api-in-isolation)
    - [Bugs found while testing the React front-end](#bugs-found-while-testing-the-react-front-end)
  - [Unresolved bugs](#unresolved-bugs)

---

## ✅ Testing Summary

A comprehensive suite of unit and integration tests was implemented across all major components of the **Productivity App**, covering models, permissions, serializers, views, and routing. All tests were executed using Django’s TestCase and Django REST Framework’s APITestCase, and **all tests passed successfully**.

---

## Manual testing

### 📦 productivity_app/models.py Manual Tests

#### **Task Model**

- **Model Creation:** Created a Task instance in Django Admin and via shell with required and optional fields (title, description, due_date, category). Verified created_at and updated_at fields were auto-populated. No errors occurred.
- **Field Defaults:** Left status field blank during creation. Verified it defaulted to 'pending'.
- \***\*str** Method:\*\* Confirmed it returned the task title.
- **is_overdue Property:** Tested tasks with today, past, future dates and no due_date. All scenarios returned correct boolean.
- **Many-to-Many (assigned_users):** Assigned single and multiple users. Verified association, removal, and cascade deletion.

#### **File Model**

- **Model Creation:** Uploaded a file via Admin linked to a Task. Verified file saved and uploaded_at auto-populated.
- \***\*str** Method:\*\* Returned the file name.
- **Cascade Delete:** Deleted linked Task ➜ associated files deleted.

#### **Profile Model**

- **Model Creation:** Manually created a Profile and linked it to a User. Verified timestamps.
- \***\*str** Method:\*\* Returned User's name or 'Profile' when unlinked.
- **Ordering (Meta):** Confirmed descending order by created_at.

#### **Signals**

- **create_profile on user creation:** Verified profile auto-generation and proper population of name/email.

---

### 🔐 productivity_app/permissions.py Manual Tests

#### **IsAssignedOrReadOnly**

- GET as unauthenticated ➜ allowed
- POST as unauthenticated ➜ 403 Forbidden
- POST as authenticated ➜ allowed
- Object-level permissions verified for assigned users only.

#### **IsSelfOrReadOnly**

- Authenticated user updated own data ➜ allowed
- Tried to update another user ➜ denied
- Unauthenticated user ➜ denied

#### **IsOwnerOrReadOnly**

- Profile update/delete only allowed for the owner
- All reads allowed
- Unauthenticated users cannot modify

---

### 📦 productivity_app/serializers.py Manual Tests

#### **FileSerializer**

- Serialized a File instance ➜ verified output fields (id, file)

#### **UserSerializer**

- Serialized a User ➜ id, username, email present

#### **TaskSerializer**

- Serialized Task ➜ all fields verified
- Nested upload_files and assigned_users verified
- is_overdue logic correct
- Invalid input raised validation errors

#### **TaskListSerializer**

- Serialized Task ➜ output fields: id, title, due_date, is_overdue

#### **TaskDetailSerializer**

- Full output verified including nested users/files
- assigned_user_ids update successful

#### **RegisterSerializer**

- Valid registration ➜ created User + Profile
- Invalid scenarios handled (password mismatch, weak password, duplicate email, missing fields)
- Password hashed correctly

#### **LoginSerializer**

- Valid login ➜ success
- Missing or invalid credentials ➜ proper error
- Inactive user ➜ login blocked

#### **ProfileSerializer**

- Serialized Profile ➜ output showed id, name, email
- to_representation() verified

---

### 🌐 productivity_app/views.py Manual Tests

#### **ProfileViewSet**

- List: GET /api/profiles/ ➜ all visible
- Retrieve: GET own or other profile ➜ success
- Update/Delete: only own profile ➜ allowed, others ➜ 403, unauth ➜ 401

#### **TaskViewSet**

- List (auth): only assigned tasks visible
- List (unauth): all tasks visible
- Create (auth): with/without assigned_users ➜ success
- Create (unauth): 401
- Retrieve: anyone can view
- Update/Delete: permission enforced
- File upload via PATCH ➜ success

#### **UsersListAPIView**

- Auth ➜ received user list
- Unauth ➜ 401 Unauthorized

#### **UserDetailAPIView**

- Auth ➜ retrieve/update/delete self
- Unauth ➜ 401 blocked

#### **RegisterViewSet**

- Valid registration ➜ User + Profile + JWT returned
- Invalid input ➜ proper errors
- Checked for no partial data created on error

#### **LoginViewSet**

- Valid login ➜ received JWT
- Invalid credentials ➜ 401
- Missing credentials ➜ 400
- Inactive account ➜ blocked

---

### 🛣️ drf_api/urls.py Manual Tests

- Accessed `/` ➜ got welcome message
- `/admin/` ➜ login screen or 200 OK
- Verified `/api/tasks/` and all routes

---

## Automated tests

### 📦 productivity_app/models.py Tests

#### ✅ Task Model

- Task creation with required/optional fields tested
- Default values confirmed
- created_at and updated_at auto-populated
- **str**() returns task title
- is_overdue property validated
- Many-to-many relationship with assigned_users validated

#### ✅ File Model

- File creation and linkage to tasks tested
- uploaded_at auto-populated
- **str**() returns file name
- Cascade delete confirmed

#### ✅ Profile Model

- Profile creation linked to users
- Timestamps validated
- **str**() returns correct output
- Profiles ordered by created_at descending

#### ✅ Signal: create_profile

- Profile automatically created on user creation
- Name and email populated correctly

---

### 🔐 productivity_app/permissions.py Tests

#### ✅ IsAssignedOrReadOnly

- Read access allowed for all
- Write access controlled by assignment
- Object-level permission enforced

#### ✅ IsSelfOrReadOnly

- Own object write access allowed
- Others denied
- Unauthenticated denied

#### ✅ IsOwnerOrReadOnly

- Read allowed
- Write/delete allowed only to owners
- Unauthenticated blocked

---

### 🔧 productivity_app/serializers.py Tests

- FileSerializer, UserSerializer, TaskSerializer, TaskListSerializer, TaskDetailSerializer, RegisterSerializer, LoginSerializer, ProfileSerializer all tested with valid/invalid data

---

### 🌐 productivity_app/views.py Tests

- ProfileViewSet, TaskViewSet, UsersListAPIView, UserDetailAPIView, RegisterViewSet, LoginViewSet tested for authenticated/unauthenticated users, permissions, and endpoints

---

### 🧭 drf_api/urls.py Tests

- Root path `/` and `/admin/` accessible
- All productivity_app routes verified

---

## Python validation

### ✅ Model Validation

- Task, File, Profile models validated
- Bugs fixed: is_overdue TypeError, **str** methods returning None, cascade delete

### 🔐 Permissions Validation

- Validated IsAssignedOrReadOnly, IsSelfOrReadOnly, IsOwnerOrReadOnly
- Bug fixed: null check for assigned_users

### 🧾 Serializer Validation

- RegisterSerializer, LoginSerializer, TaskDetailSerializer validated
- Bugs fixed: password mismatch, missing fields, assigned_user_ids not saved

### 🌍 Views Validation

- TaskViewSet, ProfileViewSet, RegisterViewSet, LoginViewSet validated
- Bugs fixed: get_queryset for anonymous users, signals for profile creation, active user check

### 🌐 URL Validation

- Endpoints verified: /api/tasks/, /api/register/, /api/login/, /api/profiles/, /api/users/

| Component   | Bugs Found | Bugs Fixed | Validation Method          |
| ----------- | ---------- | ---------- | -------------------------- |
| Models      | 3          | ✅ 3       | Unit Tests + Shell         |
| Permissions | 1          | ✅ 1       | RequestFactory             |
| Serializers | 4          | ✅ 4       | DRF Serializer Tests       |
| Views       | 3          | ✅ 3       | APIClient + RequestFactory |
| URLs        | 0          | ✅ N/A     | URL Reverse + APIClient    |

**All Python validation tests passed successfully. All known bugs were fixed.**

---

## Resolved bugs

### Bugs found while testing the API in isolation

- Task.is_overdue TypeError
- File.**str**() failed when file missing
- Profile.**str**() returned None
- assigned_user_ids not saving in TaskDetailSerializer
- get_queryset failed for anonymous users
- LoginViewSet not checking active users

### Bugs found while testing the React front-end

- (You can fill in any front-end bugs discovered during manual/automated testing)

---

## Unresolved bugs

- None currently
